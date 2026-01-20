import pinocchio as pin
from .path import *

def loadGo2() -> pin.RobotWrapper:
    robot = pin.RobotWrapper.BuildFromURDF(GO2_DESCRIPTION_URDF_PATH, [GO2_DESCRIPTION_PACKAGE_DIR], pin.JointModelFreeFlyer())

    # Reference configurations
    pin.loadReferenceConfigurations(robot.model, GO2_DESCRIPTION_SRDF_PATH)

    # Collision pairs
    robot.collision_model.removeAllCollisionPairs()
    robot.collision_model.addAllCollisionPairs()
    pin.removeCollisionPairs(robot.model, robot.collision_model, GO2_DESCRIPTION_SRDF_PATH)

    return robot


def loadG1() -> pin.RobotWrapper:
    robot = pin.RobotWrapper.BuildFromURDF(G1_DESCRIPTION_URDF_PATH, [G1_DESCRIPTION_PACKAGE_DIR], pin.JointModelFreeFlyer())

    # Reference configurations
    pin.loadReferenceConfigurations(robot.model, G1_DESCRIPTION_SRDF_PATH)

    # Collision pairs
    robot.collision_model.removeAllCollisionPairs()
    robot.collision_model.addAllCollisionPairs()
    pin.removeCollisionPairs(robot.model, robot.collision_model, G1_DESCRIPTION_SRDF_PATH)

    return robot