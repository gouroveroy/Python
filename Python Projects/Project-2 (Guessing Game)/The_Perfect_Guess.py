import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    count = 7
    guessed = False
    print(f"Welcome to the guessing game! The computer has chosen a number between 1 and {x}.")
    print(f"You have total of {count} guesses to guess the number.")
    while guess != random_number and count != 0:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        count -= 1
        
        if guess == random_number:
            print(f"Congratulations! You have guessed the number {random_number} correctly!")
            guessed = True
            break
        
        elif count == 0:
            break
        
        difference = abs(guess - random_number)
        
        if guess > random_number:
            print("Sorry, guess again.")
            
            if difference > 5:
                print("Guessed number is too high. You are too far.")
            
            else:
                print("Guessed number is high. You are close.")
            
        else:
            print("Sorry, guess again.")
            
            if difference > 5:
                print("Guessed number is too low. You are too far.")
            
            else:
                print("Guessed number is low. You are close.")
        
        if count == 1:
            print(f"You have {count} guess left.\n")
            
        else:
            print(f"You have {count} guesses left.\n")
            

    if not guessed:
        print(f"Sorry, you have run out of guesses. The correct number was {random_number}.")
        return
    

guess(100)
