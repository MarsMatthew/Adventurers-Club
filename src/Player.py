class Player:
  Name = ""
  HP = 50
  ATK = 5
  ARM = 0
  MGC = 0
  MON = 0
  XP = 0
  LVL = 1
  pLVL = 0
  pigGot = 0
  villGot = 0
  oldEnc = 0
  Alive = 1
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
    self.Name = ""
    self.LVL = 1
    self.pLVL = 0
  def Experience(self):
    if self.XP >= 50 and self.LVL >= self.pLVL:
      self.XP -= 50
      self.LVL += 1
      print ("Level up! You are now level,", self.LVL)
  def Inventory(self,currWeap,currARM,currMGC):
    self.ATK = currWeap[1]
    self.ARM = currARM[1]
    self.MGC = currMGC[1]
    self.ATK += self.LVL
    self.MGC += self.LVL