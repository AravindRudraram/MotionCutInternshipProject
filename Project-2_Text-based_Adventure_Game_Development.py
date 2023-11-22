def enter_cave():
    print("You chose to enter the cave. You encounter a sleeping bear.")
    print("Choices:\n1. Try to sneak past the bear.\n2. Turn back.")
    choice = int(input())
    if choice == 1:
        sneak_past_bear()
    else:
        start_adventure()

def sneak_past_bear():
    print("You successfully sneak past the bear and find a treasure chest.")
    print("Choices:\n1. Open the chest.\n2. Leave the chest and exit the cave.")
    choice = int(input())
    if choice == 1:
        open_chest()
    else:
        start_adventure()

def open_chest():
    print("You open the chest and find a golden crown. Congratulations, you've won the game!")

def climb_mountain():
    print("You chose to climb the mountain. You encounter a steep cliff.")
    print("Choices:\n1. Try to climb the cliff.\n2. Turn back.")
    choice = int(input())
    if choice == 1:
        climb_cliff()
    else:
        start_adventure()

def climb_cliff():
    print("You successfully climb the cliff and find a dragon's egg.")
    print("Choices:\n1. Take the egg.\n2. Leave the egg and descend the mountain.")
    choice = int(input())
    if choice == 1:
        take_egg()
    else:
        start_adventure()

def take_egg():
    print("You take the egg and safely descend the mountain. Congratulations, you've won the game!")

def start_adventure():
    print("Welcome to the Text-based Adventure Game!")
    print("You are at the edge of a dark forest. You can either enter a cave or climb a mountain.")
    print("Choices:\n1. Enter the cave.\n2. Climb the mountain.")
    choice = int(input())
    if choice == 1:
        enter_cave()
    else:
        climb_mountain()

start_adventure()
