from weapon import fists
from health_bar import HealthBar

class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.max_health = health

        self.weapon = fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.healt_bar.update()
        print(f'{self.name} dealt {self.weapon.damage} with {self.weapon.name} to {target.name}')
        
class Hero(Character):
    def __init__(self, name: str, health: int):
        super().__init__(name=name, health=health)
        self.default_weapon = self.weapon
        self.healt_bar = HealthBar(self, color="green")
        
    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped {self.weapon.name}")
        
    def drop(self) -> None:
        print(f"{self.name} dropped {self.weapon.name}")
        self.weapon = self.default_weapon

class Enemy(Character):
    def __init__(self, name: str, health: int, weapon):
        super().__init__(name=name, health=health)
        self.healt_bar = HealthBar(self, color="red")
        self.weapon = weapon