class Armor:

    def __init__(self, name, dp, gold):
        self.name = name
        self.dp = dp
        self.gold = gold

    @classmethod
    def armor_equip(cls, player, armor):
        # for _ in range(50):
        # print("")

        player.dp -= player.armor.dp
        print(f"{player.armor.name}가 해제되었습니다.")
        player.armor_list.append(player.armor)
        player.armor = None

        player.dp += armor.dp
        print(f"{armor.name}가 장착되었습니다.")
        player.armor = armor
        player.armor_list.pop(player.armor_list.index(armor))
