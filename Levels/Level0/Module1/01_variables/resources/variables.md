# Variables

A variable is a placeholder for information. Unlike some other programming languages, they are very simple to create in Python because you do not need to know what type of data you are storing.

Give the variable a name (any name works as long as it starts with a letter) and then use `=` to give it a value.

## Examples:
```python
dogsName = "rufus"
myAge = 19
userId = input("Enter your ID Number: ")
```

Once a variable has been given a value, that value can be used in later parts of the program.

## Examples:
```python
print("My dog's name is " + dogsName)
yearOfBirth = 2020 - age
check_database_for_id(userId)
```

Sometimes, however, you do need to know what type of data you are holding. Look at the following example and guess what the output will be.

```python
num1 = input("Enter a number")
num2 = input("Enter another number")
sum = num1 + num2
print("The sum is: " + sum)
```

If the input is 5 for num1 and 10 for num2, the output would be 510 instead of 15. So in this case you would need to convert num1 and num2 into an integer using the `int()` function.

```python
num1 = input("Enter a number")
num2 = input("Enter another number")
sum = int(num1) + int(num2)
print("The sum is: " + sum)
```

The opposite is also true. The following example will cause an error because you cannot combine integer data with string data

```python
val = 15
print("The value is " + val)
```

To make this work, val must be converted to a string using the `str()` function.

```python
val = 15
print("The value is " + str(val))
```

