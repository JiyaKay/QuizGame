from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_text = q["question"]
    question_ans = q["correct_answer"]
    question = Question(question_text, question_ans)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

quiz.next_question()

