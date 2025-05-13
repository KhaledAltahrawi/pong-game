# Pygame Pong: Player vs Computer

This repository contains a classic Pong game implemented using the Pygame library in Python. In this version, players control the left paddle and compete against a simple AI-controlled right paddle.

## Features

- **Intuitive Controls:** Players use the 'W' and 'S' keys to move their paddle up and down.
- **Basic AI Opponent:** The computer-controlled paddle attempts to track and hit the ball. The AI's speed slightly increases as the player's score goes up, providing a gentle increase in difficulty.
- **Scoring System:** The game keeps track of both the player's and the computer's scores.
- **Ball Physics:** The ball bounces off the top and bottom walls and speeds up slightly upon hitting a paddle, adding a dynamic element to the gameplay.
- **Win Condition:** The first player (or computer) to reach a score of 10 wins the game.
- **Start Screen:** A simple start screen prompts the player to press the SPACE bar to begin.
- **Pause Functionality:** Press the 'P' key during gameplay to pause and resume the game.
- **Game Over Screen:** When a player wins, a game over screen displays the winner and the final score, offering the option to play again ('Y') or quit ('N').

## How to Run

1.  **Prerequisites:** Ensure you have Python 3 and the Pygame library installed on your system. If you don't have Pygame, you can install it using pip:

    ```bash
    pip install pygame
    ```

2.  **Download the Script:** Download the `pong.py` file (or whatever you name the Python script containing the code) from this repository.

3.  **Run the Game:** Open your terminal or command prompt, navigate to the directory where you saved the script, and run it using:
    ```bash
    python pong.py
    ```

## Gameplay

- Upon running the script, you will be greeted with a start screen. Press the **SPACE** bar to begin the game.
- Control the **left paddle** using the **'W'** key to move up and the **'S'** key to move down.
- The **right paddle** is controlled by a basic AI.
- The goal is to hit the ball past your opponent's paddle to score a point.
- The first player to reach **10 points** wins the game.
- Press the **'P'** key to pause the game. Press **'P'** again to resume.
- After a player wins, you will see a game over screen. Press **'Y'** to play a new game or **'N'** to quit.

## Author

This Pygame Pong game was created as a fun practice project to strengthen game development concepts with Pygame. Feel free to fork this repository and contribute your own improvements!
