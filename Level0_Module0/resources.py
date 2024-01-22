# True or False questions
import turtle


def true_or_false(question, answer):
    turtle.hideturtle()
    response = turtle.textinput("Logic Quiz", question + "\n(True/False): ")
    if len(response) > 0:
        response = response[0].upper()
        return response == answer[0]
    return response == answer[0]


# Multiple Choice questions
def multiple_choice(question, choices, correct_answer):
    turtle.hideturtle()
    turtle.clear()
    turtle.penup()
    turtle.goto(-400, 300)
    turtle.write(question, font=("Arial", 16, "normal"))
    turtle.penup()

    y_position = 200
    for i, choice in enumerate(choices, start=1):
        turtle.penup()
        turtle.goto(-150, y_position)
        turtle.write(f"{i}. {choice}", font=("Arial", 14, "normal"))
        y_position -= 30
    turtle.goto(-300, -300)

    response = turtle.textinput("Logic Quiz", "Enter the correct number: ")
    if len(response) > 0:
        response = response[0].upper()
        return response == str(correct_answer)
    return response == str(correct_answer)


def display_results(questions, correct_answers):
    turtle.hideturtle()
    turtle.clear()
    turtle.penup()
    turtle.goto(-400, 300)
    turtle.write(f"You got {correct_answers} out of {len(questions)} questions correct!", font=("Arial", 16, "normal"))
    turtle.goto(-200, -200)
    turtle.done()


questions_deductive = {
    "tf0": ("If all cats like fish, and Fluffy is a cat, then Fluffy must like fish.", "True"),
    "tf1": ("If all cookies are sweet, and this pastry is sweet, then it must be a cookie.", "False"),
    "tf2": ("If all cars have wheels, and this bicycle has wheels, then it must be a car.", "False"),
    "mc0": ("If all dogs bark, and Fido is a dog, what can you deduce?", ["Fido can fly.", "Fido can bark.", "Fido is a cat."], 2),
    "mc1": ("If all bananas are fruits, and this is a banana, what can you deduce?", ["It's a vegetable.", "It's a fruit.", "It's a rock."], 2),
    "mc2": ("If all pencils write, and this is a pencil, what can you deduce?", ["It can dance.", "It can write.", "It's a book."], 2),
    "mc3": ("If all flowers bloom in spring, and this flower is blooming, what can you deduce?", ["It's winter.", "It's spring.", "Flowers don't bloom."], 2),
    "mc4": ("If all stars twinkle in the night sky, and you see something twinkling, what can you deduce?", ["It's daytime.", "It's nighttime.", "Stars never twinkle."], 2)
}

# Inductive Logic Quiz Questions
questions_inductive = {
    "tf0": ("If every time it rains, the grass gets wet, then it must be raining when the grass is wet.", "True"),
    "tf1": ("If you've only met friendly dogs, then all dogs must be friendly.", "True"),
    "tf2": ("If every time you wear a lucky hat, good things happen, then the hat must be lucky.", "True"),
    "tf3": ("If all your friends like ice cream, then you must not like ice cream.", "False"),
    "mc0": ("If every time you eat a certain fruit, it tastes sweet, what can you deduce?", ["All fruits are sweet.", "That fruit is sweet.", "You don't like sweet things."], 2),
    "mc1": ("If every time you practice piano, you get better, what can you deduce?", ["You should stop practicing piano.", "Practice doesn't make you better.", "Practice helps you improve."], 3),
    "mc2": ("If every time you study for a test, you get good grades, what can you deduce?", ["Tests are easy.", "Studying helps you get good grades.", "Grades are not related to studying."], 2),
    "mc3": ("If every time it snows, school is canceled, what can you deduce?", ["School is always canceled.", "Snow is the only reason school is canceled.", "You don't like snow."], 2),
    "mc4": ("If every time you visit the park, you see people playing, what can you deduce?", ["Parks are always crowded.", "People like playing in the park.", "Parks are boring."], 2)
}

# # Abductive Logic Quiz Questions
questions_abductive = {
    "tf0": ("If you find an umbrella, it must be raining.", "False"),
    "tf1": ("If you see footprints on the sandy beach, someone must have walked there.", "True"),
    "tf2": ("If the lights are off, someone might be sleeping in the room.", "True"),
    "tf3": ("If you smell cookies baking, there must be cookies in the oven.", "True"),
    "tf4": ("If your friend looks sad, they might have had a bad day.", "True"),
    "mc0": ("If you find a wet umbrella by the door, what can you abduce?", ["It's sunny outside.", "Someone forgot their umbrella.", "It's raining."], 3),
    "mc1": ("If you see a broken vase on the floor, what can you abduce?", ["The vase fell on its own.", "A unicorn knocked it over.", "Someone accidentally broke the vase."], 3),
    "mc2": ("If you find a note saying, 'Gone to the store,' what can you abduce?", ["Nobody is at home.", "Someone is sleeping.", "The store is closed."], 1),
    "mc3": ("If you hear a loud crash in the kitchen, what can you abduce?", ["It's a normal sound.", "Someone dropped something.", "There's a ghost in the kitchen."], 2),
    "mc4": ("If you smell pizza in the house, what can you abduce?", ["There's a pizza restaurant nearby.", "Someone is cooking pizza.", "Your sense of smell is playing tricks."], 2)
}

# Propositional Logic Quiz Questions
questions_propositional = {
    "tf0": ("If it's sunny, then you can play outside.", "True"),
    "tf1": ("If you finish your homework, then you can watch TV.", "True"),
    "tf2": ("If it's bedtime, then you should brush your teeth.", "True"),
    "tf3": ("If you're wearing a jacket, then it must be cold outside.", "True"),
    "tf4": ("If it's raining, then you need an umbrella.", "True"),
    "mc0": ("If it's a school day, what can you propose?", ["You have to stay in bed.", "You need to go to school.", "It's a holiday."], 2),
    "mc1": ("If you're wearing pajamas, what can you propose?", ["You're ready for a party.", "You're going to bed.", "You're going to play outside."], 2),
    "mc2": ("If you're holding a book, what can you propose?", ["You're going to cook.", "You're going to read.", "You're going to sleep."], 2),
    "mc3": ("If it's snowing, what can you propose?", ["It's summer.", "You need sunscreen.", "It's cold outside."], 3),
    "mc4": ("If it's lunchtime, what can you propose?", ["You should take a nap.", "You should eat lunch.", "You should go for a walk."], 2)
}
