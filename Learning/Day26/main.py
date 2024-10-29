# Exercitiul 1

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55,]

# squared_numbers = [numbers **2 for numbers in numbers]

# print(squared_numbers)

# Exercitiul 2

# numbers = [1 ,1 ,2 ,3 ,5 ,8 ,13 ,21 ,34 ,55]

# result = [numbers for numbers in numbers if numbers % 2 == 0]

# print(result)


# Exercitiul 3

# with open("D:\Python\Git-Repo\Python\Learning\Day26/file1.txt", "r") as file1:
#     file1_content = file1.readlines()
    
# with open("D:\Python\Git-Repo\Python\Learning\Day26/file2.txt", "r") as file2:
#     file2_content = file2.readlines()
    
    
    
# result = [int(number) for number in file1_content if number in file2_content]
# print(result)

# Exercitiul 4

# names = ["Alex", "John", "Mary", "Steve", "John", "Steve"]

# import random

# students_score = {student: random.randint(1, 100) for student in names}

# passed_students = {student: score for (student, score) in students_score.items() if score >= 50}

# print(students_score)
# print(passed_students)

# Exercitiul 5

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# result = {word: len(word) for word in sentence.split()}

# print(result)

# Exercitiul 6

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }

# weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}

# print(weather_f)

# Exercitiul 7

student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)
    
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through a data frame

# for (key,value) in student_data_frame.items():
#     print(value)

#Loop through rows of a data frame
for(index,row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)