import random


class QuizBrain:

    def __init__(self):
        self.score = 0
        self.options = ['A', 'B', 'C', 'D']
        self.all_answers = None
        self.user_answer = None

    def set_options(self, correct_answer: str, incorrect_answers: list) -> dict:
        self.all_answers = incorrect_answers + [correct_answer]
        random.shuffle(self.all_answers)
        answer_mapping = {option: answer for option, answer in zip(self.options, self.all_answers)}
        return answer_mapping

    def get_answer_from_user(self):
        self.user_answer = None
        while self.user_answer not in self.options:
            self.user_answer = input("Enter your answer (A, B, C, D): ").strip().upper()
            if self.user_answer not in self.options:
                print("Invalid input. Please enter one of the options (A, B, C, D).")

    def check_answer(self, answer_mapping: dict, correct_answer: str):
        if answer_mapping.get(self.user_answer) == correct_answer:
            print("Correct!\n")
            self.score += 10
        else:
            print(f"Wrong! Correct answer is: {correct_answer}\n")
