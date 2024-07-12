from enum import Enum

class Status(Enum):
    """
    Enum which specifies the status of the robot.
    """
    IDLE = 1
    WORKING = 2
    CHARGING = 3
    BUSY = 4
    FAULTY = 5

class CookingSkill(Enum):
    """
    Enum which specifies the cooking skill of the robot.
    """
    BEGINNER = 1
    INTERMEDIATE = 2
    EXPERT = 3

class CleaningTool(Enum):
    """
    Enum which specifies the cleaning tool of the robot.
    """
    VACUUM = 1
    MOP = 2
    BROOM = 3

class Error(Enum):
    """
    Enum which specifies the error returned from a self diagnose.
    """
    BATTERY = 1
    MEMORY = 2
    UNKNOWN = 3