# Build a number guessing game, in which the user selects a range

# Importing Libraries
import random
import math

# Getting input from the user
def userInput(msg):
    while True:
        try:
            print(msg, end=" : ")
            guess = int(input())
            return guess
        except:
            print("Please enter a valid number.")


def play(number):
    guess = 0
    count = 0
    while True:
        count += 1
        while True:
            try:
                guess = int(input())
                break
            except:
                print("Please Enter a number")
        if guess > number:
            print("Try Again! You guessed too high.")
        elif guess < number:
            print("Try Again! You guessed too small.")
        else:
            return count
        

# Calculating the minimum number of guesses that takes to guess the number.
def algo(range1, range2):
    return round(math.log(range2 - range1 + 1, 2))


def main():
    # Getting the range A
    rangeA = userInput("Enter the range A")
    # Getting the range B
    rangeB = userInput("Enter the range B")
    # Getting a random number 
    RandomNumber = random.randint(rangeA, rangeB)
    NumberOfGuesses = algo(rangeA, rangeB)
    print("Random number is created start guessing.")
    # Getting the number of gusses
    TotalNumberofGusses = play(RandomNumber)
    print("Total Number of Guesses = " + str(TotalNumberofGusses))
    if TotalNumberofGusses <= NumberOfGuesses:
        print("Congratulations you passed.")
    else: 
        print("The limit is" + str(NumberOfGuesses) + "gusess.\n Better Luck Next time!")


if __name__ == "__main__" :
    main()