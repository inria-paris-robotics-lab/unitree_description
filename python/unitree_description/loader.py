# ruff: noqa: F403, F405
# ignore ruff formating error for import * & undefined imports
import pinocchio as pin
from .path import *


def loadGo2() -> pin.RobotWrapper:
    robot = pin.RobotWrapper.BuildFromURDF(
        GO2_DESCRIPTION_URDF_PATH,
        [GO2_DESCRIPTION_PACKAGE_DIR],
        pin.JointModelFreeFlyer(),
    )

    # Reference configurations
    pin.loadReferenceConfigurations(robot.model, GO2_DESCRIPTION_SRDF_PATH)

    # Collision pairs
    robot.collision_model.removeAllCollisionPairs()
    robot.collision_model.addAllCollisionPairs()
    pin.removeCollisionPairs(
        robot.model, robot.collision_model, GO2_DESCRIPTION_SRDF_PATH
    )

    return robot


def loadG1(locked_waist: bool) -> pin.RobotWrapper:
    if locked_waist:
        urdf_path = G1_LOCKED_WAIST_DESCRIPTION_URDF_PATH
        srdf_path = G1_LOCKED_WAIST_DESCRIPTION_URDF_PATH
    else:
        urdf_path = G1_UNLOCKED_WAIST_DESCRIPTION_URDF_PATH
        srdf_path = G1_UNLOCKED_WAIST_DESCRIPTION_URDF_PATH

    robot = pin.RobotWrapper.BuildFromURDF(
        urdf_path, [G1_DESCRIPTION_PACKAGE_DIR], pin.JointModelFreeFlyer()
    )

    # Reference configurations
    pin.loadReferenceConfigurations(robot.model, srdf_path)

    # Collision pairs
    robot.collision_model.removeAllCollisionPairs()
    robot.collision_model.addAllCollisionPairs()
    pin.removeCollisionPairs(robot.model, robot.collision_model, srdf_path)

    return robot
