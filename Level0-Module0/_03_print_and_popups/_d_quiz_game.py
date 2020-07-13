from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    
    # Make a new window variable, window = Tk()
    window = Tk()
    
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0

    response = simpledialog.askstring(None, 'Which is better, Python or Java?')

    if response.lower() == 'python':
        score += 1
        print('Correct! Your score is ' + str(score))
    else:
        score -= 1
        messagebox.showerror(message="WRONG! It's Python of course!")
        
    messagebox.showinfo(message='Your final score is ' + str(score))
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    
    #      // 3.  Use an if statement to check if their answer is correct

    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    questions = ['Which is better, Python or Java?', 'What does OOP stand for?', 'How many days in a non-leap year?']
    answers   = ['python', 'object orientated programming', '365']
    
    score = 0
    
    for question, answer in zip(questions, answers):
        response = simpledialog.askstring(None, question)

        if response.lower() == answer:
            score += 1
            print('Correct! Your score is ' + str(score))
        else:
            score -= 1
            messagebox.showerror(message="WRONG! It's " + answer + " of course!")
    
    messagebox.showinfo(message='Your final score is ' + str(score))
    
    # Run the window's .mainloop() method
    window.mainloop()