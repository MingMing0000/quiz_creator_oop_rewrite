#import the class QuizApp
from quiz_app import QuizApp

quiz = QuizApp()
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    quiz.mainloop()