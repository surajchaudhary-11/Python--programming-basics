import random

secret = random.randint(1, 100)
guess = int(input("Guess the number: "))

while guess != secret:
    if guess > secret:
        print("Guess a lower number")
    else:
        print("Guess a higher number")
    guess = int(input("Guess the number: "))

print("You hit the bullseye!  \n  Maa chod di")