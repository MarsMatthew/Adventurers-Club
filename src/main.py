####################################################
##Matthew Sorensen                                ##
##Erick Guarneros                                 ##
##"Welcome, Adventurer!"                          ##
##2022 4th Quarter Programming 1 Project          ##
####################################################

import os
import sys
import random
from Encounter import Encounter
from Player import Player
import time

p1 = Player()
e1 = Encounter()

p1.Name = input("What is your name?: ")

def resetVar():
    global occupied, location, inCombat, woodChest, currWeap, currARM, currMGC, blStSwrd, blIrMace, blBaStaff, blChArmor, road, sLoc, butchPig, txtSpeed, currTxtSpd, firstTime
    p1.Alive = 1
    p1.HP = 50
    p1.ATK = 5
    p1.ARM = 0
    p1.XP = 0
    p1.LVL = 1
    p1.pLVL = 0
    p1.MON = 0
    p1.pigGot = 0
    p1.villGot = 0
    occupied = 1
    inCombat = 0
    location = 0
    woodChest = 1
    road = ''
    sLoc = False
    butchPig = False
    txtSpeed = 0.05
    currTxtSpd = 1
    firstTime = True
    currWeap = ["No Weapon", 5, 0, False]
    currARM = ["No Armor", 0, 0, False]
    currMGC = ["No Magic Weapon", 0, 0, False]
    blStSwrd = ['Steel Sword', 10, 20, True]
    blIrMace = ['Iron Mace', 15, 30, True]
    blBaStaff = ['Wood staff', 5, 20, True]
    blChArmor = ['Chainmail Armor', 5, 20, True]
def TextSettings():
    global currTxtSpd, txtSpeed
    print("To change the typing speed, enter 't'\nTo go back press 'y'")
    setInput = input(">")
    if setInput == 't' or setInput == 'T':
        print(
            "Enter 'f' to make text faster,\nEnter 's' to make it slower,\nEnter 'q' to set it to no delays,\nEnter 'y' to go test the text speed"
        )
        txtSpdInpt = input("\n>")
        if txtSpdInpt == 'f' and currTxtSpd == 1:
            txtSpeed = (0.01)
            currTxtSpd = 2
        elif txtSpdInpt == 'f' and currTxtSpd == 2:
            txtSpeed = (0.05)
            currTxtSpd = 1
        elif txtSpdInpt == 's' and currTxtSpd == 1:
            txtSpeed = (0.1)
            currTxtSpd = 0
        elif txtSpdInpt == 's' and currTxtSpd == 2:
            txtSpeed == 0.05
            currTxtSpd == 0
        elif txtSpdInpt == 'q':
            txtSpeed = 0
        elif txtSpdInpt == 'y':
          print_slow("This is the current text speed")
def print_slow(str):
    global txtSpeed
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(txtSpeed)


