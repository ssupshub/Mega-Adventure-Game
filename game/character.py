class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.inventory = []

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        print(f"{self.name} healed for {amount} HP.")

    def attack_enemy(self, enemy):
        damage = max(self.attack - enemy.defense, 0)
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")
        enemy.take_damage(damage)

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        if not self.inventory:
            print(f"{self.name}'s inventory is empty.")
        else:
            print(f"{self.name}'s Inventory: " + ", ".join(self.inventory))


class Enemy(Character):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
