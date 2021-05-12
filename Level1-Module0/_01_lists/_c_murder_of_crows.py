"""
Find the crow that ate the diamond!
"""
import random


def find_the_diamond(the_murder=None):
    pass
    # TODO 1) One of the Crows has eaten the diamond. You need to search
    #  through the stomach of each Crow, then print the name of the
    #  guilty Crow. The input parameter contains the list of Crow objects.

    # TODO 2) How many innocent crows had to die before the diamond was found?
    #  For example, if you had to look through the stomachs of 3 crows to find
    #  the diamond, then 2 innocent crows died.

# ======================= DO NOT EDIT THE CODE BELOW =========================

class Crow:
    def __init__(self, name):
        self.name = name
        self.stomach_contents = list()
        self.fill_crow_stomach()

    def fill_crow_stomach(self):
        for i in range(10):
            self.stomach_contents.append(self.get_random_crow_food())

    def get_random_crow_food(self):
        randomness = random.randint(0, 3)
        if randomness == 0:
            return "carrion"
        elif randomness == 1:
            return "snail"
        elif randomness == 2:
            return "acorn"
        elif randomness == 3:
            return "spider"
        else:
            return "grub"


def initialize_crows():
    crows = list()
    crows.append(Crow("Rok"))
    crows.append(Crow("Merle"))
    crows.append(Crow("Poe"))
    crows.append(Crow("Grenwyn"))
    crows.append(Crow("Crawford"))

    # Hide the diamond
    rand_crow = crows[random.randint(0, len(crows) - 1)]
    rand_crow.stomach_contents.append("diamond")

    return crows


if __name__ == '__main__':
    murder_of_crows = initialize_crows()
    find_the_diamond(murder_of_crows)
