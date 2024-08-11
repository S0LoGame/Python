# Exercitiu 1


# enemies = 1

# def incresase_enemies():
#     enemies = 2
#     print(f"Enemies inside function: {enemies}")
    
# incresase_enemies()
# print(f"Enemies outside function: {enemies}")


#Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
    
# drink_potion()
# print(potion_strength) # eroare pentru ca variabila potion_strength este locala si nu poate fi accesata in afara functiei


#Global Scope

# player_health = 10

# def drink_potion():
#     potion_strength = 2
#     print(player_health)
    
# drink_potion()
# print(player_health) # variabila player_health este globala si poate fi accesata in afara 


#There is no Block Scope

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]
    
# print(new_enemy) # variabila new_enemy este accesibila in afara blocului if, deoarece Python nu are block scope


# Exercitiul 2 Welcome to the Number Guessing Game!

import random

print("Welcome to the Number Guessing Game!")

number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5
    

guess = 0

while guess != number:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    attempts -= 1
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        break
    elif guess == number:
        print(f"You got it! The answer was {number}.")
        break
    else:
        print("Guess again.")
        

