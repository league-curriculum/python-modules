"""
 Create a _e_Jeopardy trivia game!
"""
import random
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk


class Jeopardy(tk.Tk):

    def __init__(self, categories):
        super().__init__()

        button_width, button_height, num_buttons = self.setup_buttons(categories)

        # TODO: Create a member variable for the list of categories
        self.categories = categories

        # TODO: Create a member variable for the score/money
        self.score = 0

        for i in range(num_buttons):
            row_num = int(i / len(categories))
            col_num = int(i % len(categories))
            row_y = row_num * button_height
            col_x = col_num * button_width
            category = self.categories[col_num]

            # Create the category header and buttons where
            # row 0 is the category title
            if row_num == 0:

                # TODO: To get the category name, use the categories member variable and column num
                category_title = category.name
                label = tk.Label(self, text=category_title, font=('Arial', 18, 'bold'), relief='solid')

                # TODO: Place the Label using the 'col_x', 'row_y', 'button_width',
                #  and 'button_height' variables
                label.place(x=col_x, y=row_y, width=button_width, height=button_height)

            elif len(category.questions) > row_num - 1:
                value = category.questions[row_num - 1].value

                # TODO: Create a tk.Button with the questions' value on the button
                button = tk.Button(self, text=value, fg='blue', font=('courier new', 24, 'bold'), relief='raised')

                # TODO: Place the Button using the 'col_x', 'row_y', 'button_width',
                #  and 'button_height' variables
                button.place(x=col_x, y=row_y, width=button_width, height=button_height)

                # TODO: Call the button's bind() method so the
                #  on_button_press() method is called when a mouse button is pressed
                #  example: self.joke_button.bind('<ButtonPress>', self.on_button_press)
                button.bind('<ButtonPress>', self.on_button_press)

                # TODO: Add the button to the category's list of buttons
                category.buttons.append(button)

    def on_button_press(self, event):
        button_pressed = event.widget
        print('button ' + repr(button_pressed) + ' clicked!')

        # TODO: Call the ask_question() method with button_pressed as an input
        self.ask_question(button_pressed)

    def ask_question(self, button_pressed):
        for category in self.categories:
            for i, button in enumerate(category.buttons):
                if button == button_pressed:
                    if category.questions[i].has_been_asked is False:
                        category.questions[i].has_been_asked = True
                        question = category.questions[i].question
                        answer = category.questions[i].answer
                        value = category.questions[i].value

                        # TODO: At this point the question corresponding to the button is found
                        #  Use the 'question', 'answer', and 'value' variables to ask the user
                        #  the question and get their response. If their response is correct,
                        #  increase the score member variable by the value. Otherwise, subtract
                        #  value from the score
                        response = simpledialog.askstring(category.name, question)

                        if response.lower() in answer.lower():
                            self.score += value
                            messagebox.showinfo('Score', 'Correct, your score is: ' + str(self.score))
                        else:
                            self.score -= value
                            incorrect_msg = 'Incorrect, the answer is: ' + str(answer) + '\n'
                            incorrect_msg += 'Your score is: ' + str(self.score)
                            messagebox.showinfo('Score', incorrect_msg)

                        button.configure(text='')

                        return

    def setup_buttons(self, categories):
        # Window size needs to be updated immediately here so the
        # window width/height variables can be used below
        self.geometry('800x600')
        self.update_idletasks()

        # Get category with the max num of questions to determine the
        # total number of buttons to create
        questions_per_category = 0
        for category in categories:
            if len(category.questions) > questions_per_category:
                questions_per_category = len(category.questions)

        # +1 for the category title
        num_rows = questions_per_category + 1
        num_buttons = len(categories) * num_rows

        button_width = int(self.winfo_width() / len(categories))
        button_height = int(self.winfo_height() / num_rows)

        return button_width, button_height, num_buttons


class Category:
    def __init__(self, category_name):
        self.name = category_name
        self.questions = list()
        self.buttons = list()

    def add_question(self, question, answer, value):
        new_question = Category.Question(question, answer, value)
        self.questions.append(new_question)

    class Question:
        def __init__(self, question, answer, value):
            self.has_been_asked = False
            self.question = question
            self.answer = answer
            self.value = value


if __name__ == '__main__':
    j_categories = list()

    # TODO: Use the Category class above to create at least 3 question categories
    #  for your _e_Jeopardy game
    category_1 = Category('Video Games')

    # TODO: For each Category, use the add_question method to add a question, answer, and
    #  a value for each question
    category_1.add_question('Which came first: Super Mario Bros or Pac Man?', 'Pac Man', 100)
    category_1.add_question('', '', 200)
    category_1.add_question('', '', 300)

    category_2 = Category('History')
    category_2.add_question('WWI started in what year?', '1914', 100)
    category_2.add_question('Greek philosopher', 'Socrates', 200)
    category_2.add_question('', '', 300)

    category_3 = Category('Science')
    category_3.add_question('1', 'blue', 100)
    category_3.add_question('2', 'blue', 200)
    category_3.add_question('3', 'blue', 300)

    category_4 = Category('Math')
    category_4.add_question('foo', 'bar', 100)
    category_4.add_question('foo', 'bar', 200)
    category_4.add_question('foo', 'bar', 300)

    j_categories.append(category_1)
    j_categories.append(category_2)
    j_categories.append(category_3)
    j_categories.append(category_4)

    game = Jeopardy(j_categories)
    game.title('_e_Jeopardy')
    game.mainloop()
