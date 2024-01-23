class QuizBrain:

    def __init__(self, q_list):
        self.number = 0
        self.score = 0
        self.list = q_list

    def still_has_questions(self):
        return self.number < len(self.list)

    def next_question(self):
        current_question = self.list[self.number]
        self.number += 1
        user_answer = input(f"Q.{self.number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.number}")
