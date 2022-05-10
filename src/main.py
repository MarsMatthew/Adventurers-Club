####################################################
##Matthew Sorensen                                ##
##Erick Guarneros                                 ##
##"Welcome, Adventurer!"                          ##
##2022 4th Quarter Programming 1 Project          ##
####################################################

import os
import random
from Encounter import Encounter
from Player import Player

p1 = Player()
e1 = Encounter()

location = 0
inCombat = 0
occupied = 0
woodChest = 1
currWeap = ["No Weapon", 0, 0, False]
currARM = ["No Armor", 0, 0, False]
currMGC = ["No Magic Weapon", 0, 0, False]
blStSwrd = ['Steel Sword', 10, 20, True]
blIrMace = ['Iron Mace', 15, 30, True]
blBaStaff = ['Wood staff', 5, 20, True]
blChArmor = ['Chainmail Armor', 5, 20, True]

p1.Name = input("What is your name?: ")
os.system('clear')

#What's Happening:
#1. Classes are defined and then StrtSQ is called.
#2. At the end of the sequence ready is called


def StrtSQ():
    global occupied, inCombat, woodChest, currWeap, currARM, currMGC, blStSwrd, blIrMace, blBaStaff, blChArmor
    go = 'y'
    run = 1
    while go == 'y':
        while run == 1:
            p1.Alive = 1
            p1.HP = 50
            p1.ATK = 5
            p1.ARM = 0
            p1.XP = 0
            p1.MON = 0
            p1.pigGot = 0
            p1.villGot = 0
            occupied = 1
            inCombat = 0
            location = 0
            woodChest = 1
            currWeap = ["No Weapon", 0, 0, False]
            currARM = ["No Armor", 0, 0, False]
            currMGC = ["No Magic Weapon", 0, 0, False]
            blStSwrd = ['Steel Sword', 10, 20, True]
            blIrMace = ['Iron Mace', 15, 30, True]
            blBaStaff = ['Wood staff', 5, 20, True]
            blChArmor = ['Chainmail Armor', 5, 20, True]
            #When ran, If it looks weird stretch out the console

            print(
                "██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗\n██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝\n██║ █╗ ██║████╗   ██║     ██║     ██║   ██║██╔████╔██║█████╗\n██║███╗██║██╔═╝   ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝\n╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗▄█╗\n ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝\n\n █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗██████╗\n██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝██╔══██╗\n███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗  ██████╔╝\n██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝  ██╔══██╗\n██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗██║  ██║\n╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝"
            )

            print(
                "Press 'Y' to start \nPress 'I' for instructions / rules \nPress 'C' for a cheat sheat\nPress 'E' to exit"
            )
            #GAME STARTS WHEN USER SELECTS 'Y'
            strtInpt = input("\n>")
            if (strtInpt == 'y' or strtInpt == 'Y'):
                go = 'n'
                run = 3
                occupied = 0
                os.system('clear')
                WhereAmI(location)
                Ready(location)

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
                    os.system('clear')
                    go = 'n'
                    run = 3
                    print("")
                    occupied = 1
                elif (giveUp == 'n' or giveUp == 'N'):
                    os.system('clear')
                    go = 'y'
                    run = 1
        else:
            if (run == 2):
                run = input("\nContinue? y/n: ")
                if run == 'y' or run == 'Y':
                    go = 'y'
                    run = 1
                    os.system('clear')
                elif run == 'n' or run == 'N':
                    os.system('clear')
                    go = 'n'


