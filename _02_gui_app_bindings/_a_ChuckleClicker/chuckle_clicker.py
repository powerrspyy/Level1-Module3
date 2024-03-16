"""
 Create an app that tells a joke, then a punchline
"""
import tkinter as tk
import random
from tkinter import messagebox


# Use this function to return a random character
def generate_random_letter():
    return chr(random.randint(0, 25) + ord('a'))


class ChuckleClicker(tk.Tk):
    def __init__(self):
        super().__init__()
        b = tk.Button
        # TODO: Declare and initialize 2 buttons (tk.Button)
        #  one button for the joke and another for the punchline
        self.button1 = b(self, text='Joke', fg='black',
                                font=('courier new', 11, 'bold'), command=self.on_joke)
        self.button1.place(relx=0, rely=0, relwidth=0.5, relheight=1)
        self.button2 = b(self, text='Punchline', fg='black',
                                font=('courier new', 11, 'bold'), command=self.on_punchline())
        self.button2.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
        # TODO: Place the 2 buttons next to each other (see example image)

        # TODO: Call the joke button's bind() method to call the on_joke()
        #  method when a mouse button is pressed
        #  example: self.joke_button.bind('<ButtonPress>', self.on_joke)

        # TODO: Call the joke button's bind() method to call the on_punchline()
        #  method when a mouse button is pressed
        self.button1.bind('<ButtonPress>',self.on_joke)
        self.button2.bind('<ButtonPress>', self.on_punchline)
    def on_joke(self, event = None):
        print('Joke button pressed')
        tk.messagebox.showinfo(None, "Joke Activated")
        # TODO: Write your joke below!

    def on_punchline(self, event = None):
        print('Punchline button pressed')
        tk.messagebox.showinfo(None, "Punchline Activated")
        # TODO: Write a punchline to your joke!


if __name__ == '__main__':
    app = ChuckleClicker()
    app.geometry("1000x1000")
    app.mainloop()
    # TODO: Create a new ChuckleClicker object and set the title and geometry.
    #  Remember to call mainloop() at the end

