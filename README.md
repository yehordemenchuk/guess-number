# guess number
---

## Overview
"Guess Number" is a simple and engaging number-guessing game implemented in Python. The player tries to guess a randomly generated number within a specified range. The game provides feedback on whether the guessed number is too high or too low, helping the player zero in on the correct number. This game is perfect for practicing logical thinking and number sense.

---

## Game Rules
* The game randomly selects a number within a specified range (depends on difficulty).
* Low difficulty selects a number from 0 to 20, middle - from 0 to 50, hardcore - from 0 to 100
* The player makes a guess and the game provides feedback:
* "No, my number is bigger" if the guess is greater than the target number.
* "No, my number is smaller" if the guess is less than the target number.
* Player has limited number of tryings (10 - low difficulty, 8 - middle, 5 - hardcore)
---

## Instalation
1. Download or clone this repository from GitHub.
2. Ensure you have Python installed on your system. You can download it from python.org.
3. Navigate to the directory containing the guess_number.py script.
---

## Running the Game
To run the game, use the following command in your terminal:
```shell
python main.py
```
---