def StrtSQ():
    global occupied, inCombat, woodChest, currWeap, currARM, currMGC, blStSwrd, blIrMace, blBaStaff, blChArmor, txtSpeed, currTxtSpd
    os.system('clear')
    go = 'y'
    run = 1
    while go == 'y':
        while run == 1:

            print(
                "██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗\n██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝\n██║ █╗ ██║████╗   ██║     ██║     ██║   ██║██╔████╔██║█████╗\n██║███╗██║██╔═╝   ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝\n╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗▄█╗\n ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝\n\n █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗██████╗\n██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝██╔══██╗\n███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗  ██████╔╝\n██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝  ██╔══██╗\n██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗██║  ██║\n╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝"
            )

            print(
                "Press 'Y' to start \nPress 'I' for information / rules \nPress 'S' for settings\nPress 'E' to exit"
            )
            #GAME STARTS WHEN USER SELECTS 'Y'
            strtInpt = input("\n>")
            if (strtInpt == 'y' or strtInpt == 'Y'):
                go = 'n'
                run = 3
                occupied = 0
                os.system('clear')
                WhereAmI(location)
                Ready()

            elif (strtInpt == 'i' or strtInpt == 'I'):
                print(
                    "Rules: If you die the game ends. So don't die, that's all. \nMade by \nMatthew Sorensen - Lead Programmer \nErick Guarneros - Creative Design"
                )
                run = 2

            elif (strtInpt == 's' or strtInpt == 'S'):
              TextSettings()
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
    global road, sLoc, firstTime
    if location == 0:
        sLoc = True
        print_slow(
            "You look down to see a letter on your lap and there's dribble on your chin.\nYou must've passed out; the letter is halfway pulled out and you don't remember opening it.\nYou open the letter, it reads:\n\n"
        )
        print(p1.Name)
        print_slow(
            "You have been selected to save the village from the menacing ENDBOSS\nYour merit is well known and you fit the role perfectly.\nTravel to the dark volcano to find the ENDBOSS\n"
        )
    elif location == 1:
        sLoc = False
        print("You start on the trail to the village.\n")
    elif location == 2:
        sLoc = True
        os.system('clear')
        global woodChest
        if woodChest == 1:
            print_slow(
                "You made it to a small campfire.\nA wooden chest sits on the ground."
            )
            woodChest = input("\nOpen chest? y/n: ")
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
                    Ready()
            else:
                print("You left the wooden chest alone and rested")
                woodChest = 1

                Ready()
        elif woodChest == 0:
            print_slow(
                "You find a cold campfire and an already opened wooden chest, It has nothing of value."
            )

    elif location == 3:
        sLoc = False
        os.system('clear')
        print(
            "You're nearly there to the village. You stop at a wooden bridge to take a rest"
        )
    elif location == 4:
        sLoc = True
        os.system('clear')
        if firstTime == True:
            print_slow(
                "You enter 'Erith'\nIt's a busy looking village with street shops selling food,\nchildren carrying water buckets and firewood,\nand villagers doing this and that."
            )
            firstTime = False
        elif firstTime == False:
            print_slow("You Enter 'Erith'")

    elif location == 5:
        sLoc = True
        os.system('clear')
        print("You leave the vilage and you find a fork in the road")
        road = input("Left 'l' or Right 'r'?: ")
        print(road)
        if road == 'l' or road == 'L':
            os.system('clear')
            print(road)
            print_slow(
                "You follow the left road. After some walking you find an old looking forest."
            )

            print_slow(
                "\nThere is an eeriness about the lack of creatures in the forest and a chill goes up your spine. You consider leaving."
            )
        if road == 'r' or road == 'R':
            os.system('clear')
            print_slow(
                "You follow the path to your right. After some walking you come across a wide shimmering lake.\nA lonely fisher sits at the edge of the water not noticing you behind him.\nYou try to start small talk with him but he only utters a low growl.\nSuddenly the man falls apart and a dozen or so rats fall out\n"
            )
            e1.encType = 71
            e1.typeFind()
            combat(location)
            print(
                "After an intense battle with the rats you look inside of the tackle box that sat beside the dummy."
            )
            monGain = random.randint(10,20)
            p1.MON += monGain
            print("You found", monGain, "coins. You're now at", p1.MON,
                  "coins total")
            print_slow(
                "Also in that box was a note that read 'Only the BRAVE can reel a big one in'"
            )
    elif location == 6:
        if road == 'l' or road == 'L':
            road = 'l'
            print_slow(
                "Despite your concern you move foward.\nYou notice that a tree has letters carved into it.\nYou can barely make out what it says.\n\n'Travelers be warned, the [Unreadable] is not worth the price."
            )
            print("\nYou ask yourself if you REALLY want to go foward")
        elif road == 'r' or road == 'R':
            road = 'r'
            print_slow(
                "You start walking along the edge of the lake. An object beneath the water shimmers in your eye.\nMove foward to grab it or go back."
            )
    elif location == 7:
      if road == 'l':
        print_slow("You hear a deep groan and the floor of the forest starts to swell and break")
        e1.encType = 80
        e1.typeFind()
        combat(location)
      if road == 'r':
        print_slow("The water starts to swell and a giant fish leaps out of the lake.")
        e1.encType = 81
        e1.typeFind()
        combat(location)
    elif location == 8:
      print_slow("You reach the base of the volcano and notice that the previous other road connects up\nYou start to hike your way up the volcano\nIt takes you about 30 minutes to climb halfway and you notice that two villagers are here.")
      Villagers()
      Ready()
    elif location == 9:
      print_slow("You make it to the top of the volcano, if you are ready, jump into the fight.")
      Ready()
    elif location == 10:
      print_slow("Hesitant and shaking you look over the edge and notice a giant pair of eyes looking right back.\n")
      e1.encType = 100
      e1.typeFind()
      combat(location)
      os.system('clear')
      print("You did it! You beat the game!\nMade by Matthew Sorensen and Erick Guarneros")

