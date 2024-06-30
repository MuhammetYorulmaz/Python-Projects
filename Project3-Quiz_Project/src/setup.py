class QuizSetup:

    def __init__(self, dict_of_categories):
        self.categories = dict_of_categories
        self.category = None
        self.difficulty = None
        self.amount = None

    def get_quiz_categories(self) -> str:
        control_of_categories = True
        while control_of_categories:
            self.category = input("Which question categories would you like? Just type the code of the categories: ")
            if self.category.isdigit() and int(self.category) in list(self.categories.keys()):
                control_of_categories = False
            else:
                print('You have to choose categories like 1,2,3....')
        return self.category

    def get_difficulty_level(self) -> str:
        difficulty_of_questions = ['any', 'easy', 'medium', 'hard']
        control_of_difficulties = True
        while control_of_difficulties:
            self.difficulty = input(f"Please select the difficulty level of the questions "
                                    f"{'/'.join(difficulty_of_questions)}:").lower()
            if self.difficulty in difficulty_of_questions:
                control_of_difficulties = False
            else:
                print(f"You can only select these difficulty types -> {'/'.join(difficulty_of_questions)}: ")
        return self.difficulty

    def get_amount_of_questions(self) -> str:
        control_of_amount_questions = True
        while control_of_amount_questions:
            self.amount = input("How many questions do you want? You can take max 50 questions!: ").strip()

            if self.amount.isdigit() and (1 <= int(self.amount) <= 50):
                control_of_amount_questions = False
            else:
                print("You can answer a maximum of 50 questions: ")
        return self.amount
