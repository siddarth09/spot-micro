#!/usr/bin/python3
import rospy
from spot_simulation.msg import JointAngles
import enum
from std_msgs.msg import String
from spot import SpotBehaviour
from adafruit_servokit import ServoKit 
import busio
from board import SCL,SDA

class Sleep:

    def __init__(self,calibration_mode):
        I2C=busio.I2C(SCL,SDA)
        self.calibrate=calibration_mode
        self.state=SpotBehaviour.REST
        self.joint_angles_pub=rospy.Publisher('/joint_state',JointAngles,queue_size=10)
        self.rate=rospy.Rate(1)
        self.kit=ServoKit(channels=16,i2c=I2C)

        self.robot={"Front Right":[],
                    "Back  Right":[],
                    "Front Left":[],
                    "Back  Left":[]}
        self.jointstate=JointAngles()

    def rest(self):
        #FRONT LEFT
        self.kit.servo[0].angle=90
        self.kit.servo[1].angle=0
        self.kit.servo[2].angle=0
        self.robot["Front Left"]=[90,0,0]
        
        #BACK LEFT
        self.kit.servo[4].angle=10
        self.kit.servo[5].angle=0
        self.kit.servo[6].angle=0
        self.robot["Back Left"]=[10,0,0]

        #FRONT RIGHT
        self.kit.servo[8].angle=180
        self.kit.servo[9].angle=0
        self.kit.servo[10].angle=100
        self.robot["Front Right"]=[180,0,100]

        #BACK RIGHT
        self.kit.servo[12].angle=50
        self.kit.servo[13].angle=110
        self.kit.servo[14].angle=20
        self.robot["Back Right"]=[50,110,20]
        
        self.jointstate.front_right=self.robot["Front Right"]
        self.jointstate.front_left=self.robot["Front Left"]
        self.jointstate.back_right=self.robot["Back Right"]
        self.jointstate.back_left=self.robot["Back Left"] 

        while not rospy.is_shutdown():

            self.joint_angles_pub.publish(self.jointstate)
            rospy.loginfo(self.jointstate)
            self.rate.sleep()


if __name__ =="__main__":
    rospy.init_node("sleep node")
    robot=Sleep(True)
    robot.rest()
        

    
