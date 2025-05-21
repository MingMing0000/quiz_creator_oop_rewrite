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
        self.open_button = tk.Button(self, text="Open Quiz File", font=("Roboto", 15,) fg="white", bg="#e12885")
        self.open_button.pack(pady=10)
        self.questions = []

    #create a new window to display the quiz
    def the_quiz(self):
        self.quiz_window = tk.Toplevel(self)
        self.quiz_window.title("Quiz App")
        self.quiz_window.geometry("1280x720")
        self.quiz_window.configure(bg="#86cecb")
        self.quiz_window.resizable(False, False)

        #add a label for the question
        self.the_question = tk.Label(self.quiz_window, text=self.questions[self]['question'], font=("Roboto", 20), bg="#e12885")

    #add method to open the quiz file
    def open_quiz_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    
    #add method to read the quiz file's content
    def read_quiz_file(self):
        with open(self.file_path, 'r', encoding="utf-8") as file:
            quiz_lines = file.readlines()

        for line in range(0, len(quiz_lines), 7):  # Assuming 7 lines per quiz item
            question = quiz_lines[line].strip().replace('Question: ', '')
            choice_a_text = quiz_lines[line + 1].strip()
            choice_b_text = quiz_lines[line + 2].strip()
            choice_c_text = quiz_lines[line + 3].strip()
            choice_d_text = quiz_lines[line + 4].strip()
            answer = quiz_lines[line + 5].strip().replace('Answer: ', '')

            self.questions.append({
                'question': question,
                'choices': [choice_a_text, choice_b_text, choice_c_text, choice_d_text],
                'answer': answer
            })

    