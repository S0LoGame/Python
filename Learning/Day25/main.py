# Exercitiul 1

# import csv

# with open("d:/Python/Git-Repo/Python/Learning/Day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)


# Exercitiul 2

import pandas

# data=pandas.read_csv("d:/Python/Git-Repo/Python/Learning/Day25/weather_data.csv")
#print(type(data))
#print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(f"Temperata medie este : {sum(temp_list)/len(temp_list)} \n")
# max_temp = data["temp"].max()
# print(f"Temperatura maxima este : {max_temp} \n")

#  Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("d:/Python/Git-Repo/Python/Learning/Day25/Squirrel.csv")

print(data["Primary Fur Color"].value_counts())
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels)
print(red_squirrels)
print(black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}
data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")
