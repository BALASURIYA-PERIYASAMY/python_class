import random
sec = random.randint(1,10)
guess = int(input("Enter the Guessing Number Between 1 to 10: "))

if guess == sec:
    print("Congratulation! you Guessed the Number:")

else:
    print("Sorry, The Correct Number was ",sec)