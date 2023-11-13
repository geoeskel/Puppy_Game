import random

class PuppyGame:
    def __init__(self):
        self.strength = 10
        self.wisdom = 10
        self.hunger = 0  # 0 is not hungry, 100 is very hungry
        self.age = 0
        self.foods_eaten = 0
        self.animals_met = 0
        self.inventory = []
        self.xp = 0
        self.level = 1
        self.challenges = {"meet_all_animals": False, "find_special_item": False}
        self.special_items = ["magic bone", "golden leaf"]
        self.health = 100
        self.energy = 100

    def adjust_health(self, amount):
        self.health = max(0, min(100, self.health + amount))
        if self.health == 0:
            print("Your health has dropped to 0. Be careful!")

    def adjust_energy(self, amount):
        self.energy = max(0, min(100, self.energy + amount))
        if self.energy == 0:
            print("You are out of energy. You need to rest or eat something!")

    def check_challenges(self):
        if not self.challenges["meet_all_animals"] and self.animals_met >= 4:  # Assuming 4 different animals
            self.challenges["meet_all_animals"] = True
            self.reward_challenge("meet_all_animals")

        if not self.challenges["find_special_item"] and any(item in self.special_items for item in self.inventory):
            self.challenges["find_special_item"] = True
            self.reward_challenge("find_special_item")

    def reward_challenge(self, challenge):
        if challenge == "meet_all_animals":
            self.strength += 5
            self.wisdom += 5
            print("Challenge completed: Meet all animals! Your strength and wisdom have increased.")
        elif challenge == "find_special_item":
            self.strength += 10
            self.xp += 20
            print("Challenge completed: Find a special item! You gain strength and bonus XP.")


    def gain_xp(self, amount):
        self.xp += amount
        print(f"You gained {amount} XP.")
        if self.xp >= 10 * self.level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.strength += 2
        self.wisdom += 2
        self.xp = 0
        print(f"Congratulations! You've leveled up to Level {self.level}!")

    def display_status(self):
        print("\nCurrent Status:")
        print(f"Strength: {self.strength}")
        print(f"Wisdom: {self.wisdom}")
        print(f"Hunger: {self.hunger}")
        print(f"Age: {self.age} months")
        print(f"Inventory: {self.inventory}")

    def encounter_animal(self):
        animals = {
        "squirrel": {"description": "A playful squirrel darts in front of you, flicking its tail.", "required_strength": 5, "required_wisdom": 4},
        "wolf": {"description": "You notice a majestic wolf, its eyes gleaming in the forest light.", "required_strength": 15, "required_wisdom": 12},
        "eagle": {"description": "Above you, an eagle soars high, its sharp eyes scanning the ground.", "required_strength": 10, "required_wisdom": 15},
        "bear": {"description": "A large bear lumbers across your path, sniffing the air cautiously.", "required_strength": 20, "required_wisdom": 18},
        "fox": {"description": "A cunning fox with bright, inquisitive eyes sneaks through the underbrush.", "required_strength": 8, "required_wisdom": 10},
        "owl": {"description": "In the moonlit night, a wise old owl perches silently on a tree branch.", "required_strength": 7, "required_wisdom": 14},
        "rabbit": {"description": "A fluffy rabbit hops across your path, its nose twitching adorably.", "required_strength": 3, "required_wisdom": 3},
        "butterfly": {"description": "A colorful butterfly flutters by, its wings a kaleidoscope of colors.", "required_strength": 2, "required_wisdom": 2},
        "badger": {"description": "A gruff badger emerges from its burrow, eyeing you warily.", "required_strength": 12, "required_wisdom": 10}
        }

        animal, attributes = random.choice(list(animals.items()))
        print(f"\n{attributes['description']}")

        if self.strength >= attributes["required_strength"] and self.wisdom >= attributes["required_wisdom"]:
            choice = input(f"Do you want to approach the {animal}? (y/n): ").lower()
            if choice == 'y':
                self.animals_met += 1
                # Define specific interactions and effects for each animal
                print(f"You interact with the {animal}...")
                # Example: Gain XP, strength, wisdom, etc.
            else:
                print(f"You decide to stay away from the {animal}.")
        else:
            print(f"The {animal} seems too daunting to approach right now.")

            self.gain_xp(5)
            self.check_challenges()
            self.adjust_energy(-10)  # Example: encountering an animal costs energy

    def find_food(self):
        foods = ["berries", "meat", "fish"]
        food = random.choice(foods)
        hunger_reduction = random.randint(10, 30)

        print(f"\nYou find some {food}.")
        choice = input("Do you want to eat it? (yes/no): ").lower()
        if choice == 'yes':
            self.foods_eaten += 1
            self.hunger = max(0, self.hunger - hunger_reduction)
            print(f"You eat the {food} and reduce your hunger by {hunger_reduction} points.")
        else:
            print("You decide not to eat the food.")
        
        self.gain_xp(3)
        self.check_challenges()
        self.adjust_energy(20)  # Example: eating food restores energy

    def find_item(self):
        items = {
            "stick": {"strength": 2, "wisdom": 1},
            "feather": {"strength": 1, "wisdom": 2},
            "bone": {"strength": 3, "wisdom": 0}
        }
        item = random.choice(list(items.keys()))
        print(f"\nYou found a {item}!")

        choice = input("Do you want to take it? (yes/no): ").lower()
        if choice == 'yes':
            self.inventory.append(item)
            self.strength += items[item]["strength"]
            self.wisdom += items[item]["wisdom"]
            print(f"The {item} is now in your inventory.")
        else:
            print("You leave the item behind.")
        
        self.gain_xp(4)

    def grow_older(self):
        self.age += 1
        self.hunger += 5  # Getting hungrier as time passes
        if self.age % 3 == 0:
            self.strength += 3
            self.wisdom += 2
            print("\nYou're growing older and wiser!")
    
    def random_event(self):
        events = ["find_mystery_item", "sudden_rain", "friendly_traveler"]
        chosen_event = random.choice(events)
        
        if chosen_event == "find_mystery_item":
            self.find_mystery_item()
        elif chosen_event == "sudden_rain":
            self.sudden_rain()
        elif chosen_event == "friendly_traveler":
            self.friendly_traveler()

    def find_mystery_item(self):
        item = "mysterious artifact"
        self.inventory.append(item)
        print("You found a mysterious artifact lying on the ground and added it to your inventory!")

    def sudden_rain(self):
        print("Suddenly, it starts raining! You feel refreshed and gain some wisdom.")
        self.wisdom += 2

    def friendly_traveler(self):
        print("A friendly traveler passes by and shares some tips with you.")
        self.wisdom += 3
        self.gain_xp(5)

    def explore_area(self):
        print("You explore the area...")
        if random.randint(1, 10) > 7:  # 30% chance of finding something
            self.find_random_item()
        else:
            print("It's a quiet day in the forest. You don't find anything unusual.")

    def find_random_item(self):
        items = ["hidden bone", "strange berry", "sparkling stone"]
        item = random.choice(items)
        self.inventory.append(item)
        print(f"You found a {item} hidden in the bushes!")

    def dig_hole(self):
        print("You start digging a hole...")
        if random.randint(1, 10) > 5:  # 50% chance of finding something
            self.find_buried_treasure()
        else:
            print("You just find some dirt and a few rocks.")

    def find_buried_treasure(self):
        treasures = ["old coin", "ancient artifact"]
        treasure = random.choice(treasures)
        self.inventory.append(treasure)
        print(f"You found a {treasure} buried in the ground!")

    def play_game(self):
        print("Welcome to the Decision-Based Dog Puppy Adventure in the Forest!")
        print("You are a curious puppy, exploring the vast and mysterious forest, filled with wonders and dangers.")
        
        actions = ["animal", "food", "item", "grow", "explore", "dig"]
        chosen_action = random.choice(actions)
        if chosen_action == "explore":
            self.explore_area()
        elif chosen_action == "dig":
            self.dig_hole()

        if random.randint(1, 10) <= 2:  # 20% chance for a random event
            self.random_event()

        self.adjust_health(-1)  # Example: Health decreases slowly over time

        while self.strength > 0 and self.age < 12 and self.hunger < 100:
            self.display_status()
            action = random.choice(["animal", "food", "item", "grow"])
            if action == "animal":
                self.encounter_animal()
            elif action == "food":
                self.find_food()
            elif action == "item":
                self.find_item()
            elif action == "grow":
                self.grow_older()

            if self.hunger >= 100:
                print("\nYou've become too hungry to continue your adventure. Game Over.")
                break
            elif self.strength <= 0:
                print("\nYou've become too weak to continue your adventure. Game Over.")
                break

# Create a game instance and start the game
decision_based_game = PuppyGame()
decision_based_game.play_game()
