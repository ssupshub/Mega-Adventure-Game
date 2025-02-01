import random
import time
from game.character import Character, Enemy
from game.location import Location
from game.inventory import Inventory

class Game:
    def __init__(self):
        self.player = None
        self.enemy = None
        self.locations = Location()
        self.inventory = Inventory()

    def start(self):
        print("Welcome to the Mega Adventure Game!")
        player_name = input("Enter your character's name: ")
        self.player = Character(player_name, 100, 15, 5)
        self.current_location = self.locations.random_location()
        print(f"\n{self.player.name} begins their adventure in the {self.current_location}...\n")
        self.game_loop()

    def game_loop(self):
        while self.player.is_alive():
            print(f"\nCurrent Location: {self.current_location}")
            self.display_options()

            choice = input("\nWhat will you do? (Move/Inventory/Exit): ").lower()

            if choice == 'move':
                self.move()
            elif choice == 'inventory':
                self.player.show_inventory()
            elif choice == 'exit':
                print("Exiting game...")
                break
            else:
                print("Invalid choice. Try again.")

    def display_options(self):
        print("\nOptions:")
        print("1. Move to another location")
        print("2. Check Inventory")
        print("3. Exit Game")

    def move(self):
        print("\nYou travel through the wilderness...")
        time.sleep(1)

        if random.random() < 0.5:
            self.encounter_enemy()
        else:
            self.find_item()

    def encounter_enemy(self):
        enemy_name = random.choice(['Goblin', 'Orc', 'Dragon', 'Troll'])
        enemy_hp = random.randint(20, 80)
        enemy_attack = random.randint(5, 20)
        enemy_defense = random.randint(0, 5)
        self.enemy = Enemy(enemy_name, enemy_hp, enemy_attack, enemy_defense)

        print(f"\nA wild {self.enemy.name} appears!\n")
        self.fight_enemy()

    def fight_enemy(self):
        while self.enemy.is_alive() and self.player.is_alive():
            print(f"\n{self.enemy.name} HP: {self.enemy.hp}")
            print(f"{self.player.name} HP: {self.player.hp}")
            action = input("\nWhat will you do? (Attack/Heal/Run): ").lower()

            if action == 'attack':
                self.player.attack_enemy(self.enemy)
                if self.enemy.is_alive():
                    self.enemy.attack_enemy(self.player)
            elif action == 'heal':
                if 'Healing Potion' in self.player.inventory:
                    self.player.heal(20)
                    self.player.inventory.remove('Healing Potion')
                else:
                    print("You don't have any healing items!")
            elif action == 'run':
                print(f"{self.player.name} runs away from the fight!")
                break
            else:
                print("Invalid action. Try again.")

        if not self.player.is_alive():
            print(f"{self.player.name} has been defeated!")
        elif not self.enemy.is_alive():
            print(f"{self.enemy.name} has been defeated!")
            self.player.add_item(random.choice(self.inventory.items))
            print(f"You found a {self.player.inventory[-1]}!")

    def find_item(self):
        item = random.choice(self.inventory.items)
        print(f"\nYou found a {item}!")
        self.player.add_item(item)
