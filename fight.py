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

def start_battle(hero1: Warrior, hero2: Mage):
    print(f"--- THE BATTLE BEGINS! {hero1.name} VS {hero2.name} ---")
    while hero1.is_alive() and hero2.is_alive():
        hero1.attack(hero2)
        if hero2.is_alive():
            hero2.attack(hero1)
    if hero1.is_alive():
        print(f'{hero1.name} wins!')
    else:
        print(f'{hero2.name} wins!')

war = Warrior("Kop",100,40)
mage = Mage("Zin", 100, 30)

start_battle(war, mage)
