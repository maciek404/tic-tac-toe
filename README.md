# Tic Tac Toe

A command-line Tic Tac Toe game written in Python.

The project started as a simple two-player Tic Tac Toe game and has been gradually improved with a colored terminal interface, score tracking, multiple rounds, game mode selection, and a rule-based AI opponent.

## Features

- Player vs Player mode
- Player vs AI mode
- Rule-based AI opponent
- AI can identify winning moves
- AI can block the player's winning move
- AI prioritizes the center position
- AI prioritizes corner positions
- Random fallback move when no strategic move is available
- Input validation
- Detection of wins and draws
- Multiple rounds
- Persistent score tracking
- Colored X and O symbols in the terminal
- Simple command-line interface
- Replay option after each round

## AI Strategy

The AI currently follows a simple priority-based strategy:

1. **Win if possible**  
   The AI checks whether it can complete a winning combination.

2. **Block the player**  
   If the player is one move away from winning, the AI blocks the winning position.

3. **Take the center**  
   If the center position is available, the AI chooses it.

4. **Choose a corner**  
   If the center is occupied, the AI chooses randomly from the available corners.

5. **Random fallback**  
   If no preferred move is available, the AI chooses randomly from the remaining positions.

This approach makes the AI more strategic than a purely random opponent while keeping the implementation simple and easy to understand.

## Game Modes

### Player vs Player

Two players take turns playing as X and O.

### Player vs AI

The player controls X while the computer controls O.

The AI analyzes the current board before making its move and follows the strategy described above.

## How to Play

Run the program from the terminal:

```bash
python3 main.py
```

At the beginning of the game, choose a game mode:

```text
1. Player vs Player
2. Player vs AI
```

Players choose a position by entering a number from **1 to 9**.

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

After each round, the score is displayed and the players can choose whether to play again.

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
- List comprehensions
- Dictionaries
- `while` and `for` loops
- Conditional statements
- User input and validation
- String formatting
- ANSI terminal colors
- The `random` module
- `random.choice()`
- Returning values from functions
- `None` and `is not None`
- Passing data between functions
- Basic recursion concepts
- Game state management
- Rule-based decision making
- Program structure and code organization
- Git and GitHub workflow

## Future Improvements

Possible future versions may include:

- More advanced AI decision-making
- AI fork detection
- Different AI difficulty levels
- Unbeatable AI using the Minimax algorithm
- Improved user interface
- Further code refactoring
- Unit tests

## Technologies

- Python 3
- Command Line Interface (CLI)
- Git
- GitHub

## Author

Created as part of my Python learning journey and personal programming portfolio.