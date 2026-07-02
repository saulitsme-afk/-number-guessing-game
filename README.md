# Number Guessing Game 🎯

A simple command-line number guessing game built in Python.
The game picks a random number between 1 and 100, and you try to guess it within a limited number of attempts based on the difficulty level you choose.

## How It Works

1. Run the script.
2. Choose a difficulty level:
   - **Level 1 (Easy):** 10 attempts
   - **Level 2 (Medium):** 5 attempts
   - **Level 3 (Hard):** 3 attempts
3. Try to guess the secret number within your allotted attempts.
4. If you guess correctly, you win! If you run out of attempts, the game reveals the number.

## Getting Started

### Prerequisites
- Python 3.x installed on your machine

### Running the game
```bash
python number_guessing_game.py
```

## Example Gameplay

```
Welcome to the number guessing game!
I'm thinking of a number between 1 and 100
Please select the difficulty level:
level 1 : easy
level 2 : medium
level 3 : hard
Please select the difficulty level: 2
Great! You have selected the medium level
You have 5 chances to guess the correct number
Let's start the game!

Attempt 1 of 5
Enter your guess: 50
Incorrect!

Attempt 2 of 5
Enter your guess: 65
Correct! 🎉
You guessed it in 2 attempts!
```

## Future Improvements

- [ ] Add a "too high / too low" hint mode as a selectable option
- [ ] Track and display best scores across sessions
- [ ] Add input validation for non-numeric guesses
- [ ] Allow replaying without restarting the script

## License

This project is open source and available for anyone to use or modify.

##project URL
guess me .py
