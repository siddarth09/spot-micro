#!/usr/bin/python3
from math import *
import time
from board import SCL,SDA
import busio
import rospy
from adafruit_pca9685 import PCA9685,PWMChannel
from adafruit_servokit import ServoKit
from spot_simulation.msg import JointAngles
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
        #self.contoller=Kinematics()
        self.state="Sleep"
       

        self.servokit=ServoKit(channels=16,frequency=50)

    

    
    def joint_controller(self,gait):
        gait=JointAngles()
       
        print("BODY READY TO MOVE")
        rospy.loginfo("ANGLES RECIEVED FROM MASTER")

        rospy.loginfo(gait)

        '''for i in range(5):

            if(i==0):
               self.servokit.servo[0].angle=gait.front_left[0]
               self.servokit.servo[1].angle=gait.front_left[1]
               #self.servokit.servo[2]=gait.front_left[2]
            else:
                pass'''
                



        

    
    

if __name__=="__main__":
    rospy.init_node("leg")
    robot=control()
    rospy.Subscriber('/joint_state',JointAngles,robot.joint_controller)
    rospy.spin()
    

