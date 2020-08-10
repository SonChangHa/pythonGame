from .character import Character
from equip_item.armor import Armor
from equip_item.weapon import Weapon
from sys import exit

class Player(Character):


	weapon = None
	weapon_list = []
	armor = None
	armor_list = []

	def __init__(self,name,hp,ad,dp,exp):
		super().__init__(name,hp,ad,dp)
		self.exp = exp
		self.nowexp = 0
		self.level = 1
		self.gold = 100

	def show_menu(self):
		for _ in range(50):
			print()

		print(f"────────────────────────────────────────")
		print(f"플레이어의 이름 : {self.name}")
		print(f"레벨 : {self.level}")
		print(f"체력 : {self.nowhp} / {self.hp}")
		print(f"공격력 : {self.ad}, 방어력 : {self.dp}")
		print(f"경험치 : {self.nowexp} / {self.exp}")
		print(f"골드 : {self.gold}")
		print(f"────────────────────────────────────────")
		print(f"아이템 : 1, 돌아가기 : 기타")
		k1 = input()
		if k1 == "1":
			print(f"무기 : 1, 방어구 : 2, 포션 : 3, 맵으로 돌아가기 : 기타 숫자")
			k2 = input()
			if k2 == '1':
				self.show_weapon()
			elif k2 == '2':
				self.show_armor()
			#elif k2 == '3':
				#self.show_portion()
			else:
				return
		else:
			return

	def show_weapon(self):
		while True:
			i = 0
			print(f"────────────────────────────────────────")
			print(f"현재 장착중인 무기 : {self.weapon.name}")
			print(f"추가 공격력 : {self.weapon.ad}")
			print(f"────────────────────────────────────────")

			print(f"────────────────────────────────────────")
			for t in self.weapon_list:
				i += 1
				print(f"{i} : {t.name}, 추가 공격력 : {t.ad}")
			print(f"────────────────────────────────────────")

			print(f"무기를 장착하고 싶으시면 숫자를 입력해주세요.")
			print(f"이외의 숫자를 입력할시 돌아갑니다.")
			k = int(input())
			if k > 0 and k <= i:
				Weapon.weapon_equip(self, self.weapon_list[k-1])
			else:
				break

	def show_armor(self):
		while True:
			i = 0
			print(f"────────────────────────────────────────")
			print(f"현재 장착중인 방어구 : {self.armor.name}")
			print(f"추가 방어력 : {self.armor.dp}")
			print(f"────────────────────────────────────────")

			print(f"────────────────────────────────────────")
			for t in self.armor_list:
				i += 1
				print(f"{i} : {t.name}, 추가 방어력 : {t.dp}")
			print(f"────────────────────────────────────────")

			print(f"방어구를 장착하고 싶으시면 숫자를 입력해주세요.")
			print(f"이외의 숫자를 입력할시 돌아갑니다.")
			k = int(input())
			if k > 0 and k <= i:
				Armor.armor_equip(self, self.armor_list[k-1])
			else:
				break

	def incounter(self, monster):
		print(f"{monster.name}와 만났습니다!")

		while True:
			print(f"공격 : 1, 도주 : 2")
			k = input()

			if k == '1':
				print(f"플레이어의 공격!")
				self.att(monster)
				print(f"{monster.name}의 체력은 {monster.nowhp} / {monster.hp}입니다.")
				if monster.nowhp <= 0:
					print(f"물리쳤습니다!")
					self.nowexp += monster.exp
					self.levelup()
					self.gold += monster.gold
					return
				else:
					print("")
					print(f"{monster.name}의 공격!")
					monster.att(self)
					print(f"플레이어의 체력은 {self.nowhp} / {self.hp}입니다.")
					if self.nowhp < 0:
						print("죽었습니다.")
						exit()
			elif k == '2':
				print("도망쳤습니다!")
				return



	def levelup(self):
		while self.nowexp >= self.exp:
			print("레벨업!")
			self.level += 1
			self.nowexp -= self.exp
			self.exp += 50
			self.nowhp = self.hp
			self.ad += 5
			self.dp += 5



