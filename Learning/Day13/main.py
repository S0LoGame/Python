#Exercitiul 1

#Play Computer
# year=int(input("What's your year of birth?\n")) 
# if year >1980 and year <= 1994:
#     print("You are a Millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")


#Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
    
# mutate([1,2,3,5,8,13])

#Leap Year
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
    

#FizzBuzz

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
