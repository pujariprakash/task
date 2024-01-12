import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        for i, question in enumerate(self.questions, 1):
            print(f"\nQuestion {i}: {question['question']}")
            self.display_options(question['options'])

            user_answer = self.get_user_input()
            if self.check_answer(user_answer, question['answer']):
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question['answer']}")

        print(f"\nYour final score is {self.score}/{len(self.questions)}")

    def display_options(self, options):
        for letter, option in zip("ABCD", options):
            print(f"{letter}. {option}")
        print()

    def get_user_input(self):
        while True:
            user_input = input("Your answer (A/B/C/D): ").upper()
            if user_input in ("A", "B", "C", "D"):
                return user_input
            else:
                print("Invalid input. Please enter A, B, C, or D.")

    def check_answer(self, user_answer, correct_answer):
        return user_answer == correct_answer


def main():
    questions = [
        {
            "question": "What is the capital of Japan?",
            "options": ["Tokyo", "Beijing", "Seoul", "Bangkok"],
            "answer": "A",
        },
        {
            "question": "Which programming language is this project written in?",
            "options": ["Java", "Python", "C++", "JavaScript"],
            "answer": "B",
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Mars", "Jupiter", "Saturn", "Venus"],
            "answer": "B",
        },
        # Add more questions as needed
    ]

    print("Welcome to the Quiz Game!\n")
    quiz = Quiz(questions)
    quiz.run_quiz()

if __name__ == "__main__":
    main()