def WhereAmI(location):
    if location == 0:
        print(
            "You look down to see a letter on your lap and there's dribble on your chin.\nYou must've passed out; the letter is halfway pulled out and you don't remember opening it.\nYou open the letter, it reads:\n",
            p1.Name,
            ",\nYou have been selected to save the village from the menacing ENDBOSS\nYour merit is well known and you fit the role perfectly.\nTravel to the dark volcano to find the ENDBOSS\n"
        )
    elif location == 1:
        print("You start on the trail to the village.\n")
    elif location == 2:
        os.system('clear')
        global woodChest
        if woodChest == 1:
            print(
                "You made it to a small campfire.\n a wooden chest sits on the ground."
            )
            woodChest = input("Open chest? y/n: ")
            if woodChest == 'y' or woodChest == 'Y':
                woodChest = 0
                chestRand = random.randint(0, 3)
                if chestRand == 0:
                    e1.encType = 70
                    e1.typeFind()
                    combat(location)
                elif chestRand > 0:
                    monGain = random.randint(40, 50)
                    print("You found", monGain, "gold coins!")
                    p1.MON += monGain
                    print("You now have", monGain, "coins")
                    Ready(location)
            else:
                print("You left the wooden chest alone and rested")
                woodChest = 1
                Ready(location)
        elif woodChest == 0:
            print(
                "You find a cold campfire and an already opened wooden chest, It has nothing of value."
            )
    elif location == 3:
        os.system('clear')
        print(
            "You're nearly there to the village. You stop at a wooden bridge to take a rest"
        )
    elif location == 4:
        os.system('clear')
        print(
            "You enter 'TOWN NAME LMAO'\nIt's a busy looking village with street shops selling food,\nchildren carrying water buckets and firewood,\nand villagers doing this and that."
        )


def Ready(location):
    if inCombat == 0:
        if occupied == 0:
            if p1.Alive == 1:
                #Instructions
                print(
                    "Enter 'f' to move foward\nEnter 'b' to move backward\nEnter 'p' for details about your person\nEnter 'l' to print location details"
                )
                if location == 4:
                    print(
                        "\nEnter '1' to go to the Blacksmith\nEnter '2' to the Butcher\nEnter '3' to talk to the Villagers"
                    )
                r1 = input(">")
                #MOVEMENT
                if (r1 == 'p' or r1 == 'P'):
                    print("\nXp: ", p1.XP, "\nAttack: ", p1.ATK, "\nMagic: ",
                          p1.MGC, "\nArmor: ", p1.ARM, "\nMoney: ", p1.MON,
                          "\n")
                    if p1.pigGot == 1:
                        print("You have the butcher's pig")
                    if p1.villGot == 1:
                        print(
                            "You found the lost villager. Bring her to the other villagers."
                        )
                    r1 = 0
                    Ready(location)
                elif (r1 == 'f' or r1 == 'F'):
                    location += 1
                    WhereAmI(location)
                    if (occupied == 0 and inCombat == 0 and location != 2):
                        e1.encType = random.randint(0, 15)
                        e1.typeFind()
                        if (e1.hostile == 0):
                            print("Something catches your eye, you find",
                                  e1.Name)
                            peacefulEnc(currWeap)
                            Ready(location)
                        elif (e1.hostile == 1):
                            combat(location)
                        elif (e1.hostile == 2):
                            print("You traveled safely")
                            Ready(location)
                elif (r1 == 'b' and location != 0
                      or r1 == 'B' and location != 0):
                    location -= 1
                    WhereAmI(location)
                    Ready(location)
                elif (r1 == 'l' or r1 == 'L'):
                    print("You are at location ", location)
                    Ready(location)
                elif (location == 4 and r1 == '1'):
                    os.system('clear')
                    EnterSmith()
                    p1.Inventory(currWeap, currARM, currMGC)
                    Ready(location)
                elif (location == 4 and r1 == '2'):
                    os.system('clear')
                    EnterButcher()
                elif (location == 4 and r1 == '3'):
                    print("You go to the villagers")
                else:
                    print("An error occured. Please retype that")
                    Ready(location)


def peacefulEnc(currWeap):
    #Bag of money
    if e1.encType == 0 and location != 4:
        monGain = random.randint(30, 50)
        print("You took", monGain, "gold")
        p1.MON += monGain
    #Villager
    elif e1.encType == 1 and location != 4 and p1.villGot == 0:
        print("Villager found! help her return to the village.")
        p1.villGot = 1
    #Old Man Encounter
    elif e1.encType == 2 and location != 4 and p1.oldEnc == 0:
        p1.oldEnc = 1
        print(
            "You found a lost old man. You ask him if he needs help and he spits in your face."
        )
        oldMan = input("Leave him alone or fight? 'l' to leave, 'f' to fight")
        if oldMan == 'f' or oldMan == 'F':
            combat(location)
        elif oldMan == 'l' or oldMan == 'L':
            print('He says "Its dangerous to go alone, take this!"')
            if currWeap[0] != "No Weapon":
                print(
                    "You can't take the Wooden Weapon (5 ATK) because you already have a weapon"
                )
                #Sell()
            elif currWeap[0] == "No Weapon":
                currWeap = ["WOODEN WEAPON", 5, 10, False]
                print("WOODEN WEAPON GOT!")
    #Pig
    elif e1.encType == 3 and location != 4 and p1.pigGot == 0:
        print("This must be the butcher's Pig. I should take it back")
        p1.pigGot = 1


