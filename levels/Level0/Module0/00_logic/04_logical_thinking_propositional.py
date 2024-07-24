"""
Programming Concepts: Logical Thinking Quiz Propositinal Reasoning

!!! DO NOT EDIT ANYTHING IN THIS FILE !!!

Run this file to test your logical thinking skills.

Instructions:
"Welcome to the Propositinal Logical Thinking Quiz! Answer the following questions to test your propositional reasoning skills. For each question, you will be given a statement and a conclusion. You must determine whether the conclusion is true or false based on the statement. You will also be given a statement and a list of possible conclusions. You must determine which conclusion logically follows the statement.
    
    Hint: Each type of logical thinking has a different way of determining whether a conclusion is true or false. Read the instructions carefully to determine which type of logical thinking you should use to answer each question.
    
    Good luck!
"""

# import turtle and resources.py
import resources
true_or_false = resources.true_or_false
multiple_choice = resources.multiple_choice
questions_propositional = resources.questions_propositional
display_results = resources.display_results

# start with 0 correct answers
total_correct = 0

# iterate through questions_propositional dictionary
# for each key, value pair, call the appropriate function
# increment total_correct if the answer is correct
for key, value in questions_propositional.items():
    if key.startswith("tf"):
        if (true_or_false(value[0], value[1])):
            total_correct += 1
    elif key.startswith("mc"):
        if (multiple_choice(value[0], value[1], value[2])):
            total_correct += 1

# call display_results function
display_results(questions_propositional, total_correct)
