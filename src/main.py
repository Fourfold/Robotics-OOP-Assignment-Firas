from robots.cooking_robot import *
from robots.cleaning_robot import *

robot1 = CookingRobot("Bob001", 50, Status.IDLE, CookingSkill.INTERMEDIATE)
robot2 = CleaningRobot("Bob002", 40, Status.IDLE, CleaningTool.BROOM)

print("\n")

robot1.report_battery_level()
sleep(0.1)
robot1.work()
sleep(0.1)
robot1.work()
sleep(0.1)
robot1.charge()
sleep(0.1)
robot1.work()
sleep(0.1)

print("----------------------------------------------------------------------\n")

robot2.report_battery_level()
sleep(0.1)
robot2.work()
sleep(0.1)
robot2.work()
sleep(0.1)
robot2.getCleaningTool()
sleep(0.1)
robot2.setCleaningTool(CleaningTool.MOP)
sleep(0.1)
robot2.charge()
sleep(0.1)
robot2.setCleaningTool(CleaningTool.MOP)
sleep(0.1)
robot2.work()
sleep(0.1)

