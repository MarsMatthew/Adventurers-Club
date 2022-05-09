class Shops:
    blStSwrd = True
    blIrMace = True
    blBaStaff = True
    blChArmor = True

    def __init__(self):
        self.blStSwrd = ['Steel Sword',10,20]
        self.blIrMace = True
        self.blBaStaff = True
        self.blChArmor = True

    def EnterSmith(self,MON,currWeap):
        print("You go to the blacksmith")
        print(
            "The intense heat from the forge causes you to take a slight step backward."
        )
        print(
            "Blacksmith: 'Well come on in boy. Dont let the flies in.'\n'Go ahead and look at the wares'."
        )
        print(self.blStSwrd)
        if self.blIrMace == True: print("Iron Mace (15 ATK) - Price 30 Gold - Enter '2'")
        if self.blBaStaff == True:
            print("Basic Wooden Staff (5 MGC) - Price 20 Gold - Enter '3'")
        if self.blChArmor == True:
            print("Chainmail Armor Suit (5 Armor) - Price 20 Gold - Enter '4'")
        shopChoice = input("What do you want to buy?\n>")
        if shopChoice == '1':
          if MON >= 20:
            if currWeap == "":
              print("Steel Sword Got")
              currWeap = self.blStSwrd
              print("BEFORE:",MON)
              MON -= 20
              print ("AFTERINBLACKSMITH:", MON)
            else:
              print("You have to sell your current weapon before you can buy this")
              #Sell()
          elif MON < 20:
            print("Pah! I want real money now get out of here.")

#Food or something Shop

#Butchers shop
#def Sell(self,MON,currWeap):
