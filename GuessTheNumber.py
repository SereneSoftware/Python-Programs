import random

secret_number = random.randint(1, 100)
print("I am thinking of a number between 1 and 100.")

while True:
    guess = int(input("Take a guess: "))
    
    if guess == secret_number:
        print("Good job! You guessed my number!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
