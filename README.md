# Guess the Closest Number Game

This is a simple Python-based command-line game where three players guess a number, and the program determines the winner based on whose guess is closest to a randomly generated number.

---

## How It Works

1. **Input from Players**:  
   Each of the three players is prompted to enter a number.

2. **Random Number Generation**:  
   The program generates a random number between 1 and 10 (inclusive).

3. **Difference Calculation**:  
   The program calculates the difference between each player's guess and the random number.

4. **Determine the Winner**:  
   The player whose guess is closest to the random number (i.e., has the smallest difference) is declared the winner.

---

## Code Walkthrough

### 1. **Player Input**
The program takes input from three players:
```python
player_1 = int(input("Enter a Number Player 1: "))
player_2 = int(input("Enter a Number Player 2: "))
player_3 = int(input("Enter a Number Player 3: "))
