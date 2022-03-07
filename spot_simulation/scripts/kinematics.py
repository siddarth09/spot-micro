import rospy
from spot_simulation.msg import gait_state
from geometry_msgs.msg import Pose, Twist
from math import *
import time

class Kinematics:

    def __init__(self):

        self.link1= rospy.get_param('kinematics/l1')
        self.link2= rospy.get_param('kinematics/l2')
        self.link3= rospy.get_param('kinematics/l3')
        self.x=rospy.get_param('kinematics/X')
        self.y=rospy.get_param('kinematics/Y')
        self.z=rospy.get_param('kinematics/Z')
        self.angle_pub=rospy.Publisher('/joint_state',gait_state,queue_size=10)
        self.angles=[]
        self.gait=gait_state()
        self.rate=rospy.Rate(1)
    def inverseKinematics(self):
       
       
        rospy.loginfo('PARAMETERS LOADED....')
        D1=(pow(self.x,2)+pow(self.y,2)-pow(self.link3,2)+pow(self.z,2)-pow(self.link2,2)-pow(self.link3,2))
        D2=2*self.link2*self.link3
        D=D1/D2
        F=sqrt(pow(self.x,2)+pow(self.y,2)-pow(self.link1,2))
        theta1=-atan2(self.y,self.x)-atan2(F,-self.link1)
        theta3=atan2(sqrt(1-pow(D,2)),D)
        
        theta2=atan2(self.z,F)-atan2(self.link3*sin(theta3),self.link2+self.link3*cos(theta3))
        


        return theta1,theta2,theta3

    def Sleep(self):

        self.gait.status="Sleeping"
        self.gait.angles=[0,0,0]
        while not rospy.is_shutdown():
            self.angle_pub.publish(self.gait)
            self.rate.sleep()

        rospy.loginfo(self.gait)

        

    



if __name__=="__main__":

    rospy.init_node('kinematics')
    spot=Kinematics()
    spot.Sleep()

        
