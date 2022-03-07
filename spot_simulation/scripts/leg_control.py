#! /usr/bin/python3

from math import *
import time
from board import SCL,SDA
import busio
import rospy
from adafruit_pca9685 import PCA9685,PWMChannel
from adafruit_servokit import ServoKit

from spot_simulation.scripts.kinematics import Kinematics
from spot_simulation.msg import gait_state
i2c=busio.I2C(SCL,SDA)

class control:
    
    def __init__(self):

        self.min_pulse=580
        self.max_pulse=2350
        self.num_servos=rospy.get_param("num_servos")
        self.kit=ServoKit(channels=16)
        self.MAX_SERVO_ANGLE=84
        self.pca=PCA9685(i2c)
        self.pca.frequency=80
        self.servo_offset=[180,90,90]
        self.contoller=Kinematics()

        self.gait=gait_state()

        self.servokit=ServoKit()
        

    def joint_callback(self,msg):

        return msg.status,msg.theta1,msg.theta2,msg.theta3

    def send_servo_cmd(self):
        status,t1,t2,t3= self.joint_callback()

        self.gait.status=status
        self.gait.theta1=t1
        self.gait.theta2=t2
        self.gait.theta3=t3
        angles=[t1,t2,t3]

        if status=="SLEEPING":
            # only one leg
            self.servokit.servo[0].angle=90
        elif status=="STANDING":
            self.servokit.servo[0].angle=145
            self.servokit.servo[1].angle=90
        elif status=="RELAXING":

            for i in range(3):
                self.servokit.servo[i].angle=angles[i]
    

