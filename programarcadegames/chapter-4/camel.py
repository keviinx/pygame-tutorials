"""Camel Game"""
import random
import os

# Variable declaration
done = False
miles_traveled = 0
thirst = 0
camel_tiredness = 0
miles_natives_traveled = -20
drinks_in_canteen = 3

# print intro
print(
    """
   ______                     __
  / ____/___ _____ ___  ___  / /
 / /   / __ `/ __ `__ \/ _ \/ /
/ /___/ /_/ / / / / / /  __/ /
\____/\__,_/_/ /_/ /_/\___/_/
"""
)
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")

# main program loop
while not done:
    print()
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop and rest.")
    print("E. Status check.")
    print("Q. Quit")
    print()
    user_choice = input("Your choice? ").upper()
    # Clear screen after input
    os.system("cls")

    # quits
    if user_choice == "Q":
        done = True

    # status check
    elif user_choice == "E":
        print()
        print("Miles traveled:  {}".format(miles_traveled))
        print("Drinks in canteen:  {}".format(drinks_in_canteen))
        print(
            "The natives are {} miles behind you.".format(
                miles_traveled - miles_natives_traveled
            )
        )

    # stop and rest
    elif user_choice == "D":
        camel_tiredness = 0
        # move the natives up 7 to 14 miles
        miles_natives_traveled += random.randrange(7, 15)
        print()
        print("Camel is happy.")

    # ahead full speed
    elif user_choice == "C":
        full_speed_miles_traveled = random.randrange(10, 21)
        miles_traveled += full_speed_miles_traveled
        thirst += 1
        camel_tiredness += random.randrange(1, 4)
        miles_natives_traveled += random.randrange(7, 15)
        print()
        print("You traveled {} miles.".format(full_speed_miles_traveled))

    # ahead moderate speed
    elif user_choice == "B":
        moderate_speed_miles_traveled = random.randrange(5, 13)
        miles_traveled += moderate_speed_miles_traveled
        thirst += 1
        camel_tiredness += 1
        miles_natives_traveled += random.randrange(7, 15)
        print()
        print("You traveled {} miles.".format(moderate_speed_miles_traveled))

    elif user_choice == "A":
        if drinks_in_canteen > 0:
            drinks_in_canteen -= 1
            thirst = 0
            print()
            print("You took a drink from the canteen. It quenched your thirst.")
        else:
            print()
            print("There is no drink left in your canteen.")

    # only find oasis when moving
    if user_choice == "B" or user_choice == "C":

        # one in twenty chance to find an oasis
        if random.random() < 0.05:
            thirst = 0
            camel_tiredness = 0
            drinks_in_canteen = 3
            print(
                "You found an oasis! You refilled your canteen, "
                "your thirst was quenched and your camel is well-rested and happy."
            )

    if thirst > 4 and thirst <= 6:
        print("You are thirsty.")
    elif thirst > 6:
        print("You died of thirst!")
        done = True
        input("Press ENTER to end the game.")

    if camel_tiredness > 5 and camel_tiredness <= 8 and done != True:
        print("Your camel is getting tired.")
    elif camel_tiredness > 8:
        print("Your camel is dead.")
        done = True
        input("Press ENTER to end the game.")

    if miles_natives_traveled >= miles_traveled:
        print("The natives caught you!")
        done = True
        input("Press ENTER to end the game.")
    elif miles_traveled - miles_natives_traveled < 15:
        print("The natives are getting close!")

    if miles_traveled >= 200 and done != True:
        print("You managed to crossed the great Mobi desert with your camel! You won!")
        done = True
        input("Press ENTER to end the game.")
