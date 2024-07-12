from src import *

class TestCookingRobot:

    def testBattery(self):
        """
        Test if the battery level input handling is valid.
        """
        robot1 = CookingRobot("TestBob001", -50, Status.IDLE, CookingSkill.BEGINNER)
        assert robot1.getBatteryLevel() >= 0 and robot1.getBatteryLevel() <= 100
    
    def testCharge(self):
        """
        Test if the charging works well.
        """
        robot1 = CookingRobot("TestBob001", 0, Status.IDLE, CookingSkill.BEGINNER)
        robot1.charge()
        assert robot1.getBatteryLevel() == 100
    
    def testUpgradeSkill(self):
        """
        Test the ability of the cooking robot to upgrade its skill.
        """
        testSuccessful = True
        robot1 = CookingRobot("TestBob001", 100, Status.IDLE, CookingSkill.BEGINNER)
        robot1.upgradeCookingSkill()
        testSuccessful = testSuccessful and robot1.cooking_skill == CookingSkill.INTERMEDIATE
        robot1.upgradeCookingSkill()
        testSuccessful = testSuccessful and robot1.cooking_skill == CookingSkill.EXPERT
        assert testSuccessful

