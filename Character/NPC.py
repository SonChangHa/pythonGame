class NPC:

    store_weapon_list = []
    store_armor_list = []

    def store(self, player):
        print("무기 구매 : 1, 방어구 구매 : 2, 돌아가기 : 기타")
        k = input()

        if k == '1':
            while True:
                i = 0
                print("사고 싶은 무기의 숫자를 입력해줘!")
                for t in self.store_weapon_list:
                    i += 1
                    print(f"{i} : {t.name}, 추가 공격력 : {t.ad}, 가격 : {t.gold}")
                k = int(input())
                if k > 0 and k <= i:
                    if player.gold >= self.store_weapon_list[k - 1].gold:
                        player.gold -= self.store_weapon_list[k - 1].gold
                        player.weapon_list.append(self.store_weapon_list.pop(k - 1))
                        print("거래 고마워!")
                    else:
                        print("돈이 모자란걸?")
                else:
                    break



        elif k == 2:
            while True:
                i = 0
                print("사고 싶은 방어구의 숫자를 입력해줘!")
                for t in self.store_armor_list:
                    i += 1
                    print(f"{i} : {t.name}, 추가 방어력 : {t.dp}, 가격 : {t.gold}")
                k = int(input())
                if k > 0 and k <= i:
                    if player.gold >= self.store_armor_list[k - 1].gold:
                        player.gold -= self.store_armor_list[k - 1].gold
                        player.armor_list.append(self.store_armor_list.pop(k - 1))
                        print("거래 고마워!")
                    else:
                        print("돈이 모자란걸?")
                else:
                    break
        else:
            print("또 와!")
            return