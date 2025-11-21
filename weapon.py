class Weapon:
    def __init__(self, name: str, wtype: str, dmg: int, val: int) -> None:
        self.name = name
        self.wtype = wtype
        self.dmg = dmg
        self.val = val

FISTS = Weapon("Fists", "blunt", 2, 0)
IRON_SWORD = Weapon("Iron Sword", "sharp", 5, 10)
SHORT_BOW = Weapon("Short Bow", "ranged", 4, 8)
