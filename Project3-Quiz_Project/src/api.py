import requests


class QuizAPI:

    def __init__(self, amount_of_question, type_of_quiz, select_difficulty):
        self.amount = amount_of_question
        self.category = type_of_quiz
        self.difficulty = select_difficulty

    def fetch_quiz(self) -> dict:
        if self.difficulty != 'any':
            url = (f"https://opentdb.com/api.php?amount={self.amount}&category={int(self.category) + 8}"
                   f"&difficulty={self.difficulty}&type=multiple")
        else:
            url = f"https://opentdb.com/api.php?amount={self.amount}&category={int(self.category) + 8}&type=multiple"

        response = requests.get(url)

        quiz_dict = None
        if response.status_code == 200:
            quiz_dict = response.json()
        else:
            print("Failed to retrieve data from the API. Status code:", response.status_code)

        return quiz_dict


class QuizCategories:

    @staticmethod
    def fetch_categories() -> dict:
        dict_of_categories = {}
        url = 'https://opentdb.com/api_category.php'
        response = requests.get(url)
        if response.status_code == 200:
            quiz_categories = response.json()
            categories_name = [item['name'] for item in quiz_categories['trivia_categories']]
            for i in range(1, len(categories_name) + 1):
                dict_of_categories[i] = categories_name[i - 1]
        else:
            print("Failed to retrieve data from the API. Status code:", response.status_code)
        return dict_of_categories
