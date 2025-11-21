class Weapon:
    def __init__(self, name: str, wtype: str, dmg: int, val: int) -> None:
        # weapon data container
        self.name = name
        self.wtype = wtype
        self.dmg = dmg
        self.val = val

# default option
FISTS = Weapon("Fists", "blunt", 2, 0)

# melee weapon
IRON_SWORD = Weapon("Iron Sword", "sharp", 5, 10)

# ranged weapon with moderate damage
SHORT_BOW = Weapon("Short Bow", "ranged", 4, 8)
