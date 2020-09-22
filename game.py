print("Welcome to the game!")
name = input("Enter your username:  ")
print("What a good name for a citizen of Natville!")
role = input("Do you wish to be a knight or a mage?")
if role == "knight":
    print("Very well then, you shall be a knight.")
elif role == "mage":
    print("Very well then, you shall become a mage.")
print("Let's go visit the town.")
place = input("Do you want to visit the armory or the townhall first?")
if place == "armory":
    print("Ok, the armory is near the South exit. Let's go.")
elif place == "townhall":
    print("Ok then, the townhall is in the center. Let's go.")