from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    age = simpledialog.askinteger(None, 'How old are you?')

    for i in range(age):
        print("In " + str(2020-i) + ", I was " + str(age-i) + " years old.")

    window.mainloop()