def combat(location):
    print(e1.Name, "jumps out at you")
    e1.Alive = 1
    while e1.Alive == 1 and p1.Alive == 1:
        global inCombat
        inCombat = 1
        print("\n", "HP: ", e1.HP, "\n", "ATK: ", e1.ATK, "\n", "ARMOR: ",
              e1.ARM)
        print("\nYou're stats:", "\n", "\n", "HP: ", p1.HP, "\n", "ATK:",
              p1.ATK, "\n", "ARMOR: ", p1.ARM, "\n")
        print("a to Attack\nm to use Magic\ns to surrender")
        combatOpt = input("What's your move?\n>")
        if combatOpt == 'a' or combatOpt == 'A':
            atkM = random.randint(0, p1.ATK)
            atkDMG = p1.ATK + atkM
            e1.HP -= atkDMG
            print("Your attack hit! You did", atkDMG,
                  "damage. The enemy's hp is now", e1.HP)
            if e1.HP > 0:
                p1.HP -= e1.ATK
                print(e1.Name, "Hit you for", e1.ATK, "Damage")
        elif (combatOpt == 'm' and p1.HP < 50
              or combatOpt == 'M' and p1.HP < 50):
            p1.HP += p1.MGC
            print("You Healed Yourself for", p1.MGC,
                  "HP. You brace yourself for the enemy's attack")
            p1.HP -= int(e1.ATK / 2)
            print("The enemy did", int(e1.ATK / 2), "damage to you")
        if e1.HP <= 0:
            e1.Alive = 0
        if p1.HP <= 0:
            p1.Alive = 0
            GameOver()
    if e1.Alive == 0:
        print("Success! You killed", e1.Name)
        #Evils from 4 to 9
        if e1.encType == 4:
            xpGain = random.randint(0, 30)
            monGain = random.randint(0, 10)
            #Drop armor and weapon possibility
        elif e1.encType == 5:
            xpGain = random.randint(0, 30)
            monGain = random.randint(0, 10)
            #Drop armor possiblity
        elif e1.encType == 6:
            xpGain = random.randint(0, 30)
            monGain = random.randint(0, 10)
            #Drop armor and weapon possibility
        elif e1.encType == 7:
            xpGain = random.randint(0, 30)
            monGain = random.randint(0, 10)
            #Drop armor and weapon possibility
        elif e1.encType == 8:
            xpGain = random.randint(0, 30)
            monGain = random.randint(0, 10)
            #Drop armor and weapon possibility
        elif e1.encType == 9:
            xpGain = random.randint(0, 30)
            monGain = random.randint(0, 10)
            #Drop armor and weapon possibility
        elif e1.encType == 70:
            xpGain = 40
            monGain = 40
        elif e1.encType == 2:
            xpGain = 99
        p1.XP += xpGain
        p1.MON += monGain
        print("You gained", xpGain, "Xp!, You are now at", p1.XP, "XP")
        print("You gained", monGain, "Gold Coins!, You are now at", p1.MON,
              "Gold")
        inCombat = 0
        Ready(location)


def GameOver():
    if p1.Alive == 0:
        print(
            "██╗   ██╗ ██████╗ ██╗   ██╗    ██████╗ ███████╗██████╗ ██╗███████╗██╗  ██╗███████╗██████╗\n╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██╔════╝██╔══██╗██║██╔════╝██║  ██║██╔════╝██╔══██╗\n ╚████╔╝ ██║   ██║██║   ██║    ██████╔╝█████╗  ██████╔╝██║███████╗███████║█████╗  ██║  ██║\n  ╚██╔╝  ██║   ██║██║   ██║    ██╔═══╝ ██╔══╝  ██╔══██╗██║╚════██║██╔══██║██╔══╝  ██║  ██║\n   ██║   ╚██████╔╝╚██████╔╝    ██║     ███████╗██║  ██║██║███████║██║  ██║███████╗██████╔╝\n   ╚═╝    ╚═════╝  ╚═════╝     ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝"
        )
        redo = input("Retry? y/n: ")
        if redo == 'y' or redo == 'Y':
            os.system('clear')
            StrtSQ()
        else:
            os.system('clear')


