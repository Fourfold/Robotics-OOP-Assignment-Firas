from src import *

class TestMaintenanceRobot:

    def testBattery(self):
        """
        Test if the battery level input handling is valid.
        """
        robot1 = MaintenanceRobot("TestBob001", -50, Status.IDLE, CookingSkill.BEGINNER, CleaningTool.BROOM)
        assert robot1.getBatteryLevel() >= 0 and robot1.getBatteryLevel() <= 100
    
    def testCharge(self):
        """
        Test if the charging works well.
        """
        robot1 = MaintenanceRobot("TestBob001", 0, Status.IDLE, CookingSkill.BEGINNER, CleaningTool.BROOM)
        robot1.charge()
        assert robot1.getBatteryLevel() == 100
    
    def testUpgradeCookingSkill(self):
        """
        Test the ability of the maintenance robot to upgrade its cooking skill.
        """
        testSuccessful = True
        robot1 = MaintenanceRobot("TestBob001", 100, Status.IDLE, CookingSkill.BEGINNER, CleaningTool.BROOM)
        robot1.upgradeCookingSkill()
        testSuccessful = testSuccessful and robot1.cooking_skill == CookingSkill.INTERMEDIATE
        robot1.upgradeCookingSkill()
        testSuccessful = testSuccessful and robot1.cooking_skill == CookingSkill.EXPERT
        assert testSuccessful
    
    def testChangeCleaningTool(self):
        """
        Test the ability of the maintenance robot to change its cleaning tool.
        """
        testSuccessful = True
        robot1 = MaintenanceRobot("TestBob001", 100, Status.IDLE, CookingSkill.BEGINNER, CleaningTool.BROOM)
        testSuccessful = testSuccessful and robot1.cleaning_tool == CleaningTool.BROOM
        robot1.setCleaningTool(CleaningTool.MOP)
        testSuccessful = testSuccessful and robot1.cleaning_tool == CleaningTool.MOP
        robot1.setCleaningTool(CleaningTool.VACUUM)
        testSuccessful = testSuccessful and robot1.cleaning_tool == CleaningTool.VACUUM
        assert testSuccessful

