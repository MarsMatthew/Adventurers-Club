import random


class Encounter:
    HP = 0
    ATK = 0
    ARM = 0
    hostile = 0
    Name = ""
    #enc = random.randint(0,1)
    encType = random.randint(0, 13)
    Alive = 1

    #constructor
    def __init__(self):
       self.HP = 0
       self.ATK = 0
       self.ARM = 0
       #self.enc = random.randint(0,1)
       self.encType = random.randint(0,15)
       self.Alive = 1

    def typeFind(self):
        #if self.enc == 0:
            if self.encType == 0:
                self.Name = "Bag o' gold"
                self.hostile = 0
            elif self.encType == 1:
                self.Name = "Lost Villager"
                self.hostile = 0
            elif self.encType == 2:
                self.Name = "Old man"
                self.HP = 999
                self.ATK = 999
                self.ARM = 999
                self.hostile = 0
            elif self.encType == 3:
                self.Name = "A Pig"
                self.hostile = 0
            elif self.encType == 4:
                self.HP = 20
                self.ARM = 15
                self.ATK = 4
                self.hostile = 1
                self.Name = "Strong Man Bob"
            elif self.encType == 5:
                self.HP = 40
                self.ARM = 10
                self.ATK = 3
                self.hostile = 1
                self.Name = "A Pirate"
            elif self.encType == 6:
                self.HP = 55
                self.ARM = 30
                self.ATK = 1
                self.hostile = 1
                self.Name = "A Tub of Lard"
            elif self.encType == 7:
                self.HP = 10
                self.ARM = 5
                self.ATK = 7
                self.hostile = 1
                self.Name = "Tiny Tim"
            elif self.encType == 8:
                self.HP = 30
                self.ARM = 14
                self.ATK = 4
                self.hostile = 1
                self.Name = "Terrible Tom"
            elif self.encType == 9:
                self.HP = 36
                self.ARM = 15
                self.ATK = 4
                self.hostile = 1
                self.Name = "Maniac Mark"
            elif self.encType >= 10 and self.encType < 16:
                self.hostile = 2
            elif self.encType == 70:
                print("OH NO! The chest was actually a mimic!")
                self.hostile = 1
                self.Name = "The Mimic"
                self.HP = 30
                self.ATK = 10
                self.ARM = 20
            elif self.encType == 71:
              self.hostile = 1
              self.HP = 40
              self.ATK = 15
              self.ARM = 0
              self.Name = "A Dozen or so rats"
            elif self.encType == 80:
              self.hostile = 1
              self.HP = 50
              self.ATK = 40
              self.ARM = 0
              self.Name = "Forest Abomination"
            elif self.encType == 81:
              self.hostile = 1
              self.HP = 100
              self.ATK = 15
              self.ARM = 0
              self.Name = "Lake Abomination"
            elif self.encType == 100:
              self.hostile = 1
              self.HP = 100
              self.ATK = 20
              self.ARM = 0
              self.Name = "World's Abomination"
