import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    count = 7
    print(f"You have total of {count} guesses to guess the number between 1 and {x}.")
    while guess != random_number and count != 0:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        count -= 1
        
        if guess == random_number:
            print(f"Congratulations! You have guessed the number {random_number} correctly!")
            break
        
        elif count == 0:
            break
        
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
            
        else:
            print("Sorry, guess again. Too low.")
        
        if count == 1:
            print(f"You have {count} guess left.\n")
            
        else:
            print(f"You have {count} guesses left.\n")
            

    if count == 0:
        print(f"Sorry, you have run out of guesses. The correct number was {random_number}.")
        return
    

guess(100)
