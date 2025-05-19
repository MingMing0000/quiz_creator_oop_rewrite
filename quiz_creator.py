# 

class QuizCreator:
    def __init__(self):
        self.quiz_items = []

    def ask_question(self):
        question = input("Input your question: ")
        self.quiz_items.append({"question" : question,})

    def ask_choices(self):
        print("Input the choices")
        choice_a = input("Input choice A: ")
        choice_b = input("Input choice B: ")
        choice_c = input("Input choice C: ")
        choice_d = input("Input choice D: ")
        self.quiz_items.append({"choices" : [choice_a, choice_b, choice_c, choice_d]})
    
    def ask_answer(self):
        answer = input("Input the correct answer from the choices (A, B, C, D): ")
        self.quiz_items.append({"answer" : answer})

    def save_quiz(self):
        quiz_name = input('Enter the file name of the quiz: ')
        quiz_name += '.txt'
        print("Saving quiz...")
        with open(quiz_name, 'a') as file:
            for question in self.quiz_items[0]:
                file.write(f"Question: {question['question']}\n")
            for choice in self.quiz_items[1]:
                file.write(f"a) {choice['choices'][0]}\n")
                file.write(f"b) {choice['choices'][1]}\n")
                file.write(f"c) {choice['choices'][2]}\n")
                file.write(f"d) {choice['choices'][3]}\n")
            for answer in self.quiz_items[2]:
                file.write(f"Answer: {answer['answer']}\n")
                file.write('\n')
        print(f'\n---Your quiz has been saved as {quiz_name}.---\n')