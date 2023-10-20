class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_continue(self):
        if self.question_number < len(self.question_list):
            QuizBrain.next_question(self)
        else:
            print(f"You completed the quiz! Your final score is {self.score}/{len(self.question_list)}.")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        question = input(f"Q.{self.question_number} {current_question.text} (True/False)?: ")

        if question == current_question.answer:
            self.score += 1
            print(f"You got it right!\nThe correct answer was: {current_question.answer}. Your score is {self.score}")
        elif question != current_question.answer:
            print(f"That was incorrect.\nThe correct answer was: {current_question.answer}. "
                  f"Your score is {self.score}.")

        QuizBrain.still_continue(self)
