#Hangman game Steps: 

hanged_man = [
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]
#Step 1
world_list=["africa","asia","europe","north america","south america","australia","antarctica"]

import random   #importing random module

chosen_word=random.choice(world_list)  #randomly choosing a word from the list  

#Step 2
display=[]  #empty list
word_length=len(chosen_word)  #length of the chosen word
for _ in range(word_length):  #iterating through the chosen word
    display+="_"  #adding "_" to the display list
print(display)  #printing the display list

#Nr de vieti
lives=len(hanged_man)

#Step 3
while "_" in display:  #while "_" is in the display list
    guess=input("Enter a letter: ").lower()  #taking input from the user
    
    for position in range(word_length):  #iterating through the word length
        letter=chosen_word[position]  #assigning the letter to the position
        if letter==guess:  #if the letter is equal to the input
            display[position]=letter  #display the letter in the position
            print(hanged_man[6-lives])
            
    print(display)  #print the display list
    
    if guess not in chosen_word:
        lives-=1
        print(f"You have {lives} lives left")
        print(hanged_man[6-lives])
        
        if lives==0:
            print("You lose")
            break

