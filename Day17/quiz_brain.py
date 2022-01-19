import question_model
from question_model import QuestionModel


class QuizBrain():
    right_answer = 0
    question_no = 0
    question_model = QuestionModel()

    def __init__(self):
        print("\nLet's Start Playing Quiz Game! \n")
        self.right_answer = 0


    def start_quiz(self):
        ans = self.question_model.check_answer()
        self.question_no += 1
        if ans:
            self.right_answer += 1

        print(f"\n User_Score : {self.right_answer}/{self.question_no}  \n")

