"""
Create a Minion class to make all the MinionTests pass
"""
import unittest


# TODO 1) Run this MinionTest class. Notice the run tab at the bottom says,
#  "Tests failed". This is because the tests do not run successfully. Check
#  the error message is "NameError: name 'Minion' is not defined" at the
#  bottom. This is because there is no Minion class.

# TODO 2) To make these tests pass, you will first need to create a Minion
#  class with the member variables below:
#   name
#   eyes
#   color
#   master


# ======================= DO NOT EDIT THE CODE BELOW =========================

class MinionTest(unittest.TestCase):

    def test_constructor(self):
        stuart = Minion("Stuart", 1, "yellow", "")
        self.assertEquals("Stuart", stuart.name)
        self.assertEquals(1, stuart.eyes)
        self.assertEquals("yellow", stuart.color)

        dave = Minion("Dave", 2, "yellow", "")
        self.assertEquals("Dave", dave.name)
        self.assertEquals(2, dave.eyes)
        self.assertEquals("yellow", dave.color)


if __name__ == '__main__':
    unittest.main()
