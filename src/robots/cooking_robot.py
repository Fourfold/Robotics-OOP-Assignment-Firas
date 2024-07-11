from robots.base_robot import *
from robots.enums import CookingSkill

class CookingRobot(Robot):
    def __init__(self, name: str, battery_level: int, status: Status, cooking_skill: CookingSkill):
        super().__init__(name, battery_level, status)
        self.cooking_skill = cooking_skill
    
    def work(self) -> None:
        if (self.battery_level < 30):
            print(f"Robot {self.name} is unable to cook. Not enough battery.")
        else:
            super().work()
            print(f"Robot {self.name} has started cooking...")
            for _ in range(30):
                sleep(0.1)
                self.battery_level -= 1
            print(f"Robot {self.name} has finished cooking.")
            self.status = Status.IDLE
        print("\n")