from character import Hero, Enemy
from weapon import IRON_SWORD
import os

hero = Hero("Hero", 100)
hero.equip(IRON_SWORD)
# uncomment the below line to make the hero use fists
# hero.drop()

enemy = Enemy("Enemy", 100)

while True:
    # change 'clear' to 'cls' on windows systems
    os.system("clear")

    # attack loop starts with hero
    hero.attack(enemy)
    # enemy immediately counter-attacks
    enemy.attack(hero)

    # redraw updated healthbars after each exchange
    hero.healthbar.draw()
    enemy.healthbar.draw()

    # pause to see the results before continuing
    input()
