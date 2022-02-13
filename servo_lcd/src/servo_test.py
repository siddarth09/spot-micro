#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import rospy
from std_msgs.msg import String

servo1=17
ledpin= 16
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledpin,GPIO.OUT)
GPIO.setup(servo1,GPIO.OUT)
pwm=GPIO.PWM(servo1,50)
pwm.start(2.5)
def servo():
    servopub=rospy.Publisher('servostatus',String,queue_size=10)
    rate=rospy.Rate(1)
    pwm.ChangeDutyCycle(0)
    while not rospy.is_shutdown():
        msg=String()
        msg.data="SERVO TURNED ON"
        servopub.publish(msg)
        pwm.ChangeDutyCycle(0)
        try:
            pwm.ChangeDutyCycle(5)
            GPIO.output(ledpin, GPIO.HIGH)
            msg.data="-90 position"
            servopub.publish(msg)
            time.sleep(2)
            pwm.ChangeDutyCycle(7.5)
            GPIO.output(ledpin, GPIO.LOW)
            msg.data="neutral position"
            servopub.publish(msg)
            time.sleep(2)
            pwm.ChangeDutyCycle(10)
            GPIO.output(ledpin, GPIO.HIGH)
            msg.data="+90 position"
            servopub.publish(msg)
            time.sleep(2)
        except KeyboardInterrupt as e:
            GPIO.output(ledpin, GPIO.LOW)
            pass
        pwm.ChangeDutyCycle(0)   
        
        #rospy.loginfo(msg)
        rate.sleep()
    
if __name__=="__main__":
    rospy.init_node("servo")
    servo()