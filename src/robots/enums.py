from enum import Enum

class Status(Enum):
    IDLE = 1
    WORKING = 2
    CHARGING = 3
    BUSY = 4

class CookingSkill(Enum):
    BEGINNER = 1
    INTERMEDIATE = 2
    EXPERT = 3

class CleaningTool(Enum):
    VACUUM = 1
    MOP = 2
    BROOM = 3