# MotionCut Internship
# Week 1 Task: To-Do List Application in Python 
A basic GUI To-Do List Application written in Python and Tkinter library. This application allows users to perform essential operations on their to-do list, including adding tasks, marking tasks as completed, updating task descriptions, removing tasks, and displaying the current task list.
![image](https://github.com/AravindRudraram/MotionCutInternshipProject/assets/120008993/24756e49-0228-412e-8543-47d9db1a464d)

# Week 2 Task: Text-based Adventure Game Development
This Python script represents a simple text-based adventure game. The game begins with a welcome message and presents the player with a choice between entering a cave or climbing a mountain. Depending on the player's decision, the game progresses through different scenarios and outcomes.

Here's a breakdown of the main functions:

start_adventure(): Displays the initial setup of the game, introducing the player to the options of entering a cave or climbing a mountain. Based on the player's choice, it calls either enter_cave() or climb_mountain().

enter_cave(): If the player chooses to enter the cave, they encounter a sleeping bear. The player can then choose to either sneak past the bear or turn back. If they choose to sneak past, it calls the sneak_past_bear() function. If they turn back, it restarts the adventure.

sneak_past_bear(): If the player successfully sneaks past the bear, they find a treasure chest. The player can choose to either open the chest or leave it. If they choose to open it, the open_chest() function is called and the player wins the game. If they leave, the adventure restarts.

open_chest(): If the player chooses to open the chest, they find a golden crown, and the game congratulates them, indicating they've won.

climb_mountain(): If the player chooses to climb the mountain, they encounter a steep cliff. They can choose to either climb the cliff or turn back. If they choose to climb, it calls the climb_cliff() function. If they turn back, the adventure restarts.

climb_cliff(): If the player successfully climbs the cliff, they find a dragon's egg. They can choose to take the egg or leave it and descend the mountain. If they take the egg, it calls the take_egg() function, and the player wins the game. If they leave the egg, the adventure restarts.

take_egg(): If the player chooses to take the dragon's egg, they safely descend the mountain, and the game congratulates them, indicating they've won.

The game structure provides a branching narrative with different choices and outcomes, creating a simple interactive experience for the player.

# Week 3 Task: Password Generator
The code defines two functions: generate_password and generate_multiple_passwords.
The generate_password function creates a random password of a specified length using a combination of letters, digits, and punctuation.
The generate_multiple_passwords function generates a specified number of passwords by calling generate_password for each password length provided by the user.
The main block of the script takes user input for the number of passwords, generates passwords, and displays them.
