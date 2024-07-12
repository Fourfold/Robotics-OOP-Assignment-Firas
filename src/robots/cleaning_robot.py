from .base_robot import *
from .enums import CleaningTool

class CleaningRobot(Robot):
    """
    The cleaning robot implements the base robot class.
    The cleaning robot has a cleaning tool and can use it to clean the floor.
    The count static variable is used to keep track of the number of cleaning robots.
    """

    count = 0

    def __init__(self, name: str, battery_level: int, status: Status, cleaning_tool: CleaningTool):

        Robot.__init__(self, name, battery_level, status)

        self.cleaning_tool = cleaning_tool

        CleaningRobot.count += 1
    
    def work(self) -> None:
        """
        Make the robot clean the floor. Cleaning consumes 20% of the battery level.
        If the robot has less than 20% battery, it cannot work.
        The robot's work depends on the cleaning tool it has.
        """
        if (self.battery_level < 20):
            print(f"Robot {self.name} is unable to clean. Not enough battery.")
        else:
            Robot.work(self)
            if (self.cleaning_tool == CleaningTool.BROOM):
                print(f"Robot {self.name} has started brooming the floor...")
            elif (self.cleaning_tool == CleaningTool.MOP):
                print(f"Robot {self.name} has started mopping the floor...")
            elif (self.cleaning_tool == CleaningTool.VACUUM):
                print(f"Robot {self.name} has started vacuuming the floor...")
            for _ in range(20):
                sleep(0.05)
                self.battery_level -= 1
            print(f"Robot {self.name} has finished cleaning.")
            self.status = Status.IDLE
        print()
    
    def setCleaningTool(self, cleaning_tool: CleaningTool) -> None:
        """
        Change the cleaning tool of the robot. Changing the tool consumes 5% of the battery level.
        If the robot has less than 5% battery, it cannot change its tool.
        """
        if (self.cleaning_tool == cleaning_tool):
            print(f"Robot {self.name} already has a {cleaning_tool}.")
        elif (self.battery_level < 5):
            print(f"Robot {self.name} cannot change its cleaning tool. Not enough battery.")
        else:
            self.status = Status.BUSY
            print(f"Robot {self.name} is changing its cleaning tool from {self.cleaning_tool.name.lower()} to {cleaning_tool.name.lower()}...")
            sleep(1)
            self.battery_level -= 5
            self.cleaning_tool = cleaning_tool
            print(f"Robot {self.name} has finished changing its cleaning tool to {self.cleaning_tool.name.lower()}.")
            self.status = Status.IDLE
        print()

    def reportCleaningTool(self) -> CleaningTool:
        """
        Print the current tool equipped to the robot.
        """
        print(f"Robot {self.name} is using the {self.cleaning_tool.name.lower()} cleaning tool.")
        print()
        return self.cleaning_tool
    
    def getCleaningTool(self) -> CleaningTool:
        return self.cleaning_tool