def Ready():
    global road, sLoc,location
    if inCombat == 0:
        if occupied == 0:
            if p1.Alive == 1:
                #Instructions
                print(
                    "\nEnter 'f' to move foward\nEnter 'b' to move backward\nEnter 'p' for details about your person\nEnter 's' for settings"
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
                          "\nHP:", p1.HP, "\n")
                    if p1.pigGot == 1:
                        print("You have the butcher's pig")
                    if p1.villGot == 1:
                        print(
                            "You found the lost villager. Bring her to the other villagers."
                        )
                    r1 = 0
                    Ready()
                elif (r1 == 'f' or r1 == 'F'):
                    location += 1
                    WhereAmI(location)
                    if (occupied == 0 and inCombat == 0 and sLoc == False):
                        e1.encType = random.randint(0, 15)
                        e1.typeFind()
                        if (e1.hostile == 0):
                            print("Something catches your eye, you find",
                                  e1.Name)
                            peacefulEnc(currWeap)
                            Ready()
                        elif (e1.hostile == 1):
                            combat(location)
                        elif (e1.hostile == 2):
                            print("You traveled safely")
                            Ready()
                    else:
                        Ready()
                elif (r1 == 'b' and location != 0
                      or r1 == 'B' and location != 0):
                    location -= 1
                    WhereAmI(location)
                    Ready()
                elif (r1 == 's' or r1 == 'S'):
                    print("You are at location ", location)
                    TextSettings()
                    Ready()
                elif (location == 4 and r1 == '1'):
                    os.system('clear')
                    EnterSmith()
                    p1.Inventory(currWeap, currARM, currMGC)
                    p1.Experience()
                    Ready()
                elif (location == 4 and r1 == '2'):
                    os.system('clear')
                    EnterButcher()
                elif (location == 4 and r1 == '3'):
                    Villagers()
                    
                else:
                    print("An error occured. Please retype that")
                    Ready()



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
                currWeap = ["WOODEN WEAPON", 8, 10, False]
                print("WOODEN WEAPON GOT!")
    #Pig
    elif e1.encType == 3 and location != 4 and p1.pigGot == 0:
        print("This must be the butcher's Pig. I should take it back")
        p1.pigGot = 1


