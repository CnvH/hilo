from random import random

x = int(round(random() * 99) + 1)


guess_num = 1

y = int(input(f"Enter guess {guess_num}: "))

while guess_num < 5:
    guess_num += 1
    if x > y:
        y = int(input(f"too low, try again, guess {guess_num}:"))
        continue

    if x < y:
        y = int(input(f"too high, try again, guess {guess_num}:"))
        continue

    if x == y:
        print(f"pure genius, you did it in  {guess_num-1} tries")
        break

print("too slow....")
