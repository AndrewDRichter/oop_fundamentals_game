from character import Hero, Enemy
from weapon import short_bow, iron_sword
import os


hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

if __name__ == "__main__":
    while True:
        os.system("cls")
        
        hero.attack(enemy)
        enemy.attack(hero)

        hero.healt_bar.draw()
        enemy.healt_bar.draw()
        hero.drop()

        input()