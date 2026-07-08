# Number Guessing Game
A simple command-line Number Guessing Game built with Python. The player tries to guess a randomly generated number between **1** and **10**, 
receiving hints after each incorrect guess until the correct number is found.
---

## Features
- Random number generation for every round
- Unlimited guessing attempts
- Hint system:
  - Too High
  - Too Low
- Input validation
- Tracks the number of attempts
- Automatic new round after a successful guess
- Exit the game anytime by typing `exit`

---

## Concepts Used
- Python Functions
- Loops (`while`)
- Conditional Statements (`if-elif-else`)
- Exception Handling (`try-except`)
- User Input
- Random Module
- Input Validation

---

## How to Run
1. Clone the repository or download the project.
2. Open a terminal in the project directory.
3. Run the following command:

```bash
python guessing_game.py
```

---
## Example Output

```text
=======================================================
          WELCOME TO THE NUMBER GUESSING GAME
=======================================================

Rules:
- Guess a number between 1 and 10.
- Type 'exit' at any time to quit.

---------- Round 1 ----------

Enter your guess: 4
Too Low! Try again.

Enter your guess: 8
Too High! Try again.

Enter your guess: 6

Congratulations!
You guessed the correct number: 6
Attempts: 3

Starting a new round...
```

---

## Future Improvements

- Difficulty levels (Easy, Medium, Hard)
- Limited attempts
- Score tracking
- High score system
- Replay option
- Graphical User Interface (GUI)
- Sound effects

---

## Author
**Kushagra-des**
