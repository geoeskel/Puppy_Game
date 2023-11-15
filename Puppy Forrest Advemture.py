import random
import os

# Utility function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Utility function to format stat changes with colors
def format_stat_change(change):
    RED = "\033[91m"
    GREEN = "\033[92m"
    RESET = "\033[0m"
    return f"{GREEN}+{change}{RESET}" if change > 0 else f"{RED}{change}{RESET}"

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

    # Method for adjusting health
    def adjust_health(self, amount):
        old_health = self.health
        self.health = max(0, min(100, self.health + amount))
        if self.health != old_health:
            desc = "Feeling a bit under the weather!" if amount < 0 else "Feeling healthier!"
            self.display_stat_change(desc, "Health", old_health, amount)

    # Method for adjusting energy
    def adjust_energy(self, amount):
        old_energy = self.energy
        self.energy = max(0, min(100, self.energy + amount))
        if self.energy != old_energy:
            desc = "Running out of steam!" if amount < 0 else "Energized and ready to go!"
            self.display_stat_change(desc, "Energy", old_energy, amount)

    # Method to display stat changes
    def display_stat_change(self, description, stat_name, old_value, change):
        clear_screen()  # Clear the screen for a new 'page'
        new_value = old_value + change
        change_str = format_stat_change(change)

        print(description)  # Description
        print("-" * 20)
        print(f"{stat_name} Change")
        print(f"Previous {stat_name}: {old_value}")
        print(f"Change: {change_str}")
        print(f"New {stat_name}: {new_value}")
        print("-" * 20)
        input("Press Enter to continue...")

        clear_screen()  # Clear the screen after user acknowledges

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

    def find_item(self):
        items = {
            "stick": {"strength": 2, "wisdom": 1, "description": "You found a stick! It looks sturdy."},
            "feather": {"strength": 1, "wisdom": 2, "description": "A feather lies here. It's light and colorful."},
            "bone": {"strength": 3, "wisdom": 0, "description": "There's a bone buried here! It seems old but valuable."}
        }

        clear_screen()  # Clear the screen for a new 'page'

        item_key = random.choice(list(items.keys()))
        item = items[item_key]

        print(item["description"])
        self.inventory.append(item_key)
        print(f"You add the {item_key} to your inventory.")

        # Applying stat changes
        if item["strength"] > 0:
            self.strength += item["strength"]
            print(f"Strength increased: {format_stat_change(item['strength'])}")

        if item["wisdom"] > 0:
            self.wisdom += item["wisdom"]
            print(f"Wisdom increased: {format_stat_change(item['wisdom'])}")
        
        print("\n" + "-" * 30)  # End of item find decorator


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
        "squirrel": {
            "description": "A lively squirrel jumps around.",
            "required_strength": 5,
            "required_wisdom": 4,
            "puppy_thoughts": "Squirrels are so agile and fun!"
        },
        "rabbit": {
            "description": "A quick rabbit hops nearby, alert and cautious.",
            "required_strength": 3,
            "required_wisdom": 5,
            "puppy_thoughts": "That rabbit looks fast, but maybe I can catch up!"
        },
        "owl": {
            "description": "A wise owl observes you from a tree, its eyes full of wisdom.",
            "required_strength": 6,
            "required_wisdom": 10,
            "puppy_thoughts": "What secrets does that owl know?"
        },
        "fox": {
            "description": "A sly fox sneaks through the underbrush, watching you curiously.",
            "required_strength": 8,
            "required_wisdom": 7,
            "puppy_thoughts": "Foxes are so mysterious. What's it thinking?"
        },
        "badger": {
            "description": "A tenacious badger snarls defensively.",
            "required_strength": 12,
            "required_wisdom": 8,
            "puppy_thoughts": "That badger looks tough, but also kind of grumpy."
        },
        "bear": {
            "description": "A massive bear lumbers by, sniffing the air.",
            "required_strength": 20,
            "required_wisdom": 15,
            "puppy_thoughts": "Wow, that bear is huge! Better be careful."
        },
        "wolf": {
            "description": "A lone wolf watches you with piercing eyes.",
            "required_strength": 18,
            "required_wisdom": 12,
            "puppy_thoughts": "That wolf looks strong and wise. I wonder what it's thinking."
        },
        "deer": {
            "description": "A graceful deer bounds through the forest.",
            "required_strength": 7,
            "required_wisdom": 10,
            "puppy_thoughts": "Such a majestic creature. I wish I could run as fast as it does."
        },
        "snake": {
            "description": "A slithering snake hisses as it coils up.",
            "required_strength": 6,
            "required_wisdom": 14,
            "puppy_thoughts": "Snakes are scary, but also kind of fascinating."
        },
        "boar": {
            "description": "A wild boar grunts and roots around the ground.",
            "required_strength": 15,
            "required_wisdom": 9,
            "puppy_thoughts": "Boars look tough. I should approach with caution."
        },
        
    }

        clear_screen()  # Clear the screen for a new 'page'

        animal, attributes = random.choice(list(animals.items()))
        print(f"\nEncounter: A {animal} appears! {attributes['description']}")

        if self.strength >= attributes["required_strength"] and self.wisdom >= attributes["required_wisdom"]:
            choice = input(f"Do you want to approach the {animal}? (y/n): ").lower()
            if choice == 'y':
                self.animals_met += 1
                stat_change = random.randint(-5, 5)  # Stat change
                old_strength = self.strength
                self.strength += stat_change
                

                desc = "You flex your puppy muscles after the encounter!" if stat_change > 0 else "Looks like that was ruff!"
                self.display_stat_change(desc, "Strength", old_strength, stat_change)
                    
                if animal == "squirrel":
                    print("The squirrel playfully engages with you before darting away.")
                    print("Puppy thoughts: 'Chasing squirrels is fun, but they're so fast!'")
                elif animal == "wolf":
                    print("The wolf regards you with a noble grace, imparting a sense of strength.")
                    print("Puppy thoughts: 'Wow, I hope to be as majestic as that wolf one day.'")
                elif animal == "eagle":
                    print("The eagle takes flight, soaring gracefully above you.")
                    print("Puppy thoughts: 'I wish I could soar high like that eagle!'")
                elif animal == "bear":
                    print("The bear sniffs around and wanders off, seemingly uninterested.")
                    print("Puppy thoughts: 'That was scary, but I think the bear was just curious like me.'")
                elif animal == "fox":
                    print("The fox gives you a cunning look and quickly disappears into the bushes.")
                    print("Puppy thoughts: 'Foxes are so mysterious... I wonder where it went?'")
                elif animal == "owl":
                    print("The owl hoots softly, sharing its wisdom before flying away.")
                    print("Puppy thoughts: 'There's something special about that owl...'")
                elif animal == "rabbit":
                    print("The rabbit hops around a bit before scampering away.")
                    print("Puppy thoughts: 'Rabbits are cute, but they sure are jumpy!'")
                elif animal == "butterfly":
                    print("The butterfly lands on your nose for a moment before fluttering away.")
                    print("Puppy thoughts: 'Hehe, that tickled!'")
                elif animal == "badger":
                    print("The badger grumbles a bit but eventually shows some friendly gestures.")
                    print("Puppy thoughts: 'Badgers are tough, but I think we understand each other.'")
                    print(f"You interact with the {animal}...")
                self.gain_xp(5)
                self.check_challenges()
                self.adjust_energy(-10)
                print(f"Puppy thoughts: '{attributes['puppy_thoughts']}'")
            else:
                print(f"You cautiously decide to keep your distance from the {animal}.")
                print(f"Puppy thoughts: 'Better safe than sorry...'")
            
        else:
            print(f"The {animal} seems too daunting to approach right now.")
            print(f"Puppy thoughts: 'I'm not quite ready for this yet...'")
        print("\n" + "-" * 30)  # End of encounter decorator
        

    def find_food(self):
        foods = ["berries", "meat", "fish"]
        food = random.choice(foods)
        hunger_reduction = random.randint(10, 30)

        print(f"\nYou find some {food}.")
        choice = input("Do you want to eat it? (y/n): ").lower()
        if choice == 'y':
            self.foods_eaten += 1
            old_hunger = self.hunger
            self.hunger = max(0, self.hunger - hunger_reduction)
            
            # Added description for display_stat_change call
            desc = "Yum! That hit the spot!" if hunger_reduction > 0 else "Oops, maybe that wasn't so tasty after all."
            self.display_stat_change(desc, "Hunger", old_hunger, -hunger_reduction)

            print(f"You eat the {food} and reduce your hunger by {hunger_reduction} points.")
        else:
            print("You decide not to eat the food.")
        
        self.gain_xp(3)
        self.check_challenges()
        self.adjust_energy(20)  # Eating food restores energy

    def find_item(self):
        items = {
            "stick": {"strength": 2, "wisdom": 1},
            "feather": {"strength": 1, "wisdom": 2},
            "bone": {"strength": 3, "wisdom": 0}
        }
        item = random.choice(list(items.keys()))
        print(f"\nYou found a {item}!")

        choice = input("Do you want to take it? (y/n): ").lower()
        if choice == 'y':
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
        old_wisdom = self.wisdom
        wisdom_increase = 2
        print("Suddenly, it starts raining! You feel refreshed and gain some wisdom.")
        self.wisdom += wisdom_increase
        desc = "Raindrops keep falling on your head, but you just got wiser!"
        self.display_stat_change(desc, "Wisdom", old_wisdom, wisdom_increase)

    def friendly_traveler(self):
        old_wisdom = self.wisdom
        wisdom_increase = 3
        print("A friendly traveler passes by and shares some tips with you.")
        self.wisdom += wisdom_increase
        desc = "A bit of friendly advice goes a long way!"
        self.display_stat_change(desc, "Wisdom", old_wisdom, wisdom_increase)
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
        clear_screen()
        print("Welcome to the Puppy Adventure in the Forest!")
        print("------------------------------------------------")
        print("In a world filled with wonders and snacks, one puppy's journey begins.")
        print("Will you sniff, dig, and bark your way to legendary status?")
        print("Or will you nap too much and just dream about it?")
        print("The choice is yours!")
        print("------------------------------------------------")
        input("Press Enter to embark on your adventure...")

        clear_screen()  # Clear the screen after the user presses Enter

        # Main game loop
        while self.strength > 0 and self.age < 12 and self.hunger < 100:
            self.display_status()
            if random.randint(1, 10) <= 2:  # 20% chance for a random event
                self.random_event()

            self.adjust_health(-1)  # Health decreases slowly over time

            actions = ["animal", "food", "item", "grow", "explore", "dig"]
            chosen_action = random.choice(actions)
            if chosen_action == "animal":
                self.encounter_animal()
            elif chosen_action == "food":
                self.find_food()
            elif chosen_action == "item":
                self.find_item()
            elif chosen_action == "grow":
                self.grow_older()
            elif chosen_action == "explore":
                self.explore_area()
            elif chosen_action == "dig":
                self.dig_hole()

            if self.hunger >= 100:
                print("\nYou've become too hungry to continue your adventure. Game Over.")
                break
            elif self.strength <= 0:
                print("\nYou've become too weak to continue your adventure. Game Over.")
                break

# Create a game instance and start the game
game = PuppyGame()
game.play_game()