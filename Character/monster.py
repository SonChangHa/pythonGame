from .character import Character

class Monster(Character):
    def __init__(self, name, hp, ad, dp, exp, gold):
        super().__init__(name, hp, ad, dp)
        self.exp = exp
        self.gold = gold