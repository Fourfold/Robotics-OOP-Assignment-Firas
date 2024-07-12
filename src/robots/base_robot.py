from abc import ABC, abstractmethod
from time import sleep
from .enums import Status, Error

class Robot(ABC):
    """
    This is the base abstract class of the Robot family.
    Each robot has a name, battery level, and status.
    The count static variable is used to keep track of the total number of robots.
    """

    count = 0

    def __init__(self, name: str, battery_level: int, status: Status):
        
        self.name = name

        if (battery_level < 0):
            self.battery_level = 0
        elif (battery_level > 100):
            self.battery_level = 100
        else:
            self.battery_level = battery_level
        
        self.status = status

        Robot.count += 1
    
    def charge(self) -> None:
        """
        Charge the robot's battery. It takes 50 milliseconds to charge 1% of the battery.
        """
        if (self.battery_level == 100):
            print(f"Robot {self.name} is fully charged.")
        else:
            self.status = Status.CHARGING
            print(f"Robot {self.name} has started charging... Current battery level: {self.battery_level}%")
            while self.battery_level < 100:
                sleep(0.05)
                self.battery_level += 1
            self.battery_level = 100
            print(f"Robot {self.name} has finished charging.")
            self.status = Status.IDLE
        print()
    
    @abstractmethod
    def work(self) -> None:
        """
        Make the robot work. This functions is abstract for the base robot.
        Working consumes battery power, but this is implemented specifically for each robot type.
        """
        self.status = Status.WORKING

    def reportStatus(self) -> Status:
        """
        Print the status of the robot.
        """
        print(f"Robot {self.name} is {self.status}.")
        return self.status
    
    def reportBatteryLevel(self) -> int:
        """
        Print the battery level of the robot.
        """
        print(f"Robot {self.name} has {self.battery_level}% battery level.")
        print()
        return self.battery_level
    
    def getName(self) -> str:
        return self.name
    
    def getBatteryLevel(self) -> int:
        return self.battery_level
    
    def getStatus(self) -> Status:
        return self.status
    
    def selfDiagnose(self) -> list[Error]:
        """
        Self-diagnose the robot, and return a list of errors.
        """
        errorList = []
        if (self.battery_level < 0 or self.battery_level > 100):
            errorList.append(Error.BATTERY)
        if (self.name == ""):
            errorList.append(Error.MEMORY)
        if (self.status == Status.FAULTY):
            errorList.append(Error.UNKNOWN)
        return errorList
