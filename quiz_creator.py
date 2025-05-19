# 

class QuizCreator:
    def __init__(self):
        self.quiz_items = []

    def ask_question(self):
        self.question = input("Input your question: ")

    def ask_choices(self):
        print("Input the choices")
        self.choice_a = input("Input choice A: ")
        self.choice_b = input("Input choice B: ")
        self.choice_c = input("Input choice C: ")
        self.choice_d = input("Input choice D: ")
    
    def ask_answer(self):
        self.answer = input("Input the correct answer from the choices (A, B, C, D): ")

    def add_quiz_item(self):
        self.quiz_items.append({
            'question': self.question,
            'choices': [self.choice_a, self.choice_b, self.choice_c, self.choice_d],
            'answer': self.answer
        })
    
    def save_quiz(self):
        quiz_name = input('Enter the file name of the quiz: ')
        quiz_name += '.txt'
        print("Saving quiz...")
        with open(quiz_name, 'a') as file:

            for quiz in self.quiz_items:
                file.write(f"Question: {quiz['question']}\n")
                file.write(f"A) {quiz['choices'][0]}\n")
                file.write(f"B) {quiz['choices'][1]}\n")
                file.write(f"C) {quiz['choices'][2]}\n")
                file.write(f"D) {quiz['choices'][3]}\n")
                file.write(f"Answer: {quiz['answer']}\n")

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