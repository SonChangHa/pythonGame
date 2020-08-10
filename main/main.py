from Character import player, monster, NPC
from equip_item import armor, weapon
import random

player = player.Player('김용사', 100, 10, 10, 10)
monster1 = monster.Monster("주황버섯", 50, 5, 5, 10, 1000)

npc = NPC.NPC()

noarmor = armor.Armor("맨몸", 0, 0)
noweapon = weapon.Weapon("맨손", 0, 0)

justarmor = armor.Armor("쌘몸", 10, 1000)
justweapon = weapon.Weapon("쌘손", 10, 1000)

goodarmor = armor.Armor("짱쌘몸", 50, 10000)
goodweapon = weapon.Weapon("짱쌘손", 50, 10000)

npc.store_armor_list.append(justarmor)
npc.store_armor_list.append(goodarmor)
npc.store_weapon_list.append(justweapon)
npc.store_weapon_list.append(goodweapon)

player.armor = noarmor
player.weapon = noweapon

print("게임 시작")

while True:
    print("던전 입장 : 1, 상점 : 2, 휴식 : 3, 정보 보기 : 4")

    k = input()

    if k == '1':
        st = 0
        print("던전에 입장합니다.")
        player.incounter(monster1)
        st += 1
        monster1.name = f"{monster1.name} 강화+{st}"
        monster1.hp += 50
        monster1.nowhp = monster1.hp
        monster1.ad += 10
        monster1.dp += 10
        monster1.exp += 50
        monster1.gold += 1000
    elif k == '2':
        print("상점에 입장합니다.")
        npc.store(player)
    elif k == '3':
        if player.gold >= 50:
            print("돈을 내고 휴식을 취합니다")
            player.gold -= 50
        else:
            print("돈이 없습니다!")
    elif k == '4':
        player.show_menu()
    else:
        print("잘못된 입력!")



