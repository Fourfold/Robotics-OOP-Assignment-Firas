# Robotics-OOP-Assignment-Firas

**This repository contains the assignment for session 4 of the robotics path.**

The project contains a base Robot class which is abstract (child of `ABC`) and cannot be instantiated, and two children classes (Cooking Robot and Cleaning Robot) which extend the Robot base class, each with its unique functionality.
By implementing getters and setters for different attributes of these classes, encapsulation is achieved. In addition, the common class members can be accessed from the base class, achieving polymorphism.

A third Maintenance Robot class extends both the Cleaning and Cookin Robot classes. MRO for this class is achieved by specifying the parent class that the method should be called from.
For example, the `work(self)` and `multitask(self)` methods call both `CookingRobot.work(self)` and `CleaningRobot.work(self)`.
According to the tests I did, if a class extends more than one class, then `super` refers to the first class it extends from. For exxample, for `class C(A,B)`, `super` refers to `A`.

There are value checks for the class attributes. For the **Battery Level**, it is implemented using if-else conditions. For other attributes, Enum entities are created for the **Status**, **Cooking Level**, and **Cleaning Tool**.

The `main.py` script tests the different functionalities of the three robot classes.

---

The project also contains unit tests to test some cases. The tests include battery value checks, abstract class check, cooking level upgrade checks, and cleaning tool change checks.

---

The project is run in a simple Docker container.
