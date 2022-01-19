import random

from data import question_data

class QuestionModel:
    question_set = []
    new_question = []
    question_no = 0

    def __init__(self):
        self.question_set = question_data
        self.new_question = []
        self.question_no = 0

    def get_question(self):
        """Chose a random q. from question dataset and return it back
        iff q_number is greater or equal to len of dataset of q. then it
        return None."""
        if self.question_no <= len(self.question_set):
            while True:
                question = random.choice(self.question_set)
                if not question in self.new_question:
                    self.new_question.append(question)
                    self.question_no += 1
                    return question
        return None

    def check_answer(self):
        """ it checks whether user giving correct answer or not."""
        question_set = self.get_question()
        question = question_set["text"]
        answer = question_set["answer"]

        user_answer = input(f"Q.{self.question_no} {question} ( 'T' or 'F' ) : ").lower()
        if user_answer == 't' or user_answer == 'true':
            user_answer = "True"
        else: user_answer = "False"

        return user_answer == answer


