#!/usr/bin/python3
import rospy
from spot_simulation.msg import JointAngles
import enum
from std_msgs.msg import Int64,Bool
from spot import SpotBehaviour
from adafruit_servokit import ServoKit 
import busio
from board import SCL,SDA

class Stance:

    def __init__(self,calibration_mode):
        I2C=busio.I2C(SCL,SDA)
        self.calibrate=calibration_mode
        
        self.joint_angles_pub=rospy.Publisher('/joint_state',JointAngles,queue_size=10)
        self.rate=rospy.Rate(1)
        self.kit=ServoKit(channels=16,i2c=I2C)

        self.robot={"Front Right":[],
                    "Back  Right":[],
                    "Front Left":[],
                    "Back  Left":[]}

        self.jointstate=JointAngles()

    def stand(self):
        #BACK LEFT
        self.kit.servo[0].angle=135
        self.kit.servo[1].angle=15
        self.kit.servo[2].angle=115
        self.robot["Back Left"]=[135,15,115]
        
        #FRONT LEFT
        self.kit.servo[4].angle=65
        self.kit.servo[5].angle=15
        self.kit.servo[6].angle=10
        self.robot["Front Left"]=[60,15,10]

        #FRONT RIGHT
        self.kit.servo[8].angle=120
        self.kit.servo[9].angle=0
        self.kit.servo[10].angle=130
        self.robot["Front Right"]=[120,0,130]

        #BACK RIGHT
        self.kit.servo[12].angle=100
        self.kit.servo[13].angle=110
        self.kit.servo[14].angle=0
        self.robot["Back Right"]=[100,110,0]
        
        self.jointstate.front_right=self.robot["Front Right"]
        self.jointstate.front_left=self.robot["Front Left"]
        self.jointstate.back_right=self.robot["Back Right"]
        self.jointstate.back_left=self.robot["Back Left"] 

        while not rospy.is_shutdown():

            self.joint_angles_pub.publish(self.jointstate)
            #rospy.loginfo(self.jointstate)
            self.rate.sleep()

   

if __name__ =="__main__":
    rospy.init_node("stance node")
    
    robot=Stance(True)
   
   
        

    
