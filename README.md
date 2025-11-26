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

Follow the prompts to enter three numbers.

Example
User input:

Player 1: 4
Player 2: 7
Player 3: 5
If the random number is 6, distances are 
∣
4
−
6
∣
=
2
∣4−6∣=2, 
∣
7
−
6
∣
=
1
∣7−6∣=1, 
∣
5
−
6
∣
=
1
∣5−6∣=1 and the winner would be Player 2 (ties are not currently resolved).

Known issues & suggestions
The current code computes signed differences (p1_differnce, p2_differnce, p3_differnce) instead of absolute differences; use absolute values to get correct results.
Tie cases are not handled (two players equally close). Consider reporting a tie or selecting a deterministic tie-breaker.
Variable names contain a typo (differnce → difference) — renaming improves readability.
Possible improvement (fix)
Replace difference calculations with absolute values and add tie handling, e.g. compute distances via 
∣
p
l
a
y
e
r
i
−
r
a
n
d
o
m
_
n
u
m
b
e
r
∣
∣player 
i
​
 −random_number∣, then select all indices achieving the minimum and report either one or "tie".
