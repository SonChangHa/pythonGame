class Weapon:
    def __init__(self, name, ad, gold):
        self.name = name
        self.ad = ad
        self.gold = gold

    @classmethod
    def weapon_equip(cls, player, weapon):
        #for _ in range(50):
            #print("")

        player.ad -= player.weapon.ad
        print(f"{player.weapon.name}가 해제되었습니다.")
        player.weapon_list.append(player.weapon)
        player.weapon = None

        player.ad += weapon.ad
        print(f"{weapon.name}가 장착되었습니다.")
        player.weapon = weapon
        player.weapon_list.pop(player.weapon_list.index(weapon))

