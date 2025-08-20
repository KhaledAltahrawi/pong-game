# Pygame Pong: Player vs Computer

Classic Pong built with **Python + Pygame**. You control the left paddle vs a simple AI on the right.

## Features
- **Controls:** `W` = up, `S` = down; `P` = pause/resume; `SPACE` = start; on Game Over, `Y` = play again / `N` = quit
- **AI Opponent:** Tracks the ball; difficulty ramps slightly as the player scores
- **Ball Physics:** Bounces off walls; speeds up a bit on paddle hits
- **Scoring & Win:** First to 10 wins
- **States:** Start, Playing, Paused, Game Over

## Setup
```bash
python -m venv .venv            # Windows: py -3 -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install pygame
```

## Run
```bash
python pong-game.py              # Windows: python pong-game.py
```

## Notes
This is a small learning project using a single Python file. Contributions and suggestions are welcome!
