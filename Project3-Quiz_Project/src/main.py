import time
from setup import QuizSetup
from quiz_brain import QuizBrain
from api import QuizAPI, QuizCategories


def main():
    print('\n-----Welcome QUIZ Game-----\n')
    print("Categories of Questions:\n")

    # Bring categories
    quiz_categories = QuizCategories()
    dict_of_categories = quiz_categories.fetch_categories()
    for idx, val in dict_of_categories.items():
        print(f"{idx}: {val}")

    # Ask about the user's requests
    setup = QuizSetup(dict_of_categories)
    category = setup.get_quiz_categories()
    difficulty = setup.get_difficulty_level()
    amount = setup.get_amount_of_questions()

    # Bring main questions with API
    questions_class = QuizAPI(amount, category, difficulty)
    questions = questions_class.fetch_quiz()

    if questions['response_code'] == 0:
        print('\nYour questions are being prepared!')
        print('-'*50)
        time.sleep(1)

        quiz_brain = QuizBrain()

        for index, question in enumerate(questions['results']):

            question_text = question['question']
            correct_answer = question['correct_answer']
            incorrect_answers = question['incorrect_answers']

            answer_mapping = quiz_brain.set_options(correct_answer, incorrect_answers)

            # Print question and options
            print(f"Q.{index + 1}: {question_text}")
            for option in quiz_brain.options:
                print(f"{option}) {answer_mapping[option].strip()}")

            # Get answer of user
            quiz_brain.get_answer_from_user()

            # Give information about answer
            quiz_brain.check_answer(answer_mapping, correct_answer)

        print("\nYou've completed the quiz")
        print(f"Your total score is: {quiz_brain.score}")

    elif questions['response_code'] == 1:
        print("Could not return results. The API doesn't have enough questions for your query.")


if __name__ == '__main__':
    main()
