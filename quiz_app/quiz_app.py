#import tkinter
import tkinter as tk

# Create the class QuizApp
class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz App")
        self.configure(bg="turquoise")
        self.geometry("640x360")