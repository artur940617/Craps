# Game craps
import random

one = random.randint(1,7)
two = random.randint(1,7)
craps_sum = one + two
i = 3
print(f'The sum of dice is {one} + {two} = {craps_sum}')
if craps_sum == 11 or craps_sum == 7:
    print("You won")
elif craps_sum == 2 or craps_sum == 3 or craps_sum == 12:
    print("Casino wins")
else:
    print(f'Now your goal number is {craps_sum}')
    while i != 0:
        one1 = random.randint(1,7)
        two2 = random.randint(1,7)
        sum_goal = one1 + two2
        print(f'The sum of dice is {one1} + {two2} = {sum_goal}')
        if craps_sum == sum_goal:
            print("You won")
            raise SystemExit
        i -= 1
    print("You lose")


