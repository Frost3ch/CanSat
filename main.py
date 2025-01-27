from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory
import os

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
    servoT.value = rMin+angleT*i
    for j in range(rotation):
        servoB.value = bMin+angleB*j
        sleep(sTime)
    servoT.value = rMax-angleT*i
    for k in range(rotation):
        servoB.value=bMax-angleB*k
        sleep(sTime)