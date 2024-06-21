
import rospy 
from spot_simulation.srv import BehaviourResponse,Behaviour
from tf.transformations import euler_from_quaternion
from sensor_msgs.msg import Imu
import sys, select, termios, tty
import numpy as np
import enum
from std_msgs.msg import String

class SpotBehaviour(enum.Enum):
        REST = 0
        TROT = 1
        CRAWL = 2
        STAND = 3

class Controller:

    def __init__(self):

        self.behaviour=SpotBehaviour.REST

        self.roll=0.0
        self.pitch=0.0
        self.settings = termios.tcgetattr(sys.stdin)
        self.state="REST"
        self.state_pub=rospy.Publisher('spot_state',String,queue_size=10)
        self.rate=rospy.Rate(10)

    def imu_callback(self,msg):
        q=msg.orientation
        rpy_values=euler_from_quaternion([q.x,q.y,q.z,q.w])
        self.roll=rpy_values[0]
        self.pitch=rpy_values[1]

    def getKey(self):
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            key = sys.stdin.read(1)
        else:
            key = ''
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key
    def state_commander(self):
        robot=String
        while not rospy.is_shutdown():
            key=self.getKey()
            print(key)
            if key=='w':
                self.behaviour=SpotBehaviour.STAND
                robot.data="STANDING"
                rospy.loginfo("STANDING")
                self.state_pub.publish(robot)
            elif key=='a':
                self.behaviour=SpotBehaviour.CRAWL
                robot.data="CRAWLING"
                rospy.loginfo("CRAWLING")
                self.state_pub.publish(robot)
            elif key=='d':
                self.behaviour=SpotBehaviour.TROT
                robot.data="TROT"
                rospy.loginfo("TROT")
                self.state_pub.publish(robot)
            elif key=='w':
                self.behaviour=SpotBehaviour.REST
                robot.data="REST"
                rospy.loginfo("REST")
                self.state_pub.publish(robot)

            self.rate.sleep()
    
                



if __name__=="__main__":
    rospy.init_node('controller')
    robot= Controller()
    robot.state_commander()
    rospy.Subscriber('imu',Imu,robot.imu_callback)
    rospy.spin()
    


