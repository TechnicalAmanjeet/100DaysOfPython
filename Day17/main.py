from question_model import QuestionModel
from   data import question_data
from quiz_brain import QuizBrain


quiz_brain = QuizBrain()

for i in range(10):
    quiz_brain.start_quiz()

print(f"User Finel Score : {quiz_brain.right_answer}/{quiz_brain.question_no}.")
print("""\n**** Thank You so much for playing this game ****""")
