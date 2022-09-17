# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as file:
    data = file.read()
    names = data.split("\n")
    file.close()

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    file.close()

for name in names:
    new_letter = letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_to_{name}", "w") as file:
        file.write(new_letter)


