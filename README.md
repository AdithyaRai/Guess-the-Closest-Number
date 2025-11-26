# Guess the Closest Number

Small CLI game implemented in [guess the closest number.py](guess the closest number.py).  
Key variables: [`player_1`](guess the closest number.py), [`player_2`](guess the closest number.py), [`player_3`](guess the closest number.py), [`random_number`](guess the closest number.py), [`p1_differnce`](guess the closest number.py), [`p2_differnce`](guess the closest number.py), [`p3_differnce`](guess the closest number.py), [`p_differnce`](guess the closest number.py), [`minimum_diff`](guess the closest number.py).

## Description
The script asks three players to enter integers, generates a random integer in [1, 10], and declares the player whose guess is closest to the random number as the winner. The intended distance metric is the absolute difference $|player_i - random\_number|$, and the winner is the index that minimizes that distance:
$$
\arg\min_i |player_i - random\_number|
$$

## Usage
Run with Python 3:
```sh
python "guess the closest number.py"
