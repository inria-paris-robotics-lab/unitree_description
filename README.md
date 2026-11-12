Go2 description
===
This repo contains description files (urdf/srdf/...), and simple python loaders (for pinocchio model) for the Unitree Go2 and G1 robots, calibrated to INRIA Paris instances of the robot.


The urdf are taken from Unitree repo https://github.com/unitreerobotics/unitree_ros and then modified/adapted for our needs.

**Note:** Out of all the urdf provided for the unitree G1 in [this table](https://github.com/unitreerobotics/unitree_ros/blob/master/robots/g1_description/README.md), our robots correspond to the one with :
* **29 DoF**, **machine mode 5 or 6** (depending if the waist roll pitch is free or locked)
* **{14.3, 22.5}** hip.{roll, pitch} gear ratio
* **4010** wrist motors
* **with_hand** or **without** depending if the dexterous hands are mounted or not

## Python example with Pinocchio

```python
# import pinocchio
from unitree_description.loader import loadG1

pinocchio_robot_wrapper = loadG1(lock_waist=False)
```

## Developpement
### Current changes made to the URDFs
- [g1] simplifying robot name
- [g1] simplifying the collision models to convex hulls
- [g1] adding battery to the URDF

### Utils
Simplification scripts
Pythons scripts that were used to analyze and simplify the meshes can be found in [this PR](https://github.com/inria-paris-robotics-lab/unitree_description/pull/10#issuecomment-3773000247)
