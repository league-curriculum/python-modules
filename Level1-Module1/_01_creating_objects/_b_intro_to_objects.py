"""
Creating objects from classes
"""
import unittest


class Car:
    def __init__(self):
        self.amount_of_gasoline = 0
        self.miles_driven = 0
        print('Creating a Car Object')

    def add_gasoline(self):
        print('Refilling gasoline')
        self.amount_of_gasoline = 100

    def drive(self, miles):
        if self.amount_of_gasoline > miles:
            self.amount_of_gasoline -= miles
            self.miles_driven = miles
            print('Driving ' + str(miles) + ' miles')
        else:
            print("Can't drive! Fill with gasoline before driving.")

# ================== DO NOT MODIFY THE CODE ABOVE ============================


# TODO  1) Create a Car Object in the function below
#       2) Drive the car 50 miles
#       3) return the Car Object from the test_drive() function
def test_drive():

    # Replace None with your car Object
    return None


class CreatingObjectsTests(unittest.TestCase):

    def test_1(self):
        self.assertTrue(test_drive().miles_driven == 50)


if __name__ == '__main__':
    unittest.main()
