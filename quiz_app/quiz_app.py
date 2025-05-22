#import libraries needed
import tkinter as tk
from tkinter import filedialog
import random

# Create the class QuizApp
class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz App")
        self.configure(bg="#86cecb")
        self.geometry("640x360")
        #add welcome text
        self.label = tk.Label(self, text="Welcome to the Quiz App!", font="Roboto 20", bg="#86cecb")
        self.label.pack(pady=75)
        #add a button to open the quiz file
        self.open_button = tk.Button(self, text="Open Quiz File", font=("Roboto", 15), fg="white", bg="#e12885", command=self.open_quiz_file)
        self.open_button.pack(pady=10)
        #add a button to exit the app
        self.exit_button = tk.Button(self, text="Exit App", font=("Roboto", 15), fg="white", bg="#e12885", command=self.destroy)
        self.exit_button.pack(pady=10)
        self.questions = []
        

    #create a new window to display the quiz
    def the_quiz(self):
        self.quiz_window = tk.Toplevel(self)
        self.quiz_window.title("Quiz App")
        self.quiz_window.geometry("1280x720")
        self.quiz_window.configure(bg="#86cecb")
        self.quiz_window.resizable(False, False)

        #randomize the order of the questions
        random.shuffle(self.questions)
        
        #move the variables to the quiz window
        self.current_index = 0
        self.question_count = 0
        self.score = 0     

        #add a label for the question
        self.the_question = tk.Label(self.quiz_window, text=self.questions[self.current_index]['question'], font=("Roboto", 30), bg="#86cecb", wraplength=800)
        self.the_question.pack(pady=30)

        #add buttons for the choices
        self.choice_a = tk.Button(self.quiz_window, text=self.questions[self.current_index]["choices"][0], font=("roboto", 25), width=30, fg="white", bg="#e12885", command=lambda: self.check_answer(0))
        self.choice_b = tk.Button(self.quiz_window, text=self.questions[self.current_index]["choices"][1], font=("roboto", 25), width=30, fg="white", bg="#e12885", command=lambda: self.check_answer(1))
        self.choice_c = tk.Button(self.quiz_window, text=self.questions[self.current_index]["choices"][2], font=("roboto", 25), width=30, fg="white", bg="#e12885", command=lambda: self.check_answer(2)) 
        self.choice_d = tk.Button(self.quiz_window, text=self.questions[self.current_index]["choices"][3], font=("roboto", 25), width=30, fg="white", bg="#e12885", command=lambda: self.check_answer(3))
        self.choice_a.pack(pady=10)
        self.choice_b.pack(pady=10)
        self.choice_c.pack(pady=10)
        self.choice_d.pack(pady=10)

        #add a label for feedback when checking answer
        self.feedback_label = tk.Label(self.quiz_window, text="", font=("Roboto", 20), bg="#86cecb")
        self.feedback_label.pack(pady=10)
        #add a label for next question countdown timer
        self.countdown_label = tk.Label(self.quiz_window, text="", font=("Roboto", 20), bg="#86cecb")
        self.countdown_label.pack(pady=10)
        #add a label for score
        self.score_label = tk.Label(self.quiz_window, text="", font=("Roboto", 20), bg="#86cecb")
        self.score_label.pack(pady=10)
        #add button to exit the quiz
        self.exit_button = tk.Button(self.quiz_window, text="Exit", font=("Roboto", 10), fg="white", bg="#e12885", width=10, command=self.quiz_window.destroy)
        self.exit_button.pack(padx=5, pady=5, side=tk.RIGHT)  

    #add method to open the quiz file
    def open_quiz_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        self.read_quiz_file()
    
    #add method to read the quiz file's content
    def read_quiz_file(self):
        with open(self.file_path, 'r', encoding="utf-8") as file:
            quiz_lines = file.readlines()

        #clear the questions list and put the new file's content
        self.questions.clear()
        
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
        self.the_quiz()

    #add method to check the answer
    def check_answer(self, current_index):
        self.correct_answer = self.questions[self.question_count]["answer"]
        if self.questions[self.question_count]['choices'][current_index][0] == self.correct_answer: #first letter of the answer string
            self.feedback_label.config(text="✔️ Correct!", fg="green")
            self.score += 1
        else:
            self.feedback_label.config(text=f"❌ Wrong! The correct answer is: {self.correct_answer}", fg="red")
        self.question_count += 1
        
        if self.question_count < len(self.questions):
            self.countdown_timer(3)  # 3-second delay before next question
        else:
            self.score_label.config(text=f"Quiz finished! Your score is: {self.score}/{len(self.questions)}", fg="purple")
    
    #add method for countdown timer
    def countdown_timer(self, seconds):
        if seconds > 0:
            self.countdown_label.config(text=f"Next question in {seconds}", fg="blue")
            self.after(1000, self.countdown_timer, seconds - 1)  
        else:
            self.move_to_next_question()

    #add method to move to next question
    def move_to_next_question(self):
        if self.question_count < len(self.questions):
            self.feedback_label.config(text="")
            self.countdown_label.config(text="")
            self.the_question.config(text=self.questions[self.question_count]['question'])
            self.choice_a.config(text=self.questions[self.question_count]["choices"][0])
            self.choice_b.config(text=self.questions[self.question_count]["choices"][1])
            self.choice_c.config(text=self.questions[self.question_count]["choices"][2])
            self.choice_d.config(text=self.questions[self.question_count]["choices"][3])