from question_model_day_17 import Question
from data_day_17 import question_data

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank[0])
