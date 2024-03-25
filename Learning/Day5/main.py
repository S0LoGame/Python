#Exercitiul 1
# fruits = ["Apple" , "Peach", "Pear"]
# for fruit in fruits:
#   print(fruit)
#   print(fruit + " Pie")
# print(fruits)

#Exercitiul 2
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# print(student_heights)
# total_height = 0
# contor=0
# for height in student_heights:
#   total_height += height
#   contor+=1
# media=round(total_height/contor)
# print(f"Media inaltimilor este: {media}")

#Exercitiul 3
# suma=0
# for numar in range(1,101):
#     if numar % 2 ==0:
#         suma+=numar
# print(suma)

#Exercitiul 4
# for numar in range(1,101):
#     if numar % 3 ==0 and numar % 5 ==0:
#         print("FizzBuzz")
#     elif numar % 3 ==0:
#         print("Fizz")
#     elif numar % 5 ==0:
#         print("Buzz")
#     else:
#         print(numar)

#Exercitiul 5
# import random
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
#            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G",
#            "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
#            "Y", "Z"]
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# password=""
# for letter in range(1,nr_letters+1):
#     password+=random.choice(letters)
# for symbol in range(1,nr_symbols+1):
#     password+=random.choice(symbols)
# for numar in range(1,nr_numbers+1):
#     password+=str(random.choice(number))
# print(password)
