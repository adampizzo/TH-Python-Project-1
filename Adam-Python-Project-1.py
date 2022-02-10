"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""
class GuessOutOfRangeError(Exception):
    pass
class GuessTooLow(Exception):
    pass
class GuessTooHigh(Exception):
    pass

import random
import time

def sleep():
    time.sleep(.75)

def determine_score(score):           
    if score == 1:
        print("You guessed it in only {} guess, no beating that!\n".format(score))
        sleep()
    else:
        print("You guessed it in {} guesses!\n".format(score))
        sleep()


def set_high_score(score, high_score):
    print("The previous high score was: {}...".format(high_score))
    if score < high_score:
        print("But it looks like you just beat it with your score of: {}\nGreat Job!\n".format(score))
        sleep()
        return score
    else:
        print("And the record is still intact!\nBetter luck next time!")
        sleep()
        return high_score   


def evaluate_guess(answer):    
    wrong_guess_counter = 1
    while True:        
        try:
            guess = int(input("Guess a number between 1 and 10:\n"))            
            if type(guess) != int:
                raise ValueError
            elif guess < 1 or guess > 10:
                raise GuessOutOfRangeError("Oh no! That guess was not between 1 and 10.")
            elif guess > answer:
                raise GuessTooHigh("It's lower")
            elif guess < answer:
                raise GuessTooLow("It's higher")
            break
        except ValueError:
            print("That guess was not a valid number, please try again.")            
        except GuessOutOfRangeError as err:
            print(err)
        except GuessTooHigh as err:
            wrong_guess_counter += 1
            print(err)
        except GuessTooLow as err:
            wrong_guess_counter += 1
            print(err)

    print("Got it")
    sleep()        
    determine_score(wrong_guess_counter)
    sleep()
    return wrong_guess_counter

            



def continue_game():
    while True:        
        try:
            question = input("Do you want to play the game again? (Y/N)\n")

            if question.lower() != "n" and question.lower() != "y":
                raise ValueError("Invalid input. Please enter 'Y' for yes, or 'N' for no.")
        except ValueError as err:
                print(err)
        else:
            if question.lower() == "y":
                print("Great! New game starting shortly!\n")
                time.sleep(1)
                return True
            elif question.lower() == "n":
                print("Thank you for playing! Game ending shortly!")
                time.sleep(1)
                return False
                
   
def start_game():
    keep_playing = True
    high_score = 10
    
    while keep_playing:
        #1. Display an intro/welcome message to the player.
        print(("="*40) , "> Welcome To The Number Guessing Game <" , ("="*40) , "\nThe objective of this game is to guess a random number between 1 and 10.")
        sleep()
        print("When you finally guess the number correctly we will let you know how many guesses it took.")
        #2. Store a random number as the answer/solution.
        solution = random.randint(1,10)
        print(solution)
        #3. Continuously prompt the player for a guess.
        
        player_score = evaluate_guess(solution)
        high_score = set_high_score(player_score, high_score)
        keep_playing = continue_game()

        



    #   a. If the guess greater than the solution, display to the player "It's lower".

    #   b. If the guess is less than the solution, display to the player "It's higher".

    #4. Once the guess is correct, stop looping, inform the user they "Got it" and show how many attempts it took them to get the correct number.

    #5. Let the player know the game is ending, or something that indicates the game is over. ( You can add more features/enhancements if you'd like to. )

    
    



# Kick off the program by calling the start_game function.
start_game()