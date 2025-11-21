from weapon import FISTS
from healthbar import HealthBar

class Character:
    def __init__(self, name: str, hp: int, weapon=FISTS) -> None:
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.weapon = weapon

    def attack(self, target) -> None:
        target.hp = max(target.hp - self.weapon.dmg, 0)

class Hero(Character):
    def __init__(self, name: str, hp: int, weapon=FISTS) -> None:
        super().__init__(name, hp, weapon)
        self.default_weapon = weapon
        self.healthbar = HealthBar(self, color="green")

    def equip(self, weapon) -> None:
        self.weapon = weapon

    def drop(self) -> None:
        self.weapon = self.default_weapon

class Enemy(Character):
    def __init__(self, name: str, hp: int, weapon=FISTS) -> None:
        super().__init__(name, hp, weapon)
        self.healthbar = HealthBar(self, color="red")
