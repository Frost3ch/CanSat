from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory
import os
from picamera2.encoders import H264Encoder
from picamera2 import Picamera2
import time

picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

os.system('cd /home/alp/CanSatImages')
dirs = os.listdir('/home/alp/CanSatImages')
print(dirs)
dirName = str(int(dirs[-1].split('.')[0])+1)

encoder = H264Encoder(bitrate=10000000)
output = f"/home/alp/CanSatImages/{dirName}.h264" 
picam2.start_recording(encoder, output)

os.system('sudo pigpiod')
factory = PiGPIOFactory()
ServoT = Servo(12,min_pulse_width=0.5/1000, max_pulse_width=2.5/1000,pin_factory=factory)
ServoB = Servo(13,min_pulse_width=0.5/1000, max_pulse_width=2.5/1000,pin_factory=factory)

rMin = -0.8
rMax = 0.8
bMax = 1
bMin = -1
gaps = 10
rotation = 20
sTime = 0.1
angleT = (rMax-rMin)/gaps
angleB = (bMax-bMin)/rotation

for i in range(int(gaps/2)):
    print(i)
    ServoT.value = rMin+angleT*i
    for j in range(rotation):
        ServoB.value = bMin+angleB*j
        sleep(sTime)
    ServoT.value = rMax-angleT*i
    for k in range(rotation):
        ServoB.value=bMax-angleB*k
        sleep(sTime)

picam2.stop_recording()
