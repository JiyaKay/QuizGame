class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        question = input(f"Q.{self.question_number + 1} {current_question.text} (True/False)?: ")
        if question == current_question.answer:
            print(f"You got it right!\nThe correct answer was: {current_question.answer}")

            if self.question_number < 11:
                print(f"Your score is {self.question_number + 1}")
                self.question_number += 1
                QuizBrain.next_question(self)
            else:
                print(f"You got all the answers right! Your final score is {self.question_number}")
        else:
            print(f"That was incorrect. Your final score is {self.question_number}.")






