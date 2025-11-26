Go2 description
===
This repo contains description files (urdf/srdf/...), and simple python loaders (for pinocchio model) for the Unitree Go2 and G1 robots, calibrated to INRIA Paris instances of the robot.

The urdf are taken from Unitree repo https://github.com/unitreerobotics/unitree_ros and then modified/adapted for our needs.

**Note:** Out of all the urdf provided for the unitree G1 in [this table](https://github.com/unitreerobotics/unitree_ros/blob/master/robots/g1_description/README.md), our robots correspond to the one with :
* **29 DoF**, **machine mode 5 or 6** (depending if the waist roll pitch is free or locked)
* **{14.3, 22.5}** hip.{roll, pitch} gear ratio 
* **4010** wrist motors
* **with_hand** or **without** depending if the dexterous hands are mounted or not