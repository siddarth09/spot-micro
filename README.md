# SPOT-Micro
A combined simulation and hardware repositary for spotmicroAI

## Installation of packages
```bash
roscd
cd ../src
git clone https://github.com/chvmp/robots.git
git clone git clone -b gazebo https://github.com/chvmp/spot_ros
cd ..
rosdep install --from-path src --ignore-src -r -y

catkin_make

```

THINGS TO ADD
- [ ] Adding gmapping, karto and hector slam, if possible add rtab-map launch files
- [ ] Adding amcl and movebase files for easier understanding 
- [ ] Adding ekf and different worlds for the robot simulation
- [ ] Adding Servo,LCD and led light controls when the hardware is started
- [ ] Configuring the Navigation stack
- [ ] update documentation for tutorial, usage, application, hardware 
