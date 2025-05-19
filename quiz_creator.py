# 

class QuizCreator:
    def __init__(self):
        self.quiz_items = []
    
    #ask the user for the question, choices, and answer
    def create_quiz(self):
        question = input('Input your question: ')
        print('Input your choices')
        choice_a = input('Input choice a: ')
        choice_b = input('Input choice b: ')
        choice_c = input('Input choice c: ')
        choice_d = input('Input choice d: ')
        answer = input('Input the correct answer from the choices(A,B,C,D): '); print()

        #append the inputs into a list
        self.quiz_items.append({
            'question': question,
            'choices': [choice_a, choice_b, choice_c, choice_d],
            'answer': answer
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
                file.write('\n')
        print(f'\n---Your quiz has been saved as {quiz_name}.---\n')