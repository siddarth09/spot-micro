#!/usr/bin/python3

from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory
from math import *
import time
from board import SCL,SDA
import busio
from adafruit_extended_bus import ExtendedI2C as I2C
from adafruit_pca9685 import PCA9685,PWMChannel
from adafruit_servokit import ServoKit


i2c1=busio.I2C(SCL,SDA)
i2c2=busio.I2C(SCL,SDA)

class SpotServoCheck:

    def __init__(self):
        #self.factory=PiGPIOFactory()
        self.min_pulse=580
        self.max_pulse=2350
        
        self.kit=ServoKit(channels=16,i2c=i2c1)
        self.kit2=ServoKit(channels=16,i2c=i2c2)
        #self.servo=Servo(,min_pulse_width=self.min_pulse,max_pulse_width=self.max_pulse,pin_factory=self.factory)
        self.MAX_SERVO_ANGLE=84
        

  

    def STANCE(self):
        #BACK LEFT
        self.kit.servo[0].angle=165
        self.kit.servo[1].angle=20
        self.kit.servo[2].angle=0
        #FRONT LEFT
        self.kit.servo[4].angle=55
        self.kit.servo[5].angle=20
        self.kit.servo[6].angle=0

         #BACK RIGHT
        self.kit.servo[8].angle=80
        self.kit.servo[9].angle=30
        self.kit.servo[10].angle=0

        #FRONT RIGHT
        self.kit.servo[12].angle=60
        self.kit.servo[13].angle=75

        self.kit.servo[14].angle=0

    def SLEEP(self):
        #FRONT LEFT
        self.kit.servo[0].angle=0
        self.kit.servo[1].angle=0
        self.kit.servo[2].angle=0
        #BACK LEFT
        self.kit.servo[4].angle=0
        self.kit.servo[5].angle=0
        self.kit.servo[6].angle=0
      #BACK RIGHT
        self.kit.servo[8].angle=180
        self.kit.servo[9].angle=60
        self.kit.servo[10].angle=0

        #FRONT RIGHT
        self.kit.servo[12].angle=50
        self.kit.servo[13].angle=110

        self.kit.servo[14].angle=20

        

        #self.kit.servo[1].angle=0
        
        
    def test(self):
        

        #Shoulder
        self.kit.servo[2].angle=0
        self.kit.servo[6].angle=0
        self.kit.servo[10].angle=0
        self.kit.servo[14].angle=0

         #Knee
        self.kit.servo[0].angle=90
        self.kit.servo[4].angle=0
        self.kit.servo[8].angle=160
        self.kit.servo[12].angle=80

        #HIP
        
        self.kit.servo[1].angle=0
        self.kit.servo[5].angle=0
        self.kit.servo[9].angle=60
        self.kit.servo[13].angle=110

if __name__=="__main__":
    hip=SpotServoCheck()
    
    ''' hip.SLEEP()
    time.sleep(5)
    hip.STANCE()
    time.sleep(8)
    hip.SLEEP()'''
    '''time.sleep(3)'''
   # hip.STANCE()
    hip.SLEEP()
   # hip.test()
    
