from character import Hero, Enemy
from weapon import short_bow, iron_sword
import os


hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

def draw_menu():
    os.system("cls")
    hero.healt_bar.draw()
    enemy.healt_bar.draw()

if __name__ == "__main__":
    while True:
        # Interface
        draw_menu()
        
        # Combat
        hero.attack(enemy)
        enemy.attack(hero)
        hero.drop()

        # User input?
        input()