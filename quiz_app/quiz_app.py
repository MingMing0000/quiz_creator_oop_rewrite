#import libraries needed
import tkinter as tk
from tkinter import filedialog

# Create the class QuizApp
class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz App")
        self.configure(bg="#86cecb")
        self.geometry("640x360")
        #add welcome text
        self.label = tk.Label(self, text="Welcome to the Quiz App", font="Roboto 20", bg="#86cecb")
        self.label.pack(pady=10)
        #add a button to open the quiz file
        self.open_button = tk.Button(self, text="Open Quiz File", font=("Roboto", 15, "white"), bg="#e12885")
        self.open_button.pack(pady=10)

    #create a new window to display the quiz
    def the_quiz(self):
        self.quiz_window = tk.Toplevel(self)
        self.quiz_window.title("Quiz App")
        self.quiz_window.geometry("1280x720")
        self.quiz_window.configure(bg="#86cecb")

    #add method to open the quiz file
    def open_quiz_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])