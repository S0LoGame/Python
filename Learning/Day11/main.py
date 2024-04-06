#Joc de BlackJack
# Salut! Bine ai venit la jocul de BlackJack!

import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

jucator = []
computer = []

def joc_blackjack():
    for _ in range(2):
            jucator.append(random.choice(cards))
            computer.append(random.choice(cards))
    
    game_over = False
    
    while not game_over:
            puncte_jucator = calculare_puncte(jucator)
            puncte_computer = calculare_puncte(computer)
            print(f"Cartile tale: {jucator}, punctele tale: {puncte_jucator}")
            print(f"Prima carte a adversarului: {computer[0]}")
    
            if puncte_jucator == 0 or puncte_computer == 0 or puncte_jucator > 21:
                    game_over = True
            else:
                    alta_carte = input("Doresti o alta carte? Da sau Nu: ")
                    if alta_carte == "Da":
                            jucator.append(random.choice(cards))
                    else:
                            game_over = True
    
    while puncte_computer != 0 and puncte_computer < 17:
            computer.append(random.choice(cards))
            puncte_computer = calculare_puncte(computer)
    
    print(f"Cartile tale: {jucator}, punctele tale: {puncte_jucator}")
    print(f"Cartile adversarului: {computer}, punctele adversarului: {puncte_computer}")
    print(comparare(puncte_jucator, puncte_computer))

def calculare_puncte(carti):
    if sum(carti) == 21 and len(carti) == 2:
        return 0
    if 11 in carti and sum(carti) > 21:
        carti.remove(11)
        carti.append(1)
    return sum(carti)

def comparare(puncte_jucator, puncte_computer):
    if puncte_jucator == puncte_computer:
        return "Egalitate"
    elif puncte_computer == 0:
        return "Ai pierdut, adversarul are Blackjack"
    elif puncte_jucator == 0:
        return "Ai castigat cu Blackjack"
    elif puncte_jucator > 21:
        return "Ai pierdut, ai depasit 21"
    elif puncte_computer > 21:
        return "Ai castigat, adversarul a depasit 21"
    elif puncte_jucator > puncte_computer:
        return "Ai castigat"
    else:
        return "Ai pierdut"
    
joc_blackjack()
while input("Doresti sa joci din nou? Da sau Nu: ") == "Da":
    jucator = []
    computer = []
    joc_blackjack()

print("La revedere!")