def combat(location):
    print(e1.Name, "jumps out at you!!\n")
    e1.Alive = 1
    global inCombat
    inCombat = 1
    time.sleep(2)
    os.system('clear')
    while e1.Alive == 1 and p1.Alive == 1 and inCombat == 1:
        #Enemy's stats
        time.sleep(0.5)
        print(e1.Name, "'s stats:\n", "HP: ", e1.HP, "\n", "ATK: ", e1.ATK,
              "\n", "ARMOR: ", e1.ARM)
        #Player's stats
        time.sleep(0.5)
        print("\nYour stats:", "\n", "\n", "HP: ", p1.HP, "\n", "ATK:", p1.ATK,
              "\n", "ARMOR: ", p1.ARM, "\n")
        print("'a' to Attack\n'm' to use Magic\n's' to surrender")
        #Combat option input - Attack, Magic, Surrender
        combatOpt = input("What's your move?\n>")
        #Attack selection
        if combatOpt == 'a' or combatOpt == 'A':
            atkM = random.randint(0, p1.ATK)
            atkDMG = int(p1.ATK + atkM)
            atkDMG -= int(e1.ARM / 10)
            e1.HP -= atkDMG
            print("Your attack hit! You did", atkDMG,
                  "damage. The enemy's hp is now", e1.HP)
            time.sleep(0.5)
            if e1.HP > 0:
                eAtkDMG = e1.ATK
                eAtkDMG -= p1.ARM
                p1.HP -= eAtkDMG
                print(e1.Name, "Hit you for", eAtkDMG, "Damage")
        #Magic Selection
        elif (combatOpt == 'm' or combatOpt == 'M'):
            combatOpt = input("Fireball 'f' or Heal Spell 'h': ")
            if (combatOpt == 'h' and p1.HP < 50
                    or combatOpt == 'H' and p1.HP < 50):
                #Heal Spell
                    p1.HP += random.randint(p1.MGC+10,p1.MGC+15)
                    print("You Healed Yourself to",p1.HP, "HP. You brace yourself for the enemy's attack")
                    time.sleep(0.5)
                    p1.HP -= int(e1.ATK / 2)
                    print("The enemy did", int(e1.ATK / 2), "damage to you")
            elif (combatOpt == 'f' or combatOpt == 'F'):
                print("You cast fireball!")
                time.sleep(0.5)
                e1.HP -= p1.MGC + random.randint(10,15)
                print("Hit! The enemy is at", e1.HP)
                if e1.HP > 0:
                    p1.HP -= e1.ATK
                    time.sleep(0.5)
                    print(e1.Name, "Hit you for", e1.ATK, "Damage")
        elif combatOpt == 's' or combatOpt == 'S':
            print("You throw your hands up in defeat")
            eSurrender = random.randint(0, 1)
            if eSurrender == 0:
                print(e1.Name, "Let's you go but takes some of your gold")
                monREM = random.randint(10, 20)
                p1.MON -= monREM
                if p1.MON < 0:
                    p1.MON = 0
                print(e1.Name, "took", monREM,
                      "coins from you. you are now at", p1.MON)
                inCombat = 0
                Ready()
            else:
                sFail = input(
                    "The enemy didn't accept your surrender. Continue y/n: ")
                if sFail == 'y' or sFail == 'Y':
                    os.system('clear')

        #Alive determiner
        if e1.HP <= 0:
            e1.Alive = 0
        if p1.HP <= 0:
            p1.Alive = 0
            GameOver()
    #Kill rewards
    if e1.Alive == 0:
        os.system('clear')
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
            xpGain = 999
        elif e1.encType == 71:
            xpGain = 12
            monGain = random.randint(12, 24)
        elif e1.encType == 80:
            xpGain = 50
            monGain = 100
        elif e1.encType == 81:
            xpGain = 50
            monGain = 100
        else:
            print("ERROR. YOU FORGOT TO ADD ANOTHER ENCTYPE TO THE LIST")
        p1.XP += xpGain
        p1.MON += monGain
        print("You gained", xpGain, "Xp!, You are now at", p1.XP, "XP")
        p1.Experience()
        print("You gained", monGain, "Gold Coins!, You are now at", p1.MON,
              "Gold")
        inCombat = 0
        if location != 5:
          Ready()
        else:
          print()


def GameOver():
    if p1.Alive == 0:
        print(
            "██╗   ██╗ ██████╗ ██╗   ██╗    ██████╗ ███████╗██████╗ ██╗███████╗██╗  ██╗███████╗██████╗\n╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██╔════╝██╔══██╗██║██╔════╝██║  ██║██╔════╝██╔══██╗\n ╚████╔╝ ██║   ██║██║   ██║    ██████╔╝█████╗  ██████╔╝██║███████╗███████║█████╗  ██║  ██║\n  ╚██╔╝  ██║   ██║██║   ██║    ██╔═══╝ ██╔══╝  ██╔══██╗██║╚════██║██╔══██║██╔══╝  ██║  ██║\n   ██║   ╚██████╔╝╚██████╔╝    ██║     ███████╗██║  ██║██║███████║██║  ██║███████╗██████╔╝\n   ╚═╝    ╚═════╝  ╚═════╝     ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝"
        )
        print("You were killed by", e1.Name)
        redo = input("Retry? y/n: ")
        if redo == 'y' or redo == 'Y':
            os.system('clear')
            resetVar()
            StrtSQ()



