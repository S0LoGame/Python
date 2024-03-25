#Exercitiul 1
# import random

# numar_random = random.randint(1, 10)
# print(numar_random)

# random_float= random.random()
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

#Exercitiul 2
# import random

# moneda=random.randint(0,1)
# if moneda==1:
#     print("Heads")
# else:
#     print("Tails")

#Exercitiul 3
# import random

# nume=input("Spune-mi numele participantilor la masa. ")
# nume_lista=nume.split(", ")
# nume_print=nume_lista[random.randint(0, len(nume_lista)-1)]
# print(f"{nume_print} va plati nota de plata.")

#Exercitiul 4
# row1=["⬜️", "⬜️", "⬜️"]
# row2=["⬜️", "⬜️", "⬜️"]
# row3=["⬜️", "⬜️", "⬜️"]
# map=[row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position=input("Where do you want to put the treasure? ")
# x=int(position[0])
# y=int(position[1])
# map[y-1][x-1]="X"
# print(f"{row1}\n{row2}\n{row3}")

#Exercitiul 5
# import random


# user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
# computer_choice=random.randint(0, 2)
# if user_choice==0:
#     if computer_choice==0:
#         print("It's a draw.")
#     elif computer_choice==1:
#         print("You lose.")
#     else:
#         print("You win.")
# elif user_choice==1:
#     if computer_choice==0:
#         print("You win.")
#     elif computer_choice==1:
#         print("It's a draw.")
#     else:
#         print("You lose.")
# else:
#     if computer_choice==0:
#         print("You lose.")
#     elif computer_choice==1:
#         print("You win.")
#     else:
#         print("It's a draw.")
# print(f"Computer chose {computer_choice}.")
# print(f"User chose {user_choice}.")


