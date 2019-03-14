#Python Web Development Techdegree
#Project 1 - Number Guessing Game
#--------------------------------
#By Samuel Montanez

import random

highscores = []

print("\n----------------------------------------\nWelcome to the Number Guessing Game!\n----------------------------------------\n")

def start_game():
    number_of_tries = [] #This is the number of tries the user has made.
    X = random.randint(1,10) #Used help menu to find this. X is the answer to the game.
    while True:
        guess = input("Pick a number between 1 and 10: ")
        try:
            guess = int(guess)
            if guess > 10:
                raise ValueError()
            if guess < 1:
                raise ValueError()
        except ValueError:
            print("Oops, I didn't understand. Please enter a value from 1 - 10.")
        else:    
            number_of_tries.append(guess)
            if guess > X:
                print("It is a lower number!")
            elif guess < X:
                print("It is a higher number!")
            elif guess == X:
                score = len(number_of_tries)
                highscores.append(score)
                print("\nYay! You got it! It took you {} tries.".format(len(number_of_tries)))
                break
start_game()

while True:
    try_again = input("Would you like to play again? (yes/no): ")
    if try_again.lower() == 'yes':
        print("\nThe Highscore is: {}\n".format(min(highscores)))
        
        #I could'nt find a way to output the lowest item from the list I created from what we learned. I know we did not learn the 'min' function yet. I used this as a reference: https://www.geeksforgeeks.org/python-program-to-find-smallest-number-in-a-list/
        
        start_game()
    elif try_again.lower() == 'no':
        print("Thank you for playing!")
        break
    elif try_again.lower() != 'no' or 'yes':
        print("Oops, I didn't understand that. Please try again.")
