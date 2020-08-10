class Character:
    #hp = 0
    #mp = 0
    #ad = 0
    #dp = 0
    #nowhp = hp
    #nowmp = mp

    def __init__(self,name,hp,ad,dp):
        self.name = name
        self.hp = hp
        self.ad = ad
        self.dp = dp
        self.nowhp = hp


    def att(self, character):
        if character.dp >= self.ad:
            character.nowhp -= 1
            print("-1!!!")
        else:
            character.nowhp -= self.ad - character.dp
            print(f"-{self.ad - character.dp}!!!")

    
