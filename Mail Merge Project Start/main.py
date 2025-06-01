#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
letter = open("../Mail Merge Project Start/Input/Letters/starting_letter.txt")
contents = letter.read()
names = open("../Mail Merge Project Start/Input/Names/invited_names.txt")
name_list = names.readlines()
for name in name_list:
    index = name_list.index(name)
    name = name.strip()
    final_letter = open(f"Output/ReadyToSend/invitation{index}.txt", "w")
    final_letter.write(contents.replace("[name]", name))