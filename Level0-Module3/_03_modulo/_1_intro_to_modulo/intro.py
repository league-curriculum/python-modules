import random

if __name__ == '__main__':
    # TODO:
    #  Modulo really just means "remainder after division".
    #  However, it's probably easier to understand from some examples
    #  -
    #  A common use for modulo is to test if a number is odd or even.
    #  To do this test, you divide the number by 2.
    #  If the remainder is zero, the number is even, but if the remainder
    #  is one, the number is odd.
    #  In code this would look like this:

    for i in range(3):
        number = random.randint(0, 100)
        if number % 2 == 0:
            print(str(number) + " is even")
        else:
            print(str(number) + " is odd")

    # TODO: Another use for modulo could be to track every 20 times a loop
    #  is executed, as follows:
    for i in range(101):
        if i % 20 == 0:
            print("i is: " + str(i) + ", 20 more repeats completed")
