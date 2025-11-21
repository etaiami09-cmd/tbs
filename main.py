from character import Hero, Enemy
from weapon import IRON_SWORD
import os
import sys

hero = Hero("Hero", 100)
hero.equip(IRON_SWORD)
# uncomment the below line to make the hero use fists
# hero.drop()

enemy = Enemy("Enemy", 100)

while True:
    os.system("clear") # or 'cls' instead of 'clear' on Windows

    hero.attack(enemy) # attack loop starts with hero
    
    enemy.attack(hero) # enemy immediately counter-attacks

    # redraw updated healthbars after each exchange
    hero.healthbar.draw()
    enemy.healthbar.draw()

    print("\nPress Enter key to fight or Ctrl+D/C to exit.")

    try:
        input()
    except EOFError:
        print("\nSIGTERM received. Exiting.")
        sys.exit(0)
    except KeyboardInterrupt:
        print("\nSIGINT received. Exiting.")
        sys.exit(0)
