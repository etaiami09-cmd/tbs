from weapon import FISTS
from healthbar import HealthBar

class Character:
    def __init__(self, name: str, hp: int, weapon=FISTS) -> None:
        # basic shared fields for all character types
        self.name = name
        self.hp = hp
        self.max_hp = hp
        # starting weapon, default is fists
        self.weapon = weapon

    def attack(self, target) -> None:
        # simple damage application with floor at zero
        target.hp = max(target.hp - self.weapon.dmg, 0)

class Hero(Character):
    def __init__(self, name: str, hp: int, weapon=FISTS) -> None:
        super().__init__(name, hp, weapon)
        # store original weapon so drop() can revert to it
        self.default_weapon = weapon
        # hero healthbar uses green
        self.healthbar = HealthBar(self, color="green")

    def equip(self, weapon) -> None:
        # change current weapon
        self.weapon = weapon

    def drop(self) -> None:
        # go back to default weapon
        self.weapon = self.default_weapon

class Enemy(Character):
    def __init__(self, name: str, hp: int, weapon=FISTS) -> None:
        super().__init__(name, hp, weapon)
        # enemy healthbar marked in red
        self.healthbar = HealthBar(self, color="red")
