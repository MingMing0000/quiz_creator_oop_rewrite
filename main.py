# quiz creator ui

from quiz_creator import QuizCreator

make_quiz = QuizCreator()
print('Welcome to Quiz Creator\n')

while True:
    print('Menu:')
    print('1. Create a Quiz')
    print('2. Exit')
    choice = input('Choose an option: ')
    if choice == '1':
        print()
        make_quiz.ask_question()
        make_quiz.ask_choices()
        make_quiz.ask_answer()
        while True:
            add_more = input('Do you want to add another question? (y/n): ')
            if add_more.lower() == 'y':
                print()
                make_quiz.ask_question()
                make_quiz.ask_choices()
                make_quiz.ask_answer()
            elif add_more.lower() == 'n':
                save = input('Do you want to save the quiz? (y/n): ')
                if save.lower() == 'y':
                    make_quiz.save_quiz()
                    break
                elif save.lower() == 'n':
                    print('--Quiz not saved.--\n')
                    make_quiz.quiz_items.clear()
                    break
                else:
                    print('Invalid option, please try again.\n')    
            else:
                print('Invalid option, please try again.\n')