"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""
import random
import time

class GuessOutOfRangeError(Exception):
    pass
class GuessTooLow(Exception):
    pass
class GuessTooHigh(Exception):
    pass
class AlreadyGuessed(Exception):
    pass



def sleep():
    '''Function used to sleep a line for half a second.'''
    time.sleep(.5)


def print_score(score):           
    if score == 1:
        print(f"You guessed it in only {score} guess, no beating that!\n")
        sleep()
    else:
        print(f"You guessed it in {score} guesses!\n")
        sleep()


def evaluate_high_score(score, high_score):
    if high_score == 9999:
        print(f"You have set the high score at: {score}\nCongratulations!\n")
        return score
    else: 
        print(f"The previous high score was: {high_score}...")
        if score < high_score:
            print(f"But it looks like you just beat it with your score of: {score}\nGreat Job!\n")
            sleep()
            return score
        elif score == high_score:
            print(f"It looks like you tied the high score at: {high_score}.\nSo close!\n")
            sleep()
            return high_score
        else:
            print("And the record is still intact!\nBetter luck next time!\n")
            sleep()
            return high_score  


def get_guess():    
    while True:                
        try:
            guess = input("Guess a number between 1 and 10:\n")
            guess = int(guess) #I don't like doing it this way, but I haven't found an answer yet                             
            if guess < 1 or guess > 10:
                raise GuessOutOfRangeError(f"\n{guess} is not between 1 and 10. Try Again.\n")
        except UnboundLocalError:
            print("Define Guess First")
        except ValueError:            
            print(f"\n{guess} is not a valid number, please try again.\n")
        except GuessOutOfRangeError as err:
            print(err)
        else:
            return guess


def guess_in_history(history):
    while True:        
        guess = get_guess()        
        try:
            if guess in history:
                raise AlreadyGuessed(f"{guess} has already been guessed, please try again")
            else:
                history.append(guess)
                break
        except AlreadyGuessed as err:
            print(err)
    return guess, history


def evaluate_guess(answer):        
    guesses = []
    while True: 
        try:
            guess, guesses = guess_in_history(guesses)
            if guess > answer:                
                raise GuessTooHigh("\nThe secret number is lower.\n")
            elif guess < answer:                
                raise GuessTooLow("\nThe secret number is higher.\n")                
            break        
        except GuessTooHigh as err:
            print(err)
        except GuessTooLow as err:
            print(err)            
    print("\nYou Got it!\n")
    sleep()        
    print_score(len(guesses))
    sleep()
    return len(guesses), guesses


def continue_game(num_rounds, round_history):
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
                sleep()
                return True
            elif question.lower() == "n":
                if num_rounds == 1:
                    print(f"You played for {num_rounds} round.\n")
                else:
                    print(f"You played for {num_rounds} rounds.\n")
                sleep()
                print("Game ending. Thank you for playing.")                
                sleep()
                return False
                
   
def start_game():
    keep_playing = True
    high_score = 9999
    player_score = 0
    round_history = [] #Not really using this yet, but it is keeping track of all of the player guesses.       
    while keep_playing:       
        print(("="*40) , "> Welcome To The Number Guessing Game <" , ("="*40))
        if player_score == 0:
            print("\nThe objective of this game is to guess a random number between 1 and 10.")
            sleep()
            print("When you finally guess the number correctly we will let you know how many guesses it took.\n")
            sleep()        
        solution = random.randint(1,10)               
        if high_score != 9999:
            print(f"The high score is currently: {high_score}.\n")
            sleep()   
        player_score, guess_history = evaluate_guess(solution)
        round_history.append(guess_history)
        high_score = evaluate_high_score(player_score, high_score)
        keep_playing = continue_game(player_score, round_history)
    #return round_history, high_score Could use this to output the high score and player results for use in another function.
        


start_game()