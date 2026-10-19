import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, amount: int):
        self.health = max(0, self.health - amount)

    def attack(self, other):
        other.take_damage(self.attack_power)
        return f'{self.name} attacks {other.name} with {self.attack_power} damage.'

class Warrior(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.health += 20

    def take_damage(self, amount: int):
        self.health = int(max(0, self.health - (amount - (amount * 0.1))))

class Mage(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.attack_power += 20

class Archer(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.dodge_chance = 0.2

    def take_damage(self, amount: int):
        if random.random() < self.dodge_chance:
            print("Archer dodged!")
        else:
            self.health = max(0, self.health - amount)

def start_battle(hero1: Mage, hero2: Archer):
    print(
        f"--- THE BATTLE BEGINS! "
        f"{hero1.name}-{hero1.health}hp VS "
        f"{hero2.name}-{hero2.health}hp ---"
    )
    while hero1.is_alive() and hero2.is_alive():
        print(hero1.attack(hero2))
        print(
            f"{hero1.name} - {hero1.health}hp. "
            f"{hero2.name} - {hero2.health}hp."
        )
        if not hero2.is_alive():
            break

        print(hero2.attack(hero1))
        print(
            f"{hero1.name} - {hero1.health}hp. "
            f"{hero2.name} - {hero2.health}hp."
        )

    if hero1.is_alive():
        print(f'{hero1.name} wins!')
    else:
        print(f'{hero2.name} wins!')

war = Warrior("Kop",100,10)
mage = Mage("Zin", 100, 10)
arch = Archer("joe", 100, 20)

start_battle(mage, arch)
