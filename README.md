[README.md](https://github.com/user-attachments/files/23566620/README.md)
# 🚀 Alien Invasion Game



## 📌Project Overview

Alien Invasion is a lightweight 2D shooting game written in Python.

Pilot your spaceship up, down, left, and right to fire bullets and shoot down aliens;

Clear an entire alien fleet to advance to the next level, with increasing difficulty.
You have 3 lives per game: losing one when aliens reach the bottom, collide with your ship, or hit you with their bombs.
Survive more waves and achieve a higher score to win!



---

## 🛠️Tech Stack

| Technology |   Description    |
| :--------: | :--------------: |
|   python   |       3.7+       |
|   pygame   |       2.x        |
|   VSCode   | Recommend editor |



---

## ⚙️Installation & Run

1. Install the pygame dependency

```bash
python -m pip install pygame
```
or use PyPI mirror

```bash
python3 -m pip install -i https://mirrors.aliyun.com/pypi/simple/ pygame
```

2. Launch the game

```bash
cd Alien_Invasion
python main.py
```



---

## 🎮Settings

Open *settings.py* to adjust the following common parameters:

|         参数示例          |           说明            |
| :-----------------------: | :-----------------------: |
|        ship_limit         |  Number of ships (lives)  |
|      bullets_allowed      |   Max bullets on screen   |
|     fleet_drop_speed      | Alien fleet descent speed |
|    alien_bullet_limit     |      Max alien bombs      |
|     ship_speed_factor     |    Ship movement speed    |
| alien_bullet_speed_factor |     Alien bomb speed      |
|    bullet_speed_factor    |       Bullet speed        |
|        alien_speed        |  Alien horizontal speed   |



---

## 🕹️Controls

- Arrow keys: Move the ship
- Spacebar: Fire bullets
- BKSP: Quit game
- Mouse click on *play* or press TAB: Start game
