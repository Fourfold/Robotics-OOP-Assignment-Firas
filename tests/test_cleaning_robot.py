from src import *

class TestCleaningRobot:

    def testBattery(self):
        """
        Test if the battery level input handling is valid.
        """
        robot1 = CleaningRobot("TestBob001", -50, Status.IDLE, CleaningTool.BROOM)
        assert robot1.getBatteryLevel() >= 0 and robot1.getBatteryLevel() <= 100
    
    def testCharge(self):
        """
        Test if the charging works well.
        """
        robot1 = CleaningRobot("TestBob001", 0, Status.IDLE, CleaningTool.BROOM)
        robot1.charge()
        assert robot1.getBatteryLevel() == 100
    
    def testChangeTool(self):
        """
        Test the ability of the cleaning robot to change its cleaning tool.
        """
        testSuccessful = True
        robot1 = CleaningRobot("TestBob001", 100, Status.IDLE, CleaningTool.BROOM)
        testSuccessful = testSuccessful and robot1.cleaning_tool == CleaningTool.BROOM
        robot1.setCleaningTool(CleaningTool.MOP)
        testSuccessful = testSuccessful and robot1.cleaning_tool == CleaningTool.MOP
        robot1.setCleaningTool(CleaningTool.VACUUM)
        testSuccessful = testSuccessful and robot1.cleaning_tool == CleaningTool.VACUUM
        assert testSuccessful

