import random as ra

player_1 = int(input("Enter a Number Player 1: "))
player_2 = int(input("Enter a Number Player 2: "))
player_3 = int(input("Enter a Number Player 3: "))
 

random_number = ra.randint(1,10)
p1_differnce = player_1 - random_number
p2_differnce = player_2 - random_number
p3_differnce = player_3 - random_number

p_differnce = [p1_differnce, p2_differnce, p3_differnce]
minimum_diff = min(p_differnce)
if minimum_diff == p_differnce[0]:
    print("Player1 is the winner!")
elif minimum_diff == p_differnce[1]:
    print("Player2 is the winner!")
elif minimum_diff == p_differnce[2]:
    print("Player3 is the winner!")