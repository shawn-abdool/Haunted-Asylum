# Haunted Asylum

A spooky 2D survival game built with **Pygame**, where you navigate eerie corridors, collect keys, and escape a relentless enemy lurking in the shadows. Simple square-based graphics with a creepy twist — can you survive the haunted asylum?

---

## Features

- Classic 2D top-down gameplay with minimalist square sprites  
- Move your player square through walls and corridors  
- Collect keys to unlock the exit and advance through levels  
- Evade a pursuing enemy that relentlessly chases you down  
- Enter your username and track your highest level survived  
- View a leaderboard stored in a CSV file showing top players and scores  
- Menus and death screens built with Tkinter for a smooth UI experience  

---

## Screenshots

![pygame_deathscreen](https://github.com/user-attachments/assets/f051a994-e196-4ea9-9a80-80f8c811e7a5)


---

## Requirements

- Python 3.x  
- [Pygame](https://www.pygame.org/news)  
- [Pillow](https://python-pillow.org/)  
- Tkinter (usually pre-installed with Python)

---

## Installation

1. Clone this repository:

- git clone https://github.com/shawn-abdool/Haunted-Asylum.git
- cd HauntedAsylum

2. Install dependencies

- pip install pygame
- pip install pillow

---

## Run the Program

python main_menu.py

---

## Controls

WASD to control your player

---

## Game Structure

- main_menu.py: Launches the Tkinter-based main menu
- main.py: Runs the main Pygame game loop
- death_screen.py: Displays the death screen with options
- game_scores.csv: Stores usernames and levels survived
- game_classes.py: Contains the enemy, wall, door and key objects
- displayLeaderboard.py: Displays the csv file content into a table
- levels_survived.txt: Stores the number of levels you survive for
- my_imports.py: Contains imports (not used due to issues)
- my_levels.py: Contains the levels
- player_class.py: Contains player object and collision detection

## Improvements

This program was a mini-project for me back at school.
I'm aware it's not perfect.
