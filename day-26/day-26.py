# # Loop
# numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n+1
#     new_list.append(add_1)
# print(new_list)
#
# # List Comprehension
# new_list = [n+1 for n in numbers]
# print(new_list)
#
# # sting
# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)
#
# # range
# new_list = [i*2 for i in range(1,5)]
# print(new_list)
#
# # Conditional List Comprehension
# names = ['Alex', 'Beth', 'Caroline', 'Eleanor', 'Freddie']
# new_names = [name.upper() for name in names if len(name)>4]
# print(new_names)
#
# # 코딩연습 제곱수
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number**2 for number in numbers]
# print(squared_numbers)
#
# # 코딩연습 짝수 필터링
# result = [number for number in numbers if number % 2==0]
# print(result)

# 코딩연습 겹치는 데이터
# with open("file1.txt") as file1:
#     num_1 = file1.readlines()
#
# with open("file2.txt") as file2:
#     num_2 = file2.readlines()
#
# result = [int(num) for num in num_1 if num in num_2]
# print(result)

# Dictionary Comprehension
# import random
# names = ['Alex', 'Beth', 'Caroline', 'Eleanor', 'Freddie']
# students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)
#
# # Conditional Dictionary Comprehension
# passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)
#
# # coding exercise1
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {letter:len(letter) for (letter) in sentence.split(sep = " ")}
# print(result)
#
# # coding exercise2
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day:temp*9/5+32 for (day,temp) in weather_c.items()}
# print(weather_f)

student_dict = {
    "student" : ["Angela","James","Lily"],
    "score" : [56,76,98]
}

# Looping through dictionaries:
#for (key,value) in student_dict.items():
    #print(value)

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)
#
# Loop through a data frame
# for (key,value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)