class QuizBrain:
    def __init__(self, question_list):
        self.que_number = 0
        self.score = 0
        self.question_list = question_list

    # TODO: 4. check if it is End of the quiz
    def still_has_questions(self):
        return self.que_number < len(self.question_list)

    def next_question(self):
        current_que = self.question_list[self.que_number]
        self.que_number += 1
        correct_answer = current_que.answer.lower()

        # TODO: 1. asking the question
        user_answer = input(f"Q.{self.que_number}: {current_que.text} (True/False): ").lower()
        self.check_answer(user_answer, correct_answer)

    # TODO: 2. check if the answer is correct
    def check_answer(self, user_answer, correct_answer):

        # TODO: 3. Give the feedback to the user
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is : {self.score}/{self.que_number}.\n")
