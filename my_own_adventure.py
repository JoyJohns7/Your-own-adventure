# This is my adventure. Select the options and enjoy
from npcs import Npcs  # The module NPC contains the npc of this game
import random

# Weather and envioronment

ENVIROMENT = ("windy", "sunny", "rainy", "cloudy")
random_weather = random.choice(ENVIROMENT)

# Make you player
player = input("What is your adventorous name? ")

# ist of habilities
elements_control = []

# List of my stuff(inventory)
weapons = []
spells = {}
skills = {}
health = 4

# Enemies
ENEMIES = ["goblin", "big bat", "big mouse"]

print(
    "Hi Adventorous",
    player,
    "and welcome to this history, your mision is end you day alives",
)

answer_of_the_element = input(
    "You have to select one of this two elements control, fire or water. Which elements do you want to control? (fire/water) "
).lower()

# Here you select your element
while True:
    if answer_of_the_element == "fire":
        elements_control.append("fire")
        spells[
            "fire ball"
        ] = 600  # This is a spell for the magic book, the number is the power
        skills["fire cut"] = 500
        print("You select fire control.")
        break

    elif answer_of_the_element == "water":
        elements_control.append("water")
        spells[
            "water ball"
        ] = 500  # This is a spell for the magic book, the number is the power
        skills["water movement"] = 600
        print("You select water control.")
        break

    else:
        print("You have to select fire or water. This option is wrong. You lose")
        quit()

# Here you select your weapon
# The class NPC contains the npcs of this game

dialogue = Npcs()

print(dialogue.npc_lopez())
while True:
    answer_of_the_weapon = input(
        "Each new warrior needs to select one of these weapons magic sword or spell book. Select one \nwrite sword or book "
    ).lower()

    if answer_of_the_weapon == "book":
        weapons.append("spell book")
        print("You select a spell book.")
        print()
        break
    elif answer_of_the_weapon == "sword":
        weapons.append("magic sword")
        print("You select a magic sword.")
        print()
        break
    else:
        print("You have to select book or sword. This option is wrong. You lose")
        quit()

print(
    "Your profile is done.\nYour element:",
    elements_control[0],
    "\nYour weapon:",
    weapons[0],
)
print()

# Here start the history
print("Today the weather is", random_weather)
print(
    "Welcome new adventurer this is your first day in this world\nGo to the tavern and select your task"
)
print()

dialogue.npc_bartender(1)  # Number of the dialogue that you want to output

election = input(
    "Where do you want to go? To the Forest or The Cave\nWrite forest or cave "
).lower()

