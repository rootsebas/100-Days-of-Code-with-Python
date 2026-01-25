# EXERCISES

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# print("Check Odd or Even")
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"Number {num} is Odd")
# else:
#     print(f"Number {num} is Even")

# print(False or True or False)

# DAY3 - PROJECT

from string import ascii_letters


print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
start = input(" Type 'left' or 'right' \n").lower()

if start == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    option = input(" Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()

    if option == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        door = input(" One red, one yellow and one blue. Which colour do you choose? \n").lower()
        
        if door == "yellow":
            print("You Win!")
        elif door == "blue":
            print("Eaten by beasts. GAME OVER!")
        elif door == "red":
            print("Burned by fire. GAME OVER!")
        else:
            print("GAME OVER!")
    elif option == "swim":
        print("Attacked by trout. GAME OVER!")

elif start == "right":
    print("Fall into a hole. GAME OVER!")
