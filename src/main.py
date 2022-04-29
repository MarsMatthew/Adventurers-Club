####################################################
##Matthew Sorensen                                ##
##Erick Guarneros                                 ##
##"Welcome, Adventurer!"                          ##
##2022 4th Quarter Programming 1 Project          ##
####################################################

import replit
import random
from Encounter import Encounter
from Player import Player

p1 = Player()
e1 = Encounter()
replit.clear()

location = 0
inCombat = 0
occupied = 0

#What's Happening:
#1. Classes are defined and then StrtSQ is called.
#2. At the end of the sequence ready is called


def StrtSQ():
    global occupied
    go = 'y'
    run = 1
    while go == 'y':
        while run == 1:
            #When ran, If it looks weird stretch out the console

            print(
                "██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗\n██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝\n██║ █╗ ██║████╗   ██║     ██║     ██║   ██║██╔████╔██║█████╗\n██║███╗██║██╔═╝   ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝\n╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗▄█╗\n╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝\n\n █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗██████╗\n██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝██╔══██╗\n███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗  ██████╔╝\n██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝  ██╔══██╗\n██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗██║  ██║\n╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝"
            )

            print("Press 'Y' to start")
            print("Press 'I' for instructions / rules")
            print("Press 'C' for a cheat sheat")
            print("Press 'E' to exit")
            #GAME STARTS WHEN USER SELECTS 'Y'
            strtInpt = input("\n>")
            if (strtInpt == 'y' or strtInpt == 'Y'):
                go = 'n'
                run = 3
                occupied = 0
                replit.clear()
                WhereAmI(location)

            elif (strtInpt == 'i' or strtInpt == 'I'):
                print(
                    "Rules: If you die the game ends. So don't die, that's all. \nMade by \nMatthew Sorensen - dummy 1 \nErick Guarneros - dummy 2"
                )
                run = 2

            elif (strtInpt == 'c' or strtInpt == 'C'):
                print(
                    "Make sure to collect lots of money and buy things you think will assist you. \nMonsters you fight may give you items as well as xp and gold, these can be useful for fighting. \nThe objective is to get to the end of the road \n(after 10 road stops!) \nAt the end of the road there is a nasty boss you have been hired to defeat."
                )
                run = 2

            elif (strtInpt == 'e' or strtInpt == 'E'):
                print(
                    " ██████╗ ██╗██╗   ██╗███████╗    ██╗   ██╗██████╗ ██████╗\n██╔════╝ ██║██║   ██║██╔════╝    ██║   ██║██╔══██╗╚════██╗\n██║  ███╗██║██║   ██║█████╗      ██║   ██║██████╔╝  ▄███╔╝\n██║   ██║██║╚██╗ ██╔╝██╔══╝      ██║   ██║██╔═══╝   ▀▀══╝ \n╚██████╔╝██║ ╚████╔╝ ███████╗    ╚██████╔╝██║       ██╗   \n ╚═════╝ ╚═╝  ╚═══╝  ╚══════╝     ╚═════╝ ╚═╝       ╚═╝   "
                )
                giveUp = input("y/n: ")
                if (giveUp == 'y' or giveUp == 'Y'):
                    replit.clear()
                    go = 'n'
                    run = 3
                    print("")
                    occupied = 1
                elif (giveUp == 'n' or giveUp == 'N'):
                    replit.clear()
                    go = 'y'
                    run = 1
        else:
            if (run == 2):
                run = input("\nContinue? y/n: ")
                if run == 'y' or run == 'Y':
                    go = 'y'
                    run = 1
                    replit.clear()
                elif run == 'n' or run == 'N':
                    replit.clear()
                    go = 'n'


def WhereAmI(location):
    if location == -1:
        print("You can't move back now! The village requires you.")
        pause = input("Continue? y/n:")
        location = 0
        replit.clear()
        WhereAmI(location)
        Ready(location)
    if location == 0:
        print(
            "You look down to see a letter on your lap and there's dribble on your chin.\nYou must've passed out; the letter is halfway pulled out and you don't remember opening it.\nYou open the letter, it reads:\n",
            p1.Name,
            ",\nYou have been selected to save the village from the menacing ENDBOSS\nYour merit is well known and you fit the role perfectly.\nTravel to the dark volcano to find the ENDBOSS\n"
        )
    if location == 1:
        print("You start on the trail to the village.\n")


def Ready(location):
    if inCombat == 0:
        if occupied == 0:
            #Instructions
            print("Enter 'm' to move")
            print("Enter 'i' for your inventory")
            print("Enter 'p' for details about your person")

            ready = input(">")
            #MOVEMENT
            if ready == 'm':
                move = input(
                    "f to progress Foward, b to progress Backward: \n>")
                if move == 'f':
                    location += 1
                    WhereAmI(location)
                    e1 = Encounter
                    e1.typeFind(e1)
                    if e1.enc > 0:
                        print("You traveled safely")
                    elif e1.hostile == 0:
                        print("Something catches your eye, you find", e1.Name)
                    elif e1.hostile == 1:
                        combat()
                elif move == 'b':
                    location -= 1
                    WhereAmI(location)

            elif ready == 'i':
                #player.Inventory()
                print("placeholder")
            elif ready == 'p':
                #player.Personal()
                print("")


def combat():
    print(e1.Name, "jumps out at you")
    print("\n", "HP: ", e1.HP, "\n", "ATK: ", e1.ATK, "\n", "ARMOR: ", e1.ARM)
    print("You're stats:\nHP: ",p1.HP,"\nATK:",p1.ATK,"\nARMOR: ",p1.ARM)
    print("a to Attack")
    print("m to use Magic")
    print("s to surrender")
    combatOpt = input("What's your move?\n>")
    if combatOpt == 'a' or 'A':
      atkM = random.randint(0,p1.ATK)
      atkDMG = p1.ATK + atkM
      e1.HP -= atkDMG      
    print("Your attack hit! You did The enemy's hp is now",e1.HP)

StrtSQ()
Ready(location)
