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

## Known Issues

1. **Signed Differences**:  
   The program calculates signed differences instead of absolute differences. This can lead to incorrect results. For example:
   - If `player_1 = 8` and `random_number = 6`, the difference is `8 - 6 = 2`.
   - If `player_2 = 4` and `random_number = 6`, the difference is `4 - 6 = -2`.
   - The program would incorrectly declare Player 2 as the winner because `-2` is smaller than `2`.

   **Fix**: Use absolute differences:
   ```python
   p1_differnce = abs(player_1 - random_number)
   p2_differnce = abs(player_2 - random_number)
   p3_differnce = abs(player_3 - random_number)

##Example Run
Input:
* Player 1: 4
* Player 2: 7
* Player 3: 5
Random Number:
* Random number generated: 6
Differences:
* Player 1: 4 - 6 = -2
* Player 2: 7 - 6 = 1
*Player 3: 5 - 6 = -1
Result:
The program incorrectly declares Player 2 as the winner because it uses signed differences instead of absolute differences.
Suggested Improvements
* Use Absolute Differences: Replace signed difference calculations with absolute differences.
* Handle Ties: Add logic to handle ties and declare multiple winners if necessary.
* Improve Variable Names: Rename variables for better readability.
