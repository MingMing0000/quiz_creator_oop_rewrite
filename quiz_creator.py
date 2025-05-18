# 

class QuizCreator:
    def __init__(self):
        pass

    def ask_question(self):
        question = input("Input your question: ")

    def ask_choices(self):
        print("Input the choices")
        choice_a = input("Input choice A: ")
        choice_b = input("Input choice B: ")
        choice_c = input("Input choice C: ")
        choice_d = input("Input choice D: ")
    
    def ask_answer(self):
        answer = input("Input the correct answer from the choices (A, B, C, D)")

    def save_quiz(self):
        print("Saving quiz...")
        with open(quiz_name, 'a') as file:
            for quiz in quiz_list:
                file.write(f"Question: {quiz['question']}\n")
                file.write(f"a) {quiz['choices'][0]}\n")
                file.write(f"b) {quiz['choices'][1]}\n")
                file.write(f"c) {quiz['choices'][2]}\n")
                file.write(f"d) {quiz['choices'][3]}\n")
                file.write(f"Answer: {quiz['answer']}\n")
                file.write('\n')
        print(f'\n---Your quiz has been saved as {quiz_name}.---\n')