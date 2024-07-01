# Quiz Project

A simple quiz project using Python, fetching questions from an API and following OOP principles.

## Project Structure

- `src/`: Contains the main source code.
  - `main.py`: The entry point of the application.
  - `setup.py`: Defines the `QuizSetup` class for setting up quiz parameters.
  - `quiz_brain.py`: Defines the `QuizBrain` class for managing quiz logic.
  - `api.py`: Handles fetching questions and categories from an API.
- `requirements.txt`: Lists the dependencies.
- `README.md`: Project overview and setup instructions.

## Setup

1. Clone the repository.
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the quiz:
    ```sh
    python src/main.py
    ```

## Running the Quiz

Simply run `main.py` to start the quiz. The quiz will fetch categories and questions from the Open Trivia Database API and prompt you to answer them.

---
