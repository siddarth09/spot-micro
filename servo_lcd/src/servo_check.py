
from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory
from math import *

class SpotServoCheck:

    def __init__(self,pin_value):
        self.factory=PiGPIOFactory()
        self.min_pulse=0.25/1000
        self.max_pulse=2.75/1000
        self.pin=pin_value
        self.servo=Servo(self.pin,min_pulse_width=self.min_pulse,max_pulse_width=self.max_pulse,pin_factory=self.factory)
        self.MAX_SERVO_ANGLE=84

    def run(self,n=0):
        print("CHECKING THE SERVO...{}".format(self.pin))
        while n<10:
            for i in range(0,180):
                self.servo.value=sin(radians(i))
                sleep(0.01)
            n+=1
        print("SERVO WORKS GOOD")       

if __name__=="__main__":
    hip=SpotServoCheck(21)
    hip.run()