from questions import Questions , Answers , question_number
import random

question_data = []

for i in range(question_number-1):
    question_data.append({"text" : Questions[i] , "answer" : Answers[i]})
random.shuffle(question_data)
