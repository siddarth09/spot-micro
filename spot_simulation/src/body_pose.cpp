#include <iostream>
#include <geometry_msgs/Pose.h>
#include <ros/ros.h>


void posecb(const geometry_msgs::Pose::ConstPtr& pose)
{
    float x,y,z;
    float rx,ry,rz,w;
    ROS_INFO("BODY POSITION");
    x=pose->position.x;
    y=pose->position.y;
    z=pose->position.z;
    rx=pose->orientation.x;
    ry=pose->orientation.y;
    rz=pose->orientation.z;
    w=pose->orientation.w;
    std::cout<<"x="<<x;
}

int main(int argc, char** argv )
{
    ros::init(argc,argv,"body_pose");
    ros::NodeHandle nh;

    ros::Subscriber sub = nh.subscribe("/body_pose", 1, posecb);
    ros::spin();
}   

