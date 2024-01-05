#Author: Jacob Neaderland
from random import seed
from random import randint
start = input("Would you like to play hangman? y/n ") # Used to start the hangman game
if start == "y": # Also used to start the game
    seeed = input("Pick a number 1-10 ") # To make it more random
    seedi = int(seeed) # To make it more random
    while not 1 <= seedi <= 10: # To make it more random
        seeed = input("Pick a number 1-10 ") # To make it more random
        seed(seedi) # To make it more random
    seedi = int(seeed) # To make it more random
    seed(seedi) # To make it more random
    wordlist = ["Pseudonym", "Sunshine", "Bicycle", "Serendipity", "Tornado", "Raspberry", "Harmony", "Fragrance", "Telescope", "Chocolate", "Adventure"] # List of all of the possible words
    randword = wordlist[randint(0, 10)] # Picking the word
    print () # To clear the screen
    print () # To clear the screen
    print () # To clear the screen
    print () # To clear the screen
    print () # To clear the screen
    print () # To clear the screen
    print () # To clear the screen
    print () # To clear the screen
else:
    exit () # Closes the code if you don't want to play
def hangman(word): # The function
    print(word) # So that I dont have to actually play hangman while testing
    wordl = list(word.lower())  # Convert the word to lowercase
    wrong = 0 # Ammount of incorrect guessed
    wordg = word.lower()  # Convert the guessed word to lowercase
    dash = [] # Creates an empty list to display the num of dashes
    gletter = [] # Used to store letters that have been guessed
    lenw = len(word) # Also used for making dashes
    letternum = 1 # Used to store the num of attempts
    worda = word.lower # Used for the win condition
    print ("This is attempt number", letternum, "!") # Shows the player what attempt they are on
    letternum = letternum + 1
    for _ in range(lenw): # Making what the player would see
        dash.append("_") # Making what the player would see
    print(" ".join(dash)) # Showing the player the num of letters
    while worda != "-"*len(word)  : # Sets the win condition
        dasha = dash
        guess = input("What's your guess? ").lower()  # Convert the guessed letter to lowercase
        wordf = wordg.find(guess) # Seeing if their guess was correct
        if wordf != -1: # Checks to see if the guess was in the word
            dash[wordf] = word[wordf]  # Keep the original case in the displayed word
            wordg = wordg.replace(guess, "-", 1) # Setup so that the code can tell if there are more than one of the same letter
            worda = wordg.replace(guess, "-", 1)
            while wordg.find(guess) != -1: # Checking if there are more than one of the same letter
                wordf = wordg.find(guess) # Repeating the check to see if their guess was correct
                dash[wordf] = word[wordf] # Keep the original case in the displayed word
                wordg = wordg.replace(guess, "-", 1) # Setup so that the code can tell if there are more than one of the same letter
                worda = wordg.replace(guess, "-", 1)
            print ("This is attempt number", letternum, "!") # Shows the player what attempt they are on
        else: # Start of incorrect guesses
            wrong = wrong + 1 # Adds 1 to the incorrect to display the correct hangman
            if wrong == 7: # Lose
                print("  O  ")
                print(" /|\ ")
                print("  |  ")
                print(" / \ ")
                print("You lose!!!!")
                exit () # Closes the program
            if wrong == 6:
                print("  O  ")
                print(" /|\ ")
                print("  |  ")
                print(" / ")
            elif wrong == 5:
                print("  O  ")
                print(" /|\ ")
                print("  |  ")
            elif wrong == 4:
                print("  O  ")
                print(" /|\ ")
            elif wrong == 3:
                print("  O  ")
                print("  |\ ")
            elif wrong == 2:
                print("  O  ")
                print("  | ")
            elif wrong == 1:
                print("  O  ")
        print(" ".join(dash)) # Shows as a word instead of a list of numbers
    print("Congrats, the word was", word, "!!!") # Congrats on winning
hangman(randword) # Starts the function
again = input("Would you like to play again? y/n ") # Allows for more play bc of the randint
if again == "y": # Allows for more play bc of the randint
    randword = wordlist[randint(0, 10)] # Allows for more play bc of the randint
    hangman(randword) # Restarts it
else:
    exit () #Closes the function if no more play is wanted