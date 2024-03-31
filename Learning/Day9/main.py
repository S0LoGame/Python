#Exercitiul 1
# programing_dictionary = { 
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again."
    
#     }

#Retrieving items from dictionary.
# print(programing_dictionary["Bug"])

#Adding new items to dictionary.
# programing_dictionary["Loop"] = "The action of doing something over and over again."
# print(programing_dictionary)

#Create an empty dictionary.
# empty_dictionary = {}

#Wipe an existing dictionary.
# programing_dictionary = {}
# print(programing_dictionary)

#Edit an item in a dictionary.
# programing_dictionary["Bug"]= "A moth in your computer."
# print(programing_dictionary)

#Loop through a dictionary.
# for thing in programing_dictionary:
#     print(thing)
#     print(programing_dictionary[thing])

#Exercitiul 2
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62
# }

# student_grades = {}

# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"


# print(student_grades)

#Exercitiul 3
#Nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }

#Nesting a List in a Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# } 

#Nesting Dictionary in a Dictionary
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
# }

#Nesting Dictionary in a List
# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5
#     }
# ]

#Exercitiul 4
# travel_log = [
# {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]


# def add_new_country(country, visits, cities):
#     new_country = {}
#     new_country["country"] = country
#     new_country["visits"] = visits
#     new_country["cities"] = cities
#     travel_log.append(new_country)

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# add_new_country("Romania", 1, ["Bucuresti", "Cluj-Napoca"])
# print(travel_log)

#Exercitiul 5
#Blind Auction
# from replit import clear

# bids= {}
# biding_finished = False

# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     winner = ""
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder] 
#         if bid_amount > highest_bid: 
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}")


# while not biding_finished:
#     name = input("What is your name?: ")
#     bid = int(input("What's your bid?: $"))
#     bids[name] = bid
#     should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
#     if should_continue == "no":
#         biding_finished = True
#     elif should_continue == "yes":
#         clear()

# find_highest_bidder(bids)
