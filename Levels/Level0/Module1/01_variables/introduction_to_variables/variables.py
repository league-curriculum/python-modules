"""
A variable is a placeholder for information. Unlike some other programming languages, they are very simple to create in Python because you do not need to know what type of data you are storing.

Give the variable a name (any name works as long as it starts with a letter) and then use `=` to give it a value.
"""

## Examples:
dogs_name = "rufus"
my_age = 19
user_id = 1234567890

# Once a variable has been given a value, that value can be used in later parts of the program.

## Examples:

print("My dog's name is " + dogs_name)
year_of_birthBirth = 2024 - my_age
print(year_of_birthBirth)


# Sometimes, however, you do need to know what type of data you are holding. Look at the following example and guess what the output will be.


num1 = input("Enter a number")
num2 = input("Enter another number")
sum = num1 + num2
print("The sum is: " + sum)


# If the input is 5 for num1 and 10 for num2, the output would be 510 instead of 15. So in this case you would need to convert num1 and num2 into an integer using the `int()` function.


num1 = input("Enter a number")
num2 = input("Enter another number")
if num1.isdigit() and num2.isdigit():
    sum = int(num1) + int(num2)
    print(f"The sum is: {sum}")
else:
    print("Please enter a valid number")


# The opposite is also true. The following example will cause an error because you cannot combine integer data with string data.  Delete the # in front of the print and run the code to see the error.


val = 15
# print("The value is " + val)


# To make this work, val must be converted to a string using the `str()` function.

val = 15
print("The value is " + str(val))


# In summary, variables are a way to store information in a program. They can be used to store any type of data and can be used in later parts of the program. They can also be converted to different types of data using the `int()`, `str()`, and `float()` functions.

# Task: Create more variables and print them out. Try to use different types of data and convert them to other types of data.
