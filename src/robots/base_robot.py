from abc import ABC, abstractmethod
from robots.enums import Status
from time import sleep

class Robot(ABC):

    def __init__(self, name: str, battery_level: int, status: Status):
        self.name = name

        if (battery_level < 0):
            self.battery_level = 0
        elif (battery_level > 100):
            self.battery_level = 100
        else:
            self.battery_level = battery_level
        
        self.status = status
    
    def charge(self) -> None:
        if (self.battery_level == 100):
            print(f"Robot {self.name} is fully charged.")
        else:
            self.status = Status.CHARGING
            print(f"Robot {self.name} has started charging... Current battery level: {self.battery_level}%")
            while self.battery_level < 100:
                sleep(0.1)
                self.battery_level += 1
            self.battery_level = 100
            print(f"Robot {self.name} has finished charging.")
            self.status = Status.IDLE
        print("\n")
    
    @abstractmethod
    def work(self) -> None:
        self.status = Status.WORKING

    def report_status(self) -> Status:
        print(f"Robot {self.name} is {self.status}.")
        return self.status
    
    def report_battery_level(self) -> int:
        print(f"Robot {self.name} has {self.battery_level}% battery level.")
        print("\n")
        return self.battery_level