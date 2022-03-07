#SPOT_FORWARD
from numpy import *   
import numpy as np

# Physical dimensions and Link lengths
L = 6.2  # length of Robot m
W = 5.2  # width of Robot m
L1 = 0  # The Length of Side Swing Joint
L2 = 6.9  # The Length of Hip Joint
L3 = 0  #The Length of Knee Joint
pi = 3.14
# AnglesFrom odom topic 
phi=45 #The Yaw Angle of Robot ϕ
psi= 45 # The Pitch Angle of Robot ψ
omega = 45 #The Roll Angle of Robot ω
#converting into radians 
phi =(phi/180)*pi
psi=(psi/180)*pi
omega =(omega/180)*pi
#variables 
theta_1 = int(input("The Angle of Side Swing Joint"))  
theta_2 = int(input("The Angle of Hip Joint "))  
theta_3 = int(input("The Angle of Knee Joint"))

theta_1 = (theta_1/180)*pi  # theta 1 in radians
theta_2 = (theta_2/180)*pi  # theta 2 in radians
theta_3 = (theta_3/180)*pi  # theta 3 in radians
#Need to get this coordinates  
xm=0
ym=0
zm=0
 
Rx = np.array([
        [1, 0, 0, 0], 
        [0, np.cos(omega), -np.sin(omega), 0],
        [0,np.sin(omega),np.cos(omega),0],
        [0,0,0,1]])

Ry = np.array([
        [np.cos(phi),0, np.sin(phi), 0], 
        [0, 1, 0, 0],
        [-np.sin(phi),0, np.cos(phi),0],
        [0,0,0,1]])

Rz = np.array([
        [np.cos(psi),-np.sin(psi), 0,0], 
        [np.sin(psi),np.cos(psi),0,0],
        [0,0,1,0],
        [0,0,0,1]])

Rxyz=Rx@Ry@Rz
#print(Rxyz)

T = np.array([[0,0,0,xm],[0,0,0,ym],[0,0,0,zm],[0,0,0,0]])
Tm = np.add(T,Rxyz)

Trb = Tm @ np.array([
        [np.cos(pi/2),0,np.sin(pi/2),-L/2],
        [0,1,0,0],
        [-np.sin(pi/2),0,np.cos(pi/2),-W/2],
        [0,0,0,1]])

Trf = Tm @ np.array([
        [np.cos(pi/2),0,np.sin(pi/2),L/2],
        [0,1,0,0],
        [-np.sin(pi/2),0,np.cos(pi/2),-W/2],
        [0,0,0,1]])

Tlf = Tm @ np.array([
        [np.cos(pi/2),0,np.sin(pi/2),L/2],
        [0,1,0,0],
        [-np.sin(pi/2),0,np.cos(pi/2),W/2],
        [0,0,0,1]])

Tlb = Tm @ np.array([
        [np.cos(pi/2),0,np.sin(pi/2),-L/2],
        [0,1,0,0],
        [-np.sin(pi/2),0,np.cos(pi/2),W/2],
        [0,0,0,1]])
                 
#Transformation matrix
T01= np.array([[np.cos(theta_1),-np.sin(theta_1),0,(-L1*np.cos(theta_1))],[np.sin(theta_1),np.cos(theta_1),0,(-L1*np.sin(theta_1))],[1,0,0,0],[0,0,0,1]])
T12= np.array([[0,0,-1,0],[-1,0,0,0],[0,0,1,0],[0,0,0,1]])
T23=np.array([[np.cos(theta_2),-np.sin(theta_2),0,(L2*np.cos(theta_2))],[np.sin(theta_2),np.cos(theta_2),0,(L2*np.sin(theta_2))],[0,0,1,0],[0,0,0,1]])
T34=np.array([[np.cos(theta_3),-np.sin(theta_3),0,(L3*np.cos(theta_3))],[np.sin(theta_3),np.cos(theta_3),0,(L3*np.sin(theta_3))],[0,0,1,0],[0,0,0,1]])

T04=T01@T12@T23@T34

print(matrix(T04))
