"""
Creating objects from classes
"""
import unittest


class Car:
    def __init__(self):
        self._amount_of_gasoline = 0
        self._miles_driven = 0
        print('Creating a Car Object')

    def add_gasoline(self):
        print('Refilling gasoline')
        self._amount_of_gasoline = 100

    def drive(self, miles):
        if self._amount_of_gasoline > miles:
            self._amount_of_gasoline -= miles
            self._miles_driven = miles
            print('Driving ' + str(miles) + ' miles')
        else:
            print("Can't drive! Fill with gasoline before driving.")

# ================== DO NOT MODIFY THE CODE ABOVE ============================


# TODO  1) Create a Car Object in the function below
#       2) Look at the Car class and figure out how to drive the car 50 miles
#       3) return the Car Object from the test_drive() function
def test_drive():

    return None

# ================== DO NOT MODIFY THE CODE BELOW ============================

class CreatingObjectsTests(unittest.TestCase):

    def test_1(self):
        self.assertTrue(test_drive()._miles_driven == 50)


if __name__ == '__main__':
    unittest.main()
