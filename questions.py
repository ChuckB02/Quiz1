from typing import List
from random import randint


class question:
    def __init__(self, title: str, answers: List[str], correct: int):
        if correct < 0 or correct >= len(answers):
            raise ValueError
        
        self.title = title
        self.answers = answers
        self.correct = correct
    
    def check(self, attempt: int):
        if attempt < 0 or attempt >= len(self.answers):
            raise ValueError

        return attempt == self.correct
    

q1 = question(
    title = "What's the height of the Everest Mountain?",
    answers = [
        "8848.86 m",
        "8912.43 m",
        "9012.11 m",
        "8632.24"
    ],
    correct = 0
)

q2 = question(
    title = "How many countries are located in Europe?",
    answers = [
        "40",
        "32",
        "44",
        "51"
    ],
    correct = 2
)

q3 = question(
    title = "How many billion years ago did the Big Bang happened?",
    answers = [
        "14.12",
        "13.77",
        "12.08",
        "10.57"
    ],
    correct = 1
)

q4 = question(
    title = "What's the capital of Australia?",
    answers = [
        "Camberra",
        "Sidney",
        "Melbourne",
        "Perth"
    ],
    correct = 0
)

q5 = question(
    title = "When did the Berlim wall fall?",
    answers = [
        "1986",
        "1991",
        "1987",
        "1989"
    ],
    correct = 0
)

q6 = question(
    title = "How many liters of blood an average human body has?",
    answers = [
        "7",
        "6",
        "4",
        "5"
    ],
    correct = 0
)

list_of_questions = [q1, q2, q3, q4, q5, q6]

def get_question():
    n = len(list_of_questions)
    if list_of_questions:
        ques = list_of_questions[randint(0, n-1)]
        list_of_questions.remove(ques)
        return ques
    else:
        raise IndexError


