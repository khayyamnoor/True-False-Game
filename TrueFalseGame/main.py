from data import question_data


class QuizBrain:
    SCORE = 0

    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(question_data):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True / False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You Got It Right...! ")
            self.score += 1
            print(f"Your Current Score is: {self.score} / {self.question_number}...")
        else:
            print("You Got It Wrong...! ")
            print(f"Your Current Score is: {self.score} / {self.question_number}...")
        print(f"The correct answer was {correct_answer}...")


class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've Completed the Quiz")