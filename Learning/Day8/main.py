#Exercitiul 1
# def greet(name="Stranger"):
#     print("Hello " + name + "!")
#     print("how do you do " + name + "?")
#     print("Isn't the weather nice today?")

# greet("Marius")
# greet("Anca")

#Exercitiul 2
# def greet_with(name, location,final):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
#     print(f"Cand pleci inapoi la {final}?")
    
# greet_with("Marius", "Iasi","Galati")
# greet_with("Anca", "Iasi","Galati")
# greet_with(name="Marius", location="Iasi",final="Galati")
# greet_with(name="Anca", location="Iasi",final="Galati")

#Exercitiul 3
# import math 


# def paint_calc(test_h, test_w, coverage):
#     paint_calculation=math.ceil((test_h*test_w)/coverage)
#     print(f"You'll need {paint_calculation} cans of paint.")

# test_h=int(input("Introduceti inaltimea: "))
# test_w=int(input("Introduceti latimea: "))
# coverage=5
# paint_calc(test_h, test_w, coverage)

#Exercitiul 4
# def prime_checker(number):
#     for i in range(2,number):
#         if number%i==0:
#             print(f"{number} is not a prime number")
#         else:
#             print(f"{number} is a prime number")
#             break
        

# n=int(input("Check this number: "))
# prime_checker(number=n)


#Exercitiul 5
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z',' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z',' ']

def ceaser(text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet: 
            position = alphabet.index(letter)
            new_position = position + shift
            new_letter = alphabet[new_position]
            end_text += new_letter
        else:
            end_text += letter
            
    print(f"The {direction}d text is {end_text}")
    

# def encrypt(text, shift):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# def decrypt(text, shift):
#     decipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         new_letter = alphabet[new_position]
#         decipher_text += new_letter
#     print(f"The decoded text is {decipher_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
ceaser(text, shift, direction)
again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")


while again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text, shift, direction)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    
# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("Invalid input")


