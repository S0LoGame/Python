#Exercitiul 1
# num_char = len(input("What is your name? "))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")
#input mereu ia string
#len mereu da numarul de caractere integer, deci num_char mereu este integer

#Execitiul 2
# numar=input("Introdu un numar de doua cifre: ")
# numar1=numar[0]
# numar2=numar[1]
# print(int(numar1)+int(numar2))
#aici a lasat int, fiindca am nevoie de numere pentru a face operatii matematice

#Exercitiul 3
# height = input("Introdu inaltimea in metri: ")
# weight = input("Introdu greutatea in kg: ")
# bmi = int(weight) / float(height) ** 2
# print(int(bmi))

#Exercitiul 4
# age = input("Introdu varsta: ")
# months = int(age) * 12
# weeks = int(age) * 52
# days = int(age) * 365
# months_90years = 90 * 12
# weeks_90years = 90 * 52
# days_90years = 90 * 365
# months_left = months_90years - months
# weeks_left = weeks_90years - weeks
# days_left = days_90years - days
# print(f"You have {months_left} months, {weeks_left} weeks, and {days_left} days left.")

#Exercitiul 5
# print("Welcome to the tip calculator!")
# total_plata = float(input("What was the total bill? $"))
# procent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# persoane = int(input("How many people to split the bill? "))
# total = total_plata + (total_plata * procent / 100)
# total_per_person = round(total / persoane,2)
#total_per_person = str(total_per_person)
#print("Each person should pay: $" + total_per_person)
# print(f"Each person should pay: ${total_per_person}")


#Exercitiul 6
# import math
# ipotenuza = math.sqrt(int(input("Introdu lungimea catetei 1: "))**2 + int(input("Introdu lungimea catetei 2: "))**2)
# print(f"Ipotenuza triunghiului este = {ipotenuza} " )

#Exercitiul 7
# import math
# a=int(input("Introdu a: "))
# b=int(input("Introdu b: "))
# c=int(input("Introdu c: "))
# delta=int(b**2-4*a*c)
# x1=(-b+math.sqrt(delta))/(2*a)
# x2=(-b-math.sqrt(delta))/(2*a)
# print(f"x1 este = {x1} , x2 este = {x2}" )


#Teorie
# nume=str("Salut sunt un string")
# numar=str(1234) #transforma numarul in string "1234", cu asta face concatenari
# numar1=int(numar) #transforma stringul in numar 1234, cu asta face operatii matematice
# print("Salut am " + numar)
# print("Salut am" + numar1) #nu merge, trebuie sa transformam numarul in string
