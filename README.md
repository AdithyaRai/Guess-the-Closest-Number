Guess the Closest Number
Simple Python console game where three players each guess a number (1–10). The program generates a random target number and the player whose guess is closest wins.

File
c:\Users\Adithya\Documents\C++ Assignment\HtmlP\guess the closest number.py
Requirements
Python 3.x
How to run
Open a terminal and run:

Gameplay
Each of three players enters an integer guess.
The script generates a random integer between 1 and 10.
It computes which player's guess is closest and prints the winner.
Example session
Known issues
Uses signed difference instead of absolute distance; negative values can produce wrong winner.
Ties are not handled — if two players are equally close, the script picks the first matching minimum.
No input validation — non-integer input raises an error.
The random target is not shown to players (useful for debugging).
Suggested improvements
Use absolute differences: abs(guess - random_number).
Handle ties (announce multiple winners or a draw).
Validate input and re-prompt on invalid entries.
Print the generated random number for clarity or debugging.
Allow configurable number of players or multiple rounds and keep score.
License
Free to use and modify.
