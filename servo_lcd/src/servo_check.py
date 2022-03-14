

from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory
from math import *
import time
from board import SCL,SDA
import busio

from adafruit_pca9685 import PCA9685,PWMChannel
from adafruit_servokit import ServoKit


i2c=busio.I2C(SCL,SDA)

class SpotServoCheck:

    def __init__(self,pin_value):
        #self.factory=PiGPIOFactory()
        self.min_pulse=580
        self.max_pulse=2350
        self.pin=pin_value
        self.kit=ServoKit(channels=16)
        #self.servo=Servo(,min_pulse_width=self.min_pulse,max_pulse_width=self.max_pulse,pin_factory=self.factory)
        self.MAX_SERVO_ANGLE=84
        self.pca=PCA9685(i2c)
        self.pca.frequency=80
        self.kit.servo[0].angle=0

    def run(self,n=0):
        print("CHECKING THE SERVO...{}".format(self.pin))
        while n<10:
            for i in range(0,180):
                self.servo.value=sin(radians(i))
                sleep(0.01)
            n+=1
        print("SERVO WORKS GOOD")  

    def test(self):
        
        for i in range(0,180,20):
            self.kit.servo[0].angle=i
            print(i)
            time.sleep(1) 
        

if __name__=="__main__":
    hip=SpotServoCheck(21)
    hip.test()