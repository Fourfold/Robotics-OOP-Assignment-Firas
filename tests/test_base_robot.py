from src import *

class TestBaseRobot:
    def testAbstractClass(self):
        """
        Test if the base robot class can be instantiated.
        It should not be instantiated because it is an abstract class.
        """
        try:
            robot1 = Robot("TestBob001", -50, Status.IDLE)
            instanceCreated = True
        except:
            instanceCreated = False
        assert not instanceCreated