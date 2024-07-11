from robots.base_robot import *
from robots.enums import CleaningTool

class CleaningRobot(Robot):
    def __init__(self, name: str, battery_level: int, status: Status, cleaning_tool: CleaningTool):
        super().__init__(name, battery_level, status)
        self.cleaning_tool = cleaning_tool
    
    def work(self) -> None:
        if (self.battery_level < 20):
            print(f"Robot {self.name} is unable to clean. Not enough battery.")
        else:
            super().work()
            print(f"Robot {self.name} has started cleaning...")
            for _ in range(20):
                sleep(0.1)
                self.battery_level -= 1
            print(f"Robot {self.name} has finished cleaning.")
            self.status = Status.IDLE
        print("\n")
    
    def setCleaningTool(self, cleaning_tool: CleaningTool) -> None:
        if (self.cleaning_tool == cleaning_tool):
            print(f"Robot {self.name} already has a {cleaning_tool}.")
        elif (self.battery_level < 5):
            print(f"Robot {self.name} cannot change its cleaning tool. Not enough battery.")
        else:
            self.status = Status.BUSY
            print(f"Robot {self.name} is changing its cleaning tool from {self.cleaning_tool.name} to {cleaning_tool.name}...")
            sleep(3)
            self.battery_level -= 5
            self.cleaning_tool = cleaning_tool
            print(f"Robot {self.name} has finished changing its cleaning tool to {self.cleaning_tool.name}.")
            self.status = Status.IDLE
        print("\n")

    def getCleaningTool(self) -> Status:
        print(f"Robot {self.name} is using the {self.cleaning_tool} cleaning tool.")
        print("\n")
        return self.cleaning_tool
