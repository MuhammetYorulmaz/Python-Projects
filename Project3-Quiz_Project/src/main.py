from api import QuizAPI, QuizCategories


def main():
    amount_of_question, type_of_quiz, select_difficulty = None, None, None
    print('\n-----Welcome QUIZ Game-----\n')
    print("Categories of Questions:\n")

    # Bring categories
    quiz_categories = QuizCategories()
    dict_of_categories = quiz_categories.fetch_categories()

    for idx, val in dict_of_categories.items():
        print(f"{idx}: {val}")

    control_of_categories = True
    while control_of_categories:
        type_of_quiz = input("Which question categories would you like? Just type the code of the categories: ")
        if type_of_quiz.isdigit() and int(type_of_quiz) in list(dict_of_categories.keys()):
            control_of_categories = False
        else:
            print('You have to choose categories like 1,2,3....')

    difficulty_of_questions = ['any', 'easy', 'medium', 'hard']
    control_of_difficulties = True
    while control_of_difficulties:
        select_difficulty = input(f"Please select the difficulty level of the questions "
                                  f"{'/'.join(difficulty_of_questions)}:").lower()
        if select_difficulty in difficulty_of_questions:
            control_of_difficulties = False
        else:
            print(f"You can only select these difficulty types -> {'/'.join(difficulty_of_questions)}: ")

    control_of_amount_questions = True
    while control_of_amount_questions:
        amount_of_question = input("How many questions do you want? You can take max 50 questions!: ").strip()

        if amount_of_question.isdigit() and (1 <= int(amount_of_question) <= 50):
            control_of_amount_questions = False
        else:
            print("You can answer a maximum of 50 questions: ")

    # Bring Questions
    questions_class = QuizAPI(amount_of_question, type_of_quiz, select_difficulty)
    questions = questions_class.fetch_quiz()
    print(questions)


if __name__ == '__main__':
    main()