def EnterSmith():
    global currWeap, currMGC, currARM
    print("You go to the blacksmith")
    print(
        "The intense heat from the forge causes you to take a slight step backward."
    )
    print(
        "Blacksmith: 'Well come on in boy. Dont let the flies in.'\n'Go ahead and look at the wares'.\n"
    )
    if blStSwrd[3] == True:
        print("Steel Sword (10 ATK) - Price 20 Gold - Enter '1'\n")
    if blIrMace.count(True) == 1:
        print("Iron Mace (15 ATK) - Price 30 Gold - Enter '2'\n")
    if blBaStaff.count(True) == 1:
        print("Basic Wooden Staff (5 MGC) - Price 20 Gold - Enter '3'\n")
    if blChArmor[3] == True:
        print("Chainmail Armor Suit (5 Armor) - Price 20 Gold - Enter '4'\n")
    shopChoice = input("What do you want to buy?\n>")
    if shopChoice == '1' and blStSwrd[3] == True:
        if p1.MON >= 20:
            if currWeap[0] == "No Weapon":
                print("Steel Sword Got")
                currWeap = blStSwrd
                p1.MON -= 20
                blStSwrd[3] = False
            else:
                print(
                    "You have to sell your current weapon before you can buy this"
                )
                #Sell()
        elif p1.MON < 20:
            print("Pah! I want real money now get out of here.")
    elif shopChoice == '2' and blIrMace[3] == True:
        if p1.MON >= 30:
            if currWeap[0] == "No Weapon":
                print("Iron Mace Got")
                currWeap = blIrMace
                p1.MON -= 30
                blIrMace[3] = False
            else:
                print(
                    "You have to sell your current weapon before you can buy this"
                )
                #Sell()
        elif p1.MON < 30:
            print("Pah! I want real money now get out of here.")
    elif shopChoice == '3' and blBaStaff[3] == True:
        if p1.MON >= 20:
            if currMGC[0] == "No Magic Weapon":
                print("Basic Wooden Staff Got")
                currMGC = blBaStaff
                p1.MON -= 20
                blBaStaff[3] = False
            else:
                print(
                    "You have to sell your current weapon before you can buy this"
                )
                #Sell()
        elif p1.MON < 20:
            print("Pah! I want real money now get out of here.")
    elif shopChoice == '4' and blChArmor[3] == True:
        if p1.MON >= 20:
            if currARM[0] == "No Armor":
                print("Chainmail Armor Got")
                currARM = blChArmor
                p1.MON -= 20
                blChArmor[3] = False
            else:
                print(
                    "You have to sell your current armor before you can buy this"
                )
                #Sell()
        elif p1.MON < 20:
            print("Pah! I want real money now get out of here.")
    else:
        print("Blacksmith: Unfortunately that is out of stock.")


def EnterButcher():
    print(
        "You Enter the buther's shop, the smell of meat makes your eyes water")
    if p1.pigGot == True:
        print(
            "Butcher: MY PIG! WHAT ARE YOU DOING WITH HIM! I KNEW SOMEBODY TOOK IT!\nYou quickly explain that randomly encountered the pig.\n\nYou give him the pig.\n\nButcher: Thank you, she's my prized pig. If I lost the damn thing I wouldnt be able to afford my tax.\nButcher: Here, I'll give you a portion of the money as a thank you"
        )
        monGain = 20
        p1.MON += monGain
        print("You gained", monGain, "coins for returning the pig")
    else:
        print("You see the butcher looking stressed and ask him what's the matter\n\nButcher: Ah I've lost 'er, I know somebody stole her.\n\nYou talk about your own partner that left you, nearly breaking into a sob.\n\nButcher: Oh me boy, I don't mean a human I mean my pig.\n\nYou Look at him with disgust and he quickly realizes the scenario\n\nButcher: No not like that! I mean my prized pig has gotten out and If i can't sell her I wont be able to afford tax.")
    print("Butcher:Please, look around!")
def Villagers():
  print("You walk up to a group of villagers")
  if p1.villGot == True:
    print("Villager 2: OH JACKIE YOU'RE BACK!\nVillager 1: Jackie, where have you been")


StrtSQ()
