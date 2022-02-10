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


def print_score(score):           
    if score == 1:
        print("You guessed it in only {} guess, no beating that!\n".format(score))
        sleep()
    else:
        print("You guessed it in {} guesses!\n".format(score))
        sleep()


def evaluate_high_score(score, high_score):
    if high_score == 9999:
        print("You have set the high score at: {}\nCongratulations!\n".format(score))
        return score
    else: 
        print("The previous high score was: {}...".format(high_score))
        if score < high_score:
            print("But it looks like you just beat it with your score of: {}\nGreat Job!\n".format(score))
            sleep()
            return score
        elif score == high_score:
            print("It looks like you tied the high score at: {}.\nSo close!\n".format(high_score))
            sleep()
            return high_score
        else:
            print("And the record is still intact!\nBetter luck next time!\n")
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
                raise GuessOutOfRangeError("\n{} is not between 1 and 10. Try Again.\n".format(guess))
            elif guess > answer:
                raise GuessTooHigh("\nThe secret number is lower.\n")
            elif guess < answer:
                raise GuessTooLow("\nThe secret number is higher.\n")
            break
        except ValueError:
            print("\n{} not a valid number, please try again.\n".format(guess))            
        except GuessOutOfRangeError as err:
            print(err)
        except GuessTooHigh as err:
            wrong_guess_counter += 1
            print(err)
        except GuessTooLow as err:
            wrong_guess_counter += 1
            print(err)

    print("\nYou Got it!\n")
    sleep()        
    print_score(wrong_guess_counter)
    sleep()
    return wrong_guess_counter


def continue_game(num_rounds):
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
                    print("You played for {} round.\n".format(num_rounds))
                else:
                    print("You played for {} rounds.\n".format(num_rounds))
                sleep()
                print("Game ending. Thank you for playing.")
                sleep()
                return False
                
   
def start_game():
    keep_playing = True
    high_score = 9999
    rounds = 1    
    while keep_playing:       
        print(("="*40) , "> Welcome To The Number Guessing Game <" , ("="*40))
        if rounds == 1:
            print("\nThe objective of this game is to guess a random number between 1 and 10.")
            sleep()
            print("When you finally guess the number correctly we will let you know how many guesses it took.\n")
            sleep()        
        solution = random.randint(1,10)               
        if high_score != 9999:
            print("The high score is currently: {}.\n".format(high_score))
            sleep()   
        player_score = evaluate_guess(solution)
        high_score = evaluate_high_score(player_score, high_score)
        keep_playing = continue_game(rounds)
        rounds += 1


start_game()