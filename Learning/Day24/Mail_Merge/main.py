#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        

with open("d:/Python/Git-Repo/Python/Learning/Day24/Mail_Merge/Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    print(letter)
    
with open("d:/Python/Git-Repo/Python/Learning/Day24/Mail_Merge/Input/Names/invited_names.txt") as file:
    names = file.readlines()
    print(names)   
    
for name in names:
    stripped_name = name.strip()
    new_letter = letter.replace("[name]", stripped_name)
    with open(f"d:/Python/Git-Repo/Python/Learning/Day24/Mail_Merge/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as file:
        file.write(new_letter)
    


