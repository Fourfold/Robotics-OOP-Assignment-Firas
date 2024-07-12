from .base_robot import Status
from .cooking_robot import *
from .cleaning_robot import *
from .enums import CookingSkill

class MaintenanceRobot(CookingRobot, CleaningRobot):
    count = 0
    def __init__(self, name: str, battery_level: int, status: Status, cooking_skill: CookingSkill, cleaning_tool: CleaningTool):
        CookingRobot.__init__(self, name, battery_level, status, cooking_skill)
        CleaningRobot.__init__(self, name, battery_level, status, cleaning_tool)
        Robot.count -= 1
        MaintenanceRobot.count += 1
    
    def work(self):
        CleaningRobot.work(self)
        CookingRobot.work(self)
    
    def multiTask(self):
        self.work()