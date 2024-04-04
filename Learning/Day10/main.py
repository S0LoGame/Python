#Exercitiul 1
#Functions with Outputs

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"

# print(format_name("anCa", "iarINa"))

#Exercitiul 2
#Function for length of string
# def string_length(text):
#     number_of_characters = 0
#     for character in text:
#         number_of_characters += 1
#     return number_of_characters

# print(string_length("Hello"))

#Exercitiul 3

# def leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def days_in_month(year, month):
#     if month > 12 or month < 1:
#         return "Invalid month"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if leap_year(year) and month == 2:
#         return 29
#     return month_days[month - 1]

# year=int(input("Enter a year: "))
# month=int(input("Enter a month: "))
# days=days_in_month(year, month)
# print(days)

#Exercitiul 4
#Calculator
import os

#Add
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

#Power
def poww(n1, n2):
    return n1 ** n2 

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
    "^": poww
}

def calculator():
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick another operation: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        second_answer=calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {second_answer}")
        
        if input(f"Type 'y' to continue calculating with {second_answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = second_answer
        else:
            should_continue = False
            calculator()
            
calculator()
