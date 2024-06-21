#!/usr/bin/python3
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist,Point,Pose,Quaternion,Vector3
from sensor_msgs.msg import Imu
from IMU import mpu6050
from math import *
import numpy as np

from tf.transformations import quaternion_about_axis

class IMU():
    def __init__(self):

        self.x=0
        self.y=0
        self.yaw=0
        self.imuvalues=mpu6050(0x68)
       
        
        self.accelaration_data=self.imuvalues.get_accel_data()
        self.gyroscope=self.imuvalues.get_gyro_data()
        self.rate=rospy.Rate(10)

    def measurement_update(self):
        
        imu=Imu()

        imu_pub=rospy.Publisher('imu',Imu,queue_size=10)

        while not rospy.is_shutdown():
           
            imu.header.stamp=rospy.Time().now()
            imu.header.frame_id='imu_link'
            imu.linear_acceleration.x=self.accelaration_data['x']
            imu.linear_acceleration.y=self.accelaration_data['y']
            imu.linear_acceleration.z=self.accelaration_data['z']
            accel = self.accelaration_data.values
            ref = np.array([0, 0, 1])
            acceln = accel / np.linalg.norm(accel)
            axis = np.cross(acceln, ref)
            angle = np.arccos(np.dot(acceln, ref))
            orientation = quaternion_about_axis(angle, axis)
            o = imu.orientation
            o.x, o.y, o.z, o.w = orientation

            imu.angular_velocity.x=self.gyroscope['x']
            imu.angular_velocity.y=self.gyroscope['y']
            imu.angular_velocity.z=self.gyroscope['z']
            imu_pub.publish(imu)
            rospy.loginfo(imu)
            self.rate.sleep()

    

if __name__=="__main__":

    rospy.init_node('imu')
    robot=IMU()
    robot.measurement_update()
