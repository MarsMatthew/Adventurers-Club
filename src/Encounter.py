import random


class Encounter:
    HP = 0
    ATK = 0
    ARM = 0
    hostile = 0
    Name = ""
    enc = random.randint(0,2)
    encType = random.randint(0, 9)

    #constructor
    def __init__(self):
       self.HP = 0
       self.ATK = 0
       self.ARM = 0
       self.enc = random.randint(0,2)

    def typeFind(self):
        if self.enc == 0:
            if self.encType == 0:
                self.Name = "Bag o' gold"
                self.hostile = 0
            elif self.encType == 1:
                self.Name = "Lost Villager"
                self.hostile = 0
            elif self.encType == 2:
                self.Name = "Old man"
                self.hostile = 0
            elif self.encType == 3:
                self.Name = "A Pig"
                self.hostile = 0
            elif self.encType == 4:
                self.HP = 50
                self.ARM = 15
                self.ATK = 4
                self.hostile = 1
                self.Name = "bob"
            elif self.encType == 5:
                self.HP = 60
                self.ARM = 10
                self.ATK = 3
                self.hostile = 1
                self.Name = "Pirate"
            elif self.encType == 6:
                self.HP = 75
                self.ARM = 30
                self.ATK = 1
                self.hostile = 1
                self.Name = "lard"
            elif self.encType == 7:
                self.HP = 30
                self.ARM = 5
                self.ATK = 7
                self.hostile = 1
                self.Name = "Tiny Tim"
            elif self.encType == 8:
                self.HP = 50
                self.ARM = 14
                self.ATK = 4
                self.hostile = 1
                self.Name = "Terrible Tom"
            elif self.encType == 9:
                self.HP = 56
                self.ARM = 15
                self.ATK = 4
                self.hostile = 1
                self.Name = "police"
