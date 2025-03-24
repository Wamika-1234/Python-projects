import random
random_number=random.randint(1,10)
number_guesses=0
user_won=False
for turn in range(10):
    user_guess=int(input("Guess a number between 1 and 10"))
    number_guesses+=1
    if user_guess==random_number:
        print("Yay! You guessed right")
        print("You guessed the number in ",number_guesses," guesses")
        user_won=True
        break
    elif user_guess<random_number:
        print("Your guess is lower than the number")
    elif user_guess>random_number:
         print("Your guess is higher than the number")
if not user_won:
    print("Game over! The random number was ",random_number)
