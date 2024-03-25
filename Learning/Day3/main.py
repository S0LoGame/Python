#Exercitiul 1
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height != 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

#Exercitiul 2
# numar=int(input("Introduceti un numar: "))

# if numar % 2 == 0:
#     print("Acest numar este par")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Acest numar este impar")

#Exercitiul 3
# height = float(input("Introduceti inaltimea in metri: "))
# weight = float(input("Introduceti greutatea in kg: "))
# bmi = weight / (height ** 2)
# print("BMI-ul este: ", bmi)
# if bmi < 18.5:
#     print("Subponderal")
# elif bmi < 25:
#     print("Normal")
# elif bmi < 30:
#     print("Supraponderal")
# elif bmi < 35:
#     print("Obezitate I")
# else:
#     print("Obezitate II")

#Exercitiul 4
# year = int(input("Which year do you want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

#Exercitiul 5
# numar=int(input("Introduceti un numar: "))
# bill=0
# if numar % 2 == 0:
#     print("Acest numar este par")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill=5
#         print("Please pay $5.")
#     elif age <= 18:
#         bill=7
#         print("Please pay $7.")
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         bill=12
#         print("Please pay $12.")
    
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill+=3
    
#     print(f"Your final bill is: {bill}")
# else:
#     print("Scuze trebuie sa cresti mai intai!")

#Exercitiul 6
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# bill=0

# if size == "S":
#     bill+=15
#     if add_pepperoni == "Y":
#         bill+=2
# elif size == "M":
#     bill+=20
#     if add_pepperoni == "Y":
#         bill+=3
# elif size == "L":
#     bill+=25
#     if add_pepperoni == "Y":
#         bill+=3

# if extra_cheese == "Y":
#     bill+=1

# print(f"Your final bill is: ${bill}.")

#Exercitiul 7
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# combined_string = name1 + name2
# lower_case_string = combined_string.lower()
# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")
# true = t + r + u + e
# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")
# love = l + o + v + e
# love_score = int(str(true) + str(love))
# if (love_score < 10) or (love_score > 90):
#     print(f"Your love score is {love_score}, you go together like coke and mentos.")
# elif (love_score >= 40) and (love_score <= 50):
#     print(f"Your love score is {love_score}, you are alright together.")
# else:
#     print(f"Your love score is {love_score}.")

#Exercitiul 8
# print("Welcome to the Treasure Island.")
# input1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right' ")
# if input1 == "left":
#     input2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
#     if input2 == "wait":
#         input3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
#         if input3 == "red":
#             print("It's a room full of fire. Game Over.")
#         elif input3 == "yellow":
#             print("You found the treasure! You Win!")
#         elif input3 == "blue":
#             print("You enter a room of beasts. Game Over.")
#         else:
#             print("You chose a door that doesn't exist. Game Over.")
#     else:
#         print("You get attacked by an angry trout. Game Over.")
# else:
#     print("You fell into a hole. Game Over.")
