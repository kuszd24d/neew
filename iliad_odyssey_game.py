import random
import time

def print_slow(text, delay=0.04):
    """Print text slowly for dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    """Introduction to the game."""
    print_slow("Welcome, hero, to the Iliad and the Odyssey adventure!\n")
    print_slow("You are Odysseus, cunning king of Ithaca, known for your wits and bravery.\n")
    print_slow("After the fall of Troy, you must journey home to Ithaca while surviving the gods' tests and mythical dangers.\n")
    print_slow("Your goal: Survive the journey and return to your family.\n")
    print_slow("Are you ready to embark on this epic journey? (yes/no)\n")

    while True:
        choice = input("> ").lower()
        if choice == "yes":
            print_slow("The gods smile upon you. Begin your journey!\n")
            break
        elif choice == "no":
            print_slow("The gods frown at your cowardice. Farewell, mortal!\n")
            exit()
        else:
            print_slow("Please answer 'yes' or 'no'.")

def encounter_choices(encounter_type):
    """Provide encounter-specific choices."""
    if encounter_type == "Cyclops":
        print_slow("1. Fight the Cyclops head-on.\n2. Sneak away and hide.\n3. Trick the Cyclops with a clever lie.")
    elif encounter_type == "Storm":
        print_slow("1. Sail through the storm.\n2. Pray to Poseidon for mercy.\n3. Anchor and wait for it to pass.")
    elif encounter_type == "Sirens":
        print_slow("1. Block your ears and row past.\n2. Challenge the Sirens to a song duel.\n3. Abandon yourself to their song.")
    elif encounter_type == "Scylla and Charybdis":
        print_slow("1. Sail closer to Scylla (6-headed monster).\n2. Sail closer to Charybdis (whirlpool).\n3. Try to find a middle path.")
    elif encounter_type == "Circe":
        print_slow("1. Attack Circe immediately.\n2. Seek her help cautiously.\n3. Accept her feast and trust her.")

def resolve_choice(encounter_type, choice, health):
    """Resolve the player's choice."""
    outcomes = {
        "Cyclops": {
            1: (-30, "The Cyclops is too strong! You barely escape with your life."),
            2: (-10, "You hide successfully, but the Cyclops destroys your supplies."),
            3: (10, "You trick the Cyclops by calling yourself 'Nobody' and escape unharmed."),
        },
        "Storm": {
            1: (-20, "The storm batters your ship, but you survive."),
            2: (-10, "Poseidon hears your prayers but is only mildly appeased."),
            3: (0, "You wait out the storm, losing precious time but staying safe."),
        },
        "Sirens": {
            1: (0, "You block your ears and row past safely."),
            2: (10, "You win the song duel, impressing the Sirens and escaping."),
            3: (-30, "You are lured into the sea and barely escape with your life."),
        },
        "Scylla and Charybdis": {
            1: (-20, "Scylla devours six of your men, but your ship survives."),
            2: (-30, "Charybdis nearly swallows your entire ship!"),
            3: (-10, "You find a middle path but suffer minor damage."),
        },
        "Circe": {
            1: (-20, "You attack Circe, but she transforms some of your crew into pigs."),
            2: (10, "You cautiously seek her help and she gives you advice for your journey."),
            3: (-10, "You trust her too easily and fall into her trap, but escape later."),
        },
    }
    health_change, result = outcomes[encounter_type][choice]
    print_slow(result + f" (Health change: {health_change})\n")
    return health + health_change

def random_encounter():
    """Randomly generate an encounter."""
    encounters = ["Cyclops", "Storm", "Sirens", "Scylla and Charybdis", "Circe"]
    return random.choice(encounters)

def game():
    """Main game loop."""
    health = 100
    journey_length = 5
    intro()
    
    for step in range(1, journey_length + 1):
        print_slow(f"\nJourney Leg {step} of {journey_length}...\n")
        encounter_type = random_encounter()
        print_slow(f"You encounter: {encounter_type}!\n")
        
        encounter_choices(encounter_type)
        
        while True:
            try:
                choice = int(input("\nChoose an action (1/2/3): "))
                if choice in [1, 2, 3]:
                    break
                else:
                    print_slow("Please choose a valid option: 1, 2, or 3.\n")
            except ValueError:
                print_slow("Invalid input. Please enter 1, 2, or 3.\n")
        
        health = resolve_choice(encounter_type, choice, health)
        print_slow(f"Your current health: {health}/100\n")
        
        if health <= 0:
            print_slow("You have succumbed to the trials of your journey. The gods weep for your loss.\n")
            print_slow("GAME OVER.\n")
            return

    print_slow("🏠 After countless trials, you finally reach Ithaca!\n")
    print_slow("Penelope and Telemachus welcome you home. The gods honor your perseverance.\n")
    print_slow("Congratulations, hero! You have completed your odyssey. 🎉\n")

if __name__ == "__main__":
    game()
