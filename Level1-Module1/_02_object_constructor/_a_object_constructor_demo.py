"""
Demonstration of object constructors
"""

# Classes can have variables that "belong" to an object created from the
# class. These variables can only be used when an object is created from
# the class. For example:
student_name = "Kevin"

class Student:
    def __init__(self, name_input):
        self.name = name_input

# * The variable 'student_name' can be used anywhere in the file
# * The variable 'name' within the class Student can only be used outside the
#   class if an object of Student is created
print(student_name)         # No error. Prints Kevin
# print(name)               # ERROR, name variable not defined outside of class
student_1 = Student("Javier")
print(student_1.name)       # No error. Prints Javier

# The name variable in the class is called a member variable. The best place
# for Member variables to be created are in a special function called the
# constructor, __init__(self):
#   def __init__(self):
#       self.member_var = 0     # create member variable 'member_var'

# Member variables always begin with 'self.' so the computer can tell the
# difference between member and non-member variables. The constructor
# is called automatically when a new object of the class is created
# (constructed). For example:
class TestConstructor:
    def __init__(self):
        print('A new TestConstructor object was created!')

obj_1 = TestConstructor()   # Prints message in the constructor ("A new...")
obj_2 = TestConstructor()   # Prints message in the constructor ("A new...")

# A class's constructor can have input variables just like a function. If the
# constructor has input variables with no default values, the same number of
# inputs must also be used when an object is created. For example:
class TestConstructor2:
    def __init__(self, input1, input2):
        local_variable = input1
        self.member_variable = input2

# obj_3 = TestConstructor2()    # ERROR, constructor requires 2 inputs
obj_4 = TestConstructor2(1, 2)  # No error

# print(obj_4.local_variable)   # ERROR, local_variable is not a member variable
                                # because it isn't created with 'self.'
print(obj_4.member_variable)    # No Error, prints 2
