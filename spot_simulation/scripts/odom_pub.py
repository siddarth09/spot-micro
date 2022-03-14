#!/usr/bin/python
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist,Point,Pose,Quaternion,Vector3
from sensor_msgs.msg import Imu

from IMU import mpu6050
from math import *
import tf


class robotOdom():

    def __init__(self):

        self.x=0
        self.y=0
        self.yaw=0
        self.imuvalues=mpu6050(0x68)
       
        
        self.accelaration_data=self.imuvalues.get_accel_data()
        self.gyroscope=self.imuvalues.get_gyro_data()
        self.rate=rospy.Rate(1)

        #odom values
        self.odom_broadcaster=tf.TransformBroadcaster()
    
            

    def IMU(self):
        
        imu=Imu()

        imu_pub=rospy.Publisher('imu',Imu,queue_size=10)

        while not rospy.is_shutdown():
           
            imu.header.stamp=rospy.Time().now()
            imu.header.frame_id='imu_link'
            imu.linear_acceleration.x=self.accelaration_data['x']
            imu.linear_acceleration.y=self.accelaration_data['y']
            imu.linear_acceleration.z=self.accelaration_data['z']

            imu.angular_velocity.x=self.gyroscope['x']
            imu.angular_velocity.y=self.gyroscope['y']
            imu.angular_velocity.z=self.gyroscope['z']
            imu_pub.publish(imu)
            #rospy.loginfo(imu)
            self.rate.sleep()

    def ODOM(self):
        odom_pub=rospy.Publisher('odom',Odometry,queue_size=15)
        vx=self.accelaration_data['x']/16384.0
        vy=self.accelaration_data['y']/16384.0
        vth=self.gyroscope['z']
        th=self.yaw

        current_time=rospy.Time.now()
        last_time=rospy.Time.now()

        dt = (current_time - last_time).to_sec()
        delta_x = (vx * cos(th) - vy * sin(th)) * dt
        delta_y = (vx * sin(th) + vy * cos(th)) * dt
        delta_th = vth * dt

        self.x+=delta_x
        self.y+=delta_y
        self.yaw+=delta_th

        #converting euler to quaternion
        quaternion=tf.transformations.quaternion_from_euler(0,0,self.yaw)
        
        #sending tf
        self.odom_broadcaster.sendTransform(
                                            (self.x, self.y, 0.),
                                            quaternion,
                                            current_time,
                                            "base_link",
                                            ""
                                            )
        odom=Odometry()
        odom.header.frame_id='odom'
        odom.pose.pose=Pose(Point(self.x,self.y,0),Quaternion(quaternion))
        odom.child_frame_id = "base_link"
        odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vth))
        #publishing odom
        while not rospy.is_shutdown():
            
            odom_pub.publish(odom)
            rospy.loginfo(odom)
            self.rate.sleep()

    def main(self):
        self.IMU()
        self.ODOM()

if __name__=="__main__":

    rospy.init_node('imunode')
    robot=robotOdom()
    robot.IMU()
    robot.ODOM()
    
        


