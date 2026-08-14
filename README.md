# Tic Tac Toe

A command-line Tic Tac Toe game written in Python.

This project started as a simple two-player Tic Tac Toe game and was later improved with a colored terminal interface, score tracking, multiple rounds, and a cleaner function-based structure.

## Features

- Two-player gameplay (X vs O)
- Input validation
- Detection of wins and draws
- Multiple rounds
- Persistent score tracking
- Colored X and O symbols in the terminal
- Simple and clean command-line interface
- Replay option after each round

## How to Play

Run the program from the terminal:

```bash
python3 tic_tac_toe.py
```

Players take turns choosing a position from **1 to 9**.

The board positions are:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

The first player to get three symbols in a row, column, or diagonal wins the round.

If all positions are filled without a winner, the round ends in a draw.

After each round, the current score is displayed and the players can choose whether to play again.

## Project Structure

```text
tic-tac-toe/
│
├── main.py
└── README.md
```

## Concepts Practiced

This project was created as part of my Python learning journey and helped me practice:

- Functions
- Lists
- Dictionaries
- `while` and `for` loops
- Conditional statements
- User input and validation
- String formatting
- ANSI terminal colors
- Passing data between functions
- Basic program structure
- Git and GitHub workflow

## Future Improvements

Possible future versions may include:

- Computer opponent (AI)
- Difficulty levels
- Improved input handling
- More advanced game statistics
- Further code refactoring

## Technologies

- Python 3
- Command Line Interface (CLI)
- Git
- GitHub

## Author

Created as part of my Python learning journey and personal programming portfolio.