"""
Adding buttons and text fields to tkinter GUI app
"""
import tkinter as tk
from tkinter import messagebox

# Below is a demo of how to add buttons and text fields to your tkinter app.
# No work needs to be done in this file, but use this as a reference for
# future projects. Additional button options can be found here:
# https://www.tcl.tk/man/tcl8.6/TkCmd/contents.htm


class ButtonsAndTextFields(tk.Tk):
    def __init__(self):
        super().__init__()

        # Add a label
        self.label = tk.Label(self, bg='green', font=('Rockwell', 20, 'normal', 'underline'))
        self.label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.3)

        # Add a button.
        #   What the command= option does:
        #   Specifies what to call when the button is pressed. If a method
        #   (without the parenthesis) is used it will get called when the
        #   button is pressed.
        self.button = tk.Button(self, text='This is a button!', fg='blue',
                                font=('courier new', 16, 'bold'), command=self.on_button_press)
        self.button.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.2)

        # Add a text field that can take input from the user
        self.text_field = tk.Entry(self)
        self.text_field.place(relx=0.1, rely=0.8, relwidth=0.8, height=18)

        # bind(event, handler) says to call the handler (function or method)
        # when an event occurs. The events are predefined by tkinter.
        # common events: https://www.tcl.tk/man/tcl8.6/TkCmd/bind.htm#M7
        #   <KeyPress>      - a keyboard key is pressed
        #   <KeyRelease>    - a keyboard key is released
        #   <ButtonPress>   - a mouse button is pressed
        #   <ButtonRelease> - a mouse button is released
        #   <Enter>         - the mouse has entered the object
        #   <Leave>         - the mouse has left the object
        #   <Motion>        - the mouse has moved within the object
        self.text_field.bind('<KeyPress>', self.on_text_entry)

        # bind() can also be used in conjunction with the command= option
        self.button.bind('<ButtonRelease>', self.on_button_release)

        # bind() used to change background of the label as the mouse enters
        # and leaves the label object
        self.label.bind('<Enter>', self.mouse_enter_label)
        self.label.bind('<Leave>', self.mouse_leave_label)

    def on_button_press(self):
        # Get the text from the text field and store into a variable
        text_in_text_field = self.text_field.get()

        # Update the text in the label
        self.label.configure(text=text_in_text_field)

        messagebox.showinfo(None, 'button pressed!')

    def on_text_entry(self, event):
        print(repr(event))
        print('  keycode ..: ' + str(event.keycode))
        print('  char: ....: ' + event.char)
        print('  keysym ...: ' + str(event.keysym))

    def on_button_release(self, event):
        print(repr(event))
        print('  num ...: ' + str(event.num) + ' (button number)')

    def on_button_press2(self, event):
        print(repr(event))
        print('  num ...: ' + str(event.num) + ' (button number)')

    def mouse_enter_label(self, event):
        print(repr(event))
        print('  x ...: ' + str(event.x))
        print('  y ...: ' + str(event.y))
        self.label.configure(bg='yellow')

    def mouse_leave_label(self, event):
        print(repr(event))
        print('  x ...: ' + str(event.x))
        print('  y ...: ' + str(event.y))
        self.label.configure(bg='green')


if __name__ == '__main__':
    app = ButtonsAndTextFields()
    app.title('Buttons and Text Fields')
    app.geometry('300x300')
    app.mainloop()
