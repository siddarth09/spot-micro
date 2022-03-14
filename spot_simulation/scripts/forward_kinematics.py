#SPOT_FORWARD
from numpy import *   # imports all function so we don't have to use np.function()
import numpy as np
import math 

# Physical dimensions and Link lengths
L = 6.2  # length of Robot m
W = 5.2  # width of Robot m
L1 = 4.0 # The Length of Side Swing Joint
L2 = 12.5  # The Length of Hip Joint
L3 = 12.5 #The Length of Knee Joint
#variables 
class kinematics:
    def __init__(self,theta_1,theta_2,theta_3):

    

        self.t1 = math.degrees(theta_1)  # theta 1 in radians
        self.t2 = math.degrees(theta_2)  # theta 2 in radians
        self.t3 = math.degrees(theta_3)  # theta 3 in radians   
    def t(self):

        T01= np.array([[np.cos(self.t1),-np.sin(self.t1),0,(-L1*np.cos(self.t1))],[np.sin(self.t1),np.cos(self.t1),0,(-L1*np.sin(self.t1))],[1,0,0,0],[0,0,0,1]])
        T12= np.array([[0,0,-1,0],[-1,0,0,0],[0,0,1,0],[0,0,0,1]])
        T23=np.array([[np.cos(self.t2),-np.sin(self.t2),0,(L2*np.cos(self.t2))],[np.sin(self.t2),np.cos(self.t2),0,(L2*np.sin(self.t2))],[0,0,1,0],[0,0,0,1]])
        T34=np.array([[np.cos(self.t3),-np.sin(self.t3),0,(L3*np.cos(self.t3))],[np.sin(self.t3),np.cos(self.t3),0,(L3*np.sin(self.t3))],[0,0,1,0],[0,0,0,1]])

        T04=T01@T12@T23@T34 
        print(matrix(T04))
        x=T04[0][3]
        y=T04[1][3]
        Z=T04[2][3]
        return x,y,Z

if __name__=="__main__":
    o=kinematics(110,100,90)
    o.t()
    

