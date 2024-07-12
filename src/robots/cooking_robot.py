from .base_robot import *
from .enums import CookingSkill

class CookingRobot(Robot):
    """
    The cooking robot implements the base robot class.
    The cooking robot has a cooking skill which affects the quality of the cooked food.
    The count static variable is used to keep track of the number of cooking robots.
    """

    count = 0

    def __init__(self, name: str, battery_level: int, status: Status, cooking_skill: CookingSkill):

        Robot.__init__(self, name, battery_level, status)

        self.cooking_skill = cooking_skill

        CookingRobot.count += 1
    
    def work(self) -> None:
        """
        Make the robot cook a dish. Cleaning consumes 30% of the battery level.
        If the robot has less than 30% battery, it cannot work.
        The quality of the cooked dish depends on the cooking skill of the robot.
        """
        if (self.battery_level < 30):
            print(f"Robot {self.name} is unable to cook. Not enough battery.")
        else:
            Robot.work(self)
            print(f"Robot {self.name} has started cooking...")
            for _ in range(30):
                sleep(0.05)
                self.battery_level -= 1
            print(f"Robot {self.name} has finished cooking.", end=" ")
            if (self.cooking_skill == CookingSkill.BEGINNER):
                print(f"The dish smells ok.")
            elif (self.cooking_skill == CookingSkill.INTERMEDIATE):
                print(f"The dish smells good.")
            elif (self.cooking_skill == CookingSkill.EXPERT):
                print(f"The dish smells amazing.")
            self.status = Status.IDLE
        print()
    
    def upgradeCookingSkill(self) -> None:
        """
        Upgrade the cooking skill of the robot. Upgrading the cooking skill consumes 40% of the battery level.
        If the robot has less than 40% battery, it cannot upgrade its skill.
        """
        if (self.cooking_skill == CookingSkill.EXPERT):
            print(f"Robot {self.name} is already {self.cooking_skill.name.lower()} at cooking.")
        elif (self.battery_level < 40):
            print(f"Robot {self.name} cannot upgrade its cooking skill. Not enough battery.")
        else:
            self.status = Status.BUSY
            print(f"Robot {self.name} is upgrading its cooking skill... Current cooking skill: {self.cooking_skill.name.lower()}")
            sleep(1)
            self.battery_level -= 40
            self.cooking_skill = [CookingSkill.BEGINNER, CookingSkill.INTERMEDIATE, CookingSkill.EXPERT][self.cooking_skill.value]
            print(f"Robot {self.name} has finished upgrading its cooking skill... Current cooking skill: {self.cooking_skill.name.lower()}")
            self.status = Status.IDLE
        print()
    
    def reportCookingSkill(self) -> CookingSkill:
        """
        Print the current cooking skill of the robot.
        """
        print(f"Robot {self.name} is {self.cooking_skill.name.lower()} at cooking.")
        print()
        return self.cooking_skill
    
    def getCookingSkill(self) -> CookingSkill:
        return self.cooking_skill