# Forest
if election == "forest":
    while health >= 0:
        print(
            "You enter the forest and you find a old men, do you want to talk with him or do you want to continue on your way"
        )
        election = input("Write talk or continue ").lower()
        print()
        random_enemy = random.choice(ENEMIES)
        if election == "continue":
            print(
                "You continue and then you get lose and you are hurt by a",
                random_enemy,
            )
            health -= 1
            print("You come back and you decide to talk with the old men")
            print()
            print(dialogue.npc_old_men())
            your_choice = input(
                "Do you want to go to the ruins or do you want to continue\nWrite go or continue "
            ).lower()
            print()
            if your_choice == "continue":
                print(
                    "You continue and then you get lose and you are hurt by a",
                    random_enemy,
                )
                health -= 1
                print("You are so dumb, Please go to the ruins")
                print()
                your_choice = input(
                    "Do you want to go to the rouins or do you want to continue\nWrite go or continue "
                ).lower()
                if your_choice == "continue":
                    print("You die for a", random_enemy)
                    health -= 3
                elif your_choice == "go":
                    election = input(
                        "You enter and there are two ways, left and right.\nWhere do you want to go? (write left or right) "
                    ).lower()

                    if election == "right":
                        election = input(
                            "A big bat appears, Do you want to run or fight? (write run or fight) "
                        ).lower()
                        if election == "fight":
                            enemy = Npcs()
                            if answer_of_the_weapon == "book":
                                for key, power in spells.items():
                                    print("your attack is", key, "with power", power)
                                enemy.npc_enemy_bat(spells)
                                print("You continue and you find a new spell")
                                break
                            elif answer_of_the_weapon == "sword":
                                for key, power in skills.items():
                                    print("your attack is", key, "with power", power)
                                enemy.npc_enemy_bat(skills)
                                print("You continue and you find a new chest armor")
                                break
                        elif election == "run":  # Continue with this
                            pass
                    elif election == "left":  # Continue with this
                        pass

                    else:
                        print(
                            "You wrote the election wrong or the option is not in the options... You DIE! Dumd"
                        )
                        health -= 4
            elif your_choice == "go":
                election = input(
                    "You enter and there are two ways, left and right.\nWhere do you want to go? (write left or right) "
                ).lower()

                if election == "right":
                    election = input(
                        "A big bat appears, Do you want to run or fight? (write run or fight) "
                    ).lower()
                    if election == "fight":
                        enemy = Npcs()
                        if answer_of_the_weapon == "book":
                            for key, power in spells.items():
                                print("your attack is", key, "with power", power)
                            enemy.npc_enemy_bat(spells)
                            print("You continue and you find a new spell")
                            break
                        elif answer_of_the_weapon == "sword":
                            for key, power in skills.items():
                                print("your attack is", key, "with power", power)
                            enemy.npc_enemy_bat(skills)
                            print("You continue and you find a new chest armor")
                            break
                    elif election == "run":  # Continue with this
                        pass
                elif election == "left":  # Continue with this
                    pass

                else:
                    print(
                        "You wrote the election wrong or the option is not in the options... You DIE! Dumd"
                    )
                    health -= 4

        elif election == "talk":
            print(dialogue.npc_old_men())
            your_choice = input(
                "Do you want to go to the ruins or do you want to continue\nWrite go or continue "
            ).lower()
            print()
            if your_choice == "continue":
                print(
                    "You continue and then you get lose and you are hurt by a",
                    random_enemy,
                )
                health -= 1
                print("You are so dumb, Please go to the ruins")
                print()
                your_choice = input(
                    "Do you want to go to the rouins or do you want to continue\nWrite go or continue "
                ).lower()
                if your_choice == "continue":
                    print("You die for a", random_enemy)
                    health -= 3

            elif your_choice == "go":
                election = input(
                    "You enter and there are two ways, left and right.\nWhere do you want to go? (write left or right) "
                ).lower()

                if election == "right":
                    election = input(
                        "A big bat appears, Do you want to run or fight? (write run or fight) "
                    ).lower()
                    if election == "fight":
                        enemy = Npcs()
                        if answer_of_the_weapon == "book":
                            for key, power in spells.items():
                                print("your attack is", key, "with power", power)
                            enemy.npc_enemy_bat(spells)
                            print("You continue and you find a new spell")
                            break
                        elif answer_of_the_weapon == "sword":
                            for key, power in skills.items():
                                print("your attack is", key, "with power", power)
                            enemy.npc_enemy_bat(skills)
                            print("You continue and you find a new chest armor")
                            break
                    elif election == "run":  # Continue with this
                        pass
                elif election == "left":  # Continue with this
                    pass

                else:
                    print(
                        "You wrote the election wrong or the option is not in the options... You DIE! Dumd"
                    )
                    health -= 4
        else:
            health -= 4

# Cave
elif election == "cave":
    print("cave")
else:
    print("This option is not valid")

if health <= 0:
    print("You lost")


# Here is the radom weather (Work with this later)
random_weather = random.choice(ENVIROMENT)


# Here is the score that his output will be in other file
"""score = 150


def score_file(your_score):
    with open("YourScore.txt", "a") as file:
        file.write("Your Score is " + str(your_score))


score_file(score)"""

print("The end")
