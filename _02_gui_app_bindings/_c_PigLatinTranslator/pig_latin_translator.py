"""
 Create an app that checks the user's typing skills
"""
import tkinter as tk
from PigLatinConverter import PigLatinConverter

class PigLatinTranslator(tk.Tk):
    def __init__(self):
        super().__init__()

        # TODO: Declare and initialize an Entry (tk.Entry) for the input text
        self.entry = tk.Entry(self, relief = "solid")
        self.entry.place(relx=0, rely = 0.5, relwidth = 0.3, relheight = 0.1)
        # TODO: Declare and initialize a Button (tk.Button) that will translate
        #  the input text to pig latin when pressed
        self.button = tk.Button(self, text='Translate', fg='black',
                                font=('courier new', 20, 'bold'), command=self.on_key_press)
        self.button.place(relx = 0.325, rely = 0.5, relwidth = 0.3, relheight = 0.1)
        # TODO: Declare and initialize an label (tk.Label) for the translated
        #  text
        self.label = tk.Label(self, text = "Output", relief = 'solid')
        self.label.place(relx=0.65, rely=0.5, relwidth = 0.35, relheight = 0.1)
        # TODO: Look at the example image () and place all the
        #  components in the same order

        # TODO: Call the label's bind() method to call the on_key_release()
        #  method when a key is released

    def on_key_press(self):
        self.translated_text = PigLatinConverter.translate(self.entry.get())
        self.label.configure(text = f'{self.translated_text}')

        # TODO: Use the _c_PigLatinTranslator.translate() method to translate
        #  the text in the input entry and set the text in the output entry


if __name__ == '__main__':
    app = PigLatinTranslator()
    app.geometry("1000x1000")
    app.mainloop()
    # TODO: Create a new _c_PigLatinTranslator object and set the title and geometry.
    #  Remember to call mainloop() at the end
