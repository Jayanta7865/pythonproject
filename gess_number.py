import random


random_number = random.randint(1, 100)

a="Welcome to the Guess the Number game!"
print(a.center(100))
print("\n I have chosen a number between 1 - 100." "\n" "You have 5 attempts.")


attempts = 5

for i in range(attempts):
    guess = int(input(f"Attempt {i+1}: Enter your guess number: "))
    if guess < 1 or guess > 100:
        print("⚠ Please enter a number between 1 and 100.")
        continue 
    
    if guess < random_number:
        print("Your guess number is too low from the random number!")
    elif guess > random_number:
        print("Your guess number is too high from the random number!")
    else:
        print(f"Congratulations! You guessed the number {random_number} in {i+1} attempts.")
        print("You won iphone 16 pro max")
        break
else:
    print(f"Sorry! You've used all {attempts} attempts. The number was {random_number}.")
    print("Better Luck Next Time")
print("Thanks! For playing this game..")