# with open("weather_data.csv") as data_file:
#     data = data_file.readlines() #list 형태로 반환
#     print(data)
#
# #csv file을 ','를 기준으로 리스트 형식으로 저장
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file) #data 객체는 반복이 가능함.
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
#
# import pandas as pd
# import numpy as np
# data = pd.read_csv("weather_data.csv")
# print(type(data))
# temperature = data["temp"]
#
# # convert to dictionary
# data_dict = data.to_dict()
# print(data_dict)
#
# # convert to list
# temp_list = data["temp"].to_list()
#
# # calculate mean
# avg_temp = np.mean(temp_list)
# print(avg_temp)
#
# avg_temp_2 = sum(temp_list) / len(temp_list)
# print(avg_temp_2)
#
# avg_temp_3 = data["temp"].mean()
# print(avg_temp_3)
#
# # find max temperature
# max_temp = data["temp"].max()
# print(max_temp)
#
# print(data.condition)
# print(data["condition"])
#
# get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pd.DataFrame(data_dict)
# print(data)
#
# # Convert to CSV files
# data.to_csv("new_data.csv")

import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
black = len(data[data["Primary Fur Color"] == "Black"])
grey = len(data[data["Primary Fur Color"] == "Grey"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinammon"])

data_dict = {
    "Fur Color" : ["Grey","black","cinnamon"],
    "count" : [grey, black, cinnamon]
}
new_Data = pd.DataFrame(data_dict)
new_Data.to_csv("new_data.csv")
