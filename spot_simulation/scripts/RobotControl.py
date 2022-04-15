#!/usr/bin/python3
import os
from std_msgs.msg import Int64,Bool
import rospy
from spot import SpotBehaviour
from SleepMode import Sleep
from StandMode import Stance

subscribed_state=3
class Ramu:

    def __init__(self,calibrate):

        self.calibration_mode=False
        self.default_state=SpotBehaviour.REST
        
        self.sleep=True
        self.Stand=True
        self.crawl=True

    def state_callback(self,msg):
        robot_state=msg.data
        subscribed_state=robot_state
        
        #rospy.loginfo(subscribed_state)
        while True:
            #rospy.loginfo(self.subscribed_state)
            if subscribed_state==0:
                Sleep(False).rest()
                rospy.loginfo("RESTING")
            elif subscribed_state==3:
                Stance(False).stand()
                rospy.loginfo("STAND")


    def state_pubilsher(self):

        #rospy.loginfo(self.subscribed_state)
        while not rospy.is_shutdown():
            #rospy.loginfo(self.subscribed_state)
            if subscribed_state==0:
                Sleep(False).rest()
                rospy.loginfo("RESTING")
            elif subscribed_state==3:
                Stance(False).stand()
                rospy.loginfo("STAND")
        
if __name__=="__main__":

    spot=Ramu(True)
    rospy.init_node('robot_control')
    rospy.Subscriber('/spot_state',Int64,spot.state_callback)
    spot.state_pubilsher()