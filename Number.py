import random
import math

lower = int(input("enter the lower bound"))
upper = int(input("enter the upper bound"))

# generate a random number between lower and upper bounds

x=random.randint(lower, upper)
total_chances = math.ceil(math.log(upper - lower + 1,2))

print("\n\tYou've only 10 chances to guess the "
           "integer!\n\n",
           total_chances)


count=0
flag = False
while count<total_chances :
    count+=1
    guess=int(input("Guess the number: "))
    if guess==x:
        flag = True
        break
    elif guess<x:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")


if not flag:
    print("\nSorry, you couldn't guess the correct number. The number was %d.", x)
print("\nCongratulations! You guessed the correct number in %d attempts.",count)