def EnterSmith():
    global currWeap, currMGC, currARM
    print("You go to the blacksmith")
    print_slow(
        "The intense heat from the forge causes you to take a slight step backward.\n"
    )
    print(
        "Blacksmith: 'Well come on in boy. Dont let the flies in.'\n'Go ahead and look at the wares'.\n"
    )
    time.sleep(2)
    if blStSwrd[3] == True:
        print("Steel Sword (10 ATK) - Price 20 Gold - Enter '1'\n")
    if blIrMace.count(True) == 1:
        print("Iron Mace (15 ATK) - Price 30 Gold - Enter '2'\n")
    if blBaStaff.count(True) == 1:
        print("Basic Wooden Staff (5 MGC) - Price 20 Gold - Enter '3'\n")
    if blChArmor[3] == True:
        print("Chainmail Armor Suit (5 Armor) - Price 20 Gold - Enter '4'\n")
    print("You have", p1.MON, "coins")
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

    print_slow(
        "You Enter the buther's shop, the smell of meat makes your eyes water\n"
    )
    if p1.pigGot == True:
        print_slow(
            "Butcher: MY PIG! WHAT ARE YOU DOING WITH HIM! I KNEW SOMEBODY TOOK IT!\nYou quickly explain that randomly encountered the pig.\n\nYou give him the pig.\n\nButcher: Thank you, she's my prized pig. If I lost the damn thing I wouldnt be able to afford my tax.\nButcher: Here, I'll give you a portion of the money as a thank you"
        )
        monGain = 20
        p1.MON += monGain
        p1.pigGot = False
        butchPig = True
        print("You gained", monGain, "coins for returning the pig")
    else:
        print_slow(
            "You see the butcher looking stressed and ask him what's the matter\n\nButcher: Ah I've lost 'er, I know somebody stole her.\n\nYou talk about your own partner that left you, nearly breaking into a sob.\n\nButcher: Oh me boy, I don't mean a human I mean my pig.\n\nYou Look at him with disgust and he quickly realizes the scenario\n\nButcher: No not like that! I mean my prized pig has gotten out and If i can't sell her I wont be able to afford tax.\n"
        )
        butchPig = False
    print("Butcher: Anyways, please have a look around!\n\nYou have", p1.MON,
          "coins")
    if butchPig == True:
        print("Prized porkchop - price: 40 - enter 'p' (Food will increase your healing ability in battle)")
    else:
        print(
            "Butcher: Oh wait no. I'm out of stock! the butcher starts to wail and you leave"
        )


def Villagers():
    print("You walk up to a group of villagers")
    if p1.villGot == True:
        print(
            "Villager 2: OH JACKIE YOU'RE BACK!\nVillager 1: Jackie!"
        )
        print("The group of villagers leave.")
        XPgain = 100
        p1.XP += XPgain
        p1.Experience()
        p1.villGot = False
    else:
      print_slow("Villager 1: Oh hey.\nVillager 2: You look like you need bandages.\nVillager 1: We sell.\nVillager 2: Yes! We sell bandages!\nVillager 1: You need.\nVillager 2: 10 coins for 1 bandage which is 5 health.\nVillager 1: 10 coins.")
      print("\nYou have %s coins" % (p1.MON))
      buyHp = int(input("\nHow many bandages would you like to buy"))
      x = p1.MON
      for i in range(buyHp):
        x -= 10
        print (x)
      if x >= 0:
        p1.MON = x
        print("You bought %s bandages. You are now at %s Health and %s coins" % (buyHp,p1.HP,p1.MON))
        print_slow("Villager 1: Very Good.\nVillager 2: We've done it! We made a sale. If only Jackie was here\nVillager 1: Oh no\nVillager 2 breaks into a sob and you decide to leave them alone")
        global location
        location = 4
      else:
        print("Villager 1: tsk\nVillager 2: You do not have enough money to buy that many\nVillager 1: Not Enough!")


resetVar()
StrtSQ()
