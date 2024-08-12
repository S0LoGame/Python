# Exercitiul 1
# from prettytable import PrettyTable
# table = PrettyTable()

# class User:
    
#     def __init__(self,user_id,username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0

#     def follow(self,user):
#         user.followers += 1
#         self.followers += 1

# user_1 = User("001","Marius")
# user_2 = User("002","Andrei")

# user_1.follow(user_2)


# table.add_column("User ID",[user_1.id,user_2.id])
# table.add_column("Username",[user_1.username,user_2.username])
# table.add_column("Followers",[user_1.followers,user_2.followers])
# table.add_column("Following",[user_1.following,user_2.following])


# print(table)


# Exercitiul 2 - True or False

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text,answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")