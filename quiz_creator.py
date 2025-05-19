# 

class QuizCreator:
    def __init__(self):
        self.quiz_items = []

    def ask_question(self):
        question = input("Input your question: ")
        question.store_items(question)

    def ask_choices(self):
        print("Input the choices")
        choice_a = input("Input choice A: ")
        choice_b = input("Input choice B: ")
        choice_c = input("Input choice C: ")
        choice_d = input("Input choice D: ")
        choice_a.store_items(choice_a)
        choice_b.store_items(choice_b)
        choice_c.store_items(choice_c)
        choice_d.store_items(choice_d)
    
    def ask_answer(self):
        answer = input("Input the correct answer from the choices (A, B, C, D): ")
        answer.store_items(answer)
        
    
    def store_items(self, question, choice_a, choice_b, choice_c, choice_d, answer):
        self.quiz_items.append({
            "question" : question,
            "choices" : [choice_a, choice_b, choice_c, choice_d],
            "answer" : answer
            })

    def save_quiz(self):
        quiz_name = input('Enter the file name of the quiz: ')
        quiz_name += '.txt'
        print("Saving quiz...")
        with open(quiz_name, 'a') as file:
            for quiz in self.quiz_items:
                file.write(f"Question: {quiz['question']}\n")
                file.write(f"a) {quiz['choices'][0]}\n")
                file.write(f"b) {quiz['choices'][1]}\n")
                file.write(f"c) {quiz['choices'][2]}\n")
                file.write(f"d) {quiz['choices'][3]}\n")
                file.write(f"Answer: {quiz['answer']}\n")
                file.write('\n')
        print(f'\n---Your quiz has been saved as {quiz_name}.---\n')