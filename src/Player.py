class Player:
  Name = input("What is your name:")
  HP = 50
  ATK = 5
  ARM = 0
  MGC = 0
  MON = 0
  XP = 0
  pigGot = 0
  villGot = 0
  oldEnc = 0
  Alive = 1
  currWeap = ""
  def __init__(self):
    self.HP = 50
    self.ATK = 5
    self.ARM = 0
    self.MGC = 0
    self.MON = 0
    self.XP = 0
    self.Alive = 1
    self.pigGot = 0
    self.villGot = 0
    self.oldEnc = 0
    self.currWeap = ""
  def Inventory(self):
    print(self.currWeap)
    #List with names of weapons player gets. starts w/ nothing or just "fists" Everytime player gets something it is appended in the list. Maybe whenever player achieves something a function called inventory is run to update ATK MGC or ARM. NEED TO BE ABLE TO FIND SOMETHING IN THE LIST AND THEN POSSIBLY REMOVE IT.
    #Better option: Player can only have one weapon, one magic weapon, one armor.
  #def Personal(self):
    