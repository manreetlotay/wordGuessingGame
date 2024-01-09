from StringDatabase import StringDatabase
from Game import Game
from tabulate import tabulate
import random
import os
import sys

class Guess: 

    def __init__(self):
        self.validOptions = ['g', 't', 'l', 'q']
        self.words = StringDatabase.readFile()
        self.gameNum = 1
        self.gamesPlayed = []

    def printMenuTest(self, currentWord, currentGuess, lettersGuessed):
        print("++")
        print("++ The great guessing game")
        print("++\n")
        print("Current word: ", currentWord)
        print("Current guess: ", currentGuess)
        print("Letters guessed: ", ' '.join(lettersGuessed))
        print("\ng = guess, t = tell me, l = guess a letter, q = quit\n")

    def printMenuPlay(self, currentGuess, lettersGuessed):
        print("++")
        print("++ The great guessing game")
        print("++\n")
        print("Current guess: ", currentGuess)
        print("Letters guessed: ", ' '.join(lettersGuessed))
        print("\ng = guess, t = tell me, l = guess a letter, q = quit\n")
        

    # prompt user to continue and clear screen
    def continueGame(self):
        os.system("pause")
        os.system('cls' if os.name == 'nt' else 'clear')

    # update current Guess when user guesses one of the letters correctly
    def updateCurrentGuess(self, currentWord, currentGuess, letter):
        currentGuessList = list(currentGuess)
        
        # Replace each occurrence of the correctly guessed letter in currentGuess
        for i in range(len(currentWord)):
            if currentWord[i] == letter:
                currentGuessList[i] = letter
        
        return ''.join(currentGuessList)

    # message to print when word is guessed correctly
    def rightGuess(self):
        print("\n@@")
        print("@@ FEEDBACK: You're right, Einstein!")
        print("@@\n")

    # message to print when word is not guessed correctly
    def wrongGuess(self):
        print("\n@@")
        print("@@ FEEDBACK: Try again, Loser!")
        print("@@\n")

    # message to print when user gives up
    def tellMe(self, currentWord):
        print("\n@@")
        print("@@ FEEDBACK: You really should have guessed this...'", currentWord, "'")
        print("@@\n")

    # message to print when a letter is guessed correctly
    def rightLetter(self, currentWord, letter):
        print("\n@@")
        print("@@ FEEDBACK: Woo hoo, you found ", currentWord.count(letter) , " letters")
        print("@@\n")

    # message to print when a letter is not guessed correctly
    def wrongLetter(self):
        print("\n@@")
        print("@@ FEEDBACK: Not a single match, genius")
        print("@@\n")

    # loop through all the games played and display each game's attributes in a table
    def gameReport(self):
        # only display report if there were games played
        finalScore = 0

        if self.gamesPlayed: 
            print("++")
            print("++ Game Report")
            print("++\n")

            game_data = []

            for game in self.gamesPlayed:
                game_data.append([game.gameNumber, game.currentWord, game.status, game.badGuesses, game.missedLetters, game.score])

            headers = ["Game", "Word", "Status", "Bad Guesses", "Missed Letters", "Score"]
            print(tabulate(game_data, headers=headers, tablefmt="simple", colalign=("left", "left", "left", "left", "left", "left")))

            for game in self.gamesPlayed:
                finalScore += game.score

            # 2 decimal places
            finalScore = round(finalScore, 2)

            print("\nFinal Score: {:.2f}\n".format(finalScore))


    # user keeps guessing new words until they choose to quit (test mode)
    def guessGameTest(self):

        while True:

            # instantiate a new game with a new word after a word has been guessed correctly
            newGame = Game()
            newGame.setGameNumber(self.gameNum)
            # increment game number for next game
            self.gameNum += 1
            newGame.currentWord = random.choice(self.words)
            currentGuess = "----"
            lettersGuessed = []

            while True:
                self.printMenuTest(newGame.currentWord, currentGuess, lettersGuessed)
                option = input("Enter option: ")

                if option not in self.validOptions:
                    print("\nInvalid Option. Please re-enter\n")
                    continue

                if option == 'g':
                    wordGuess = input("\nMake your guess: ")

                    # if user guesses word correctly, update the status of current game and add it to gamesPlayed list... a new game begins
                    if wordGuess.lower() == newGame.currentWord.lower():
                        self.rightGuess()
                        newGame.setStatus("Success")
                        # update game score
                        newGame.setScore(newGame.gameScore(newGame.currentWord, currentGuess, lettersGuessed))
                        self.gamesPlayed.append(newGame)
                        self.continueGame()
                        break
                    else:
                        # update current game's count of bad guesses
                        self.wrongGuess()
                        newGame.setBadGuesses(1)
                        self.continueGame()

                # update current game's status if user gives up...add game to games played list...a new game begins after
                elif option == 't':
                    self.tellMe(newGame.currentWord)
                    newGame.setStatus("Gave up")
                    # update game score
                    newGame.setScore(newGame.gameScore(newGame.currentWord, currentGuess, lettersGuessed))
                    self.gamesPlayed.append(newGame)
                    self.continueGame()
                    break

                elif option == 'l':
                    letter = input("\nEnter a letter: ")
                    if letter.lower() in newGame.currentWord.lower():
                        self.rightLetter(newGame.currentWord, letter)
                        lettersGuessed.append(letter)
                        currentGuess = self.updateCurrentGuess(newGame.currentWord, currentGuess, letter)
                        self.continueGame()
                    else:
                        # if user guesses wrong letter, add letter to guessedLetters list and set missedLetters
                        self.wrongLetter()
                        newGame.setMissedLetters(1)
                        lettersGuessed.append(letter)
                        self.continueGame()

                elif option == 'q':
                    # display game report if user choses to quit
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.gameReport()
                    return



    # user keeps guessing new words until they choose to quit (play mode)
    def guessGamePlay(self):

        while True:

            # instantiate a new game with a new word after a word has been guessed correctly
            newGame = Game()
            newGame.setGameNumber(self.gameNum)
            # increment game number for next game
            self.gameNum += 1
            newGame.currentWord = random.choice(self.words)
            currentGuess = "----"
            lettersGuessed = []

            while True:
                self.printMenuPlay(currentGuess, lettersGuessed)
                option = input("Enter option: ")

                if option not in self.validOptions:
                    print("\nInvalid Option. Please re-enter\n")
                    continue

                if option == 'g':
                    wordGuess = input("\nMake your guess: ")

                    # if user guesses word correctly, update the status of current game and add it to gamesPlayed list... a new game begins
                    if wordGuess.lower() == newGame.currentWord.lower():
                        self.rightGuess()
                        newGame.setStatus("Success")
                        # update game score
                        newGame.setScore(newGame.gameScore(newGame.currentWord, currentGuess, lettersGuessed))
                        self.gamesPlayed.append(newGame)
                        self.continueGame()
                        break
                    else:
                        # update current game's count of bad guesses
                        self.wrongGuess()
                        newGame.setBadGuesses(1)
                        self.continueGame()

                # update current game's status if user gives up...add game to games played list...a new game begins after
                elif option == 't':
                    self.tellMe(newGame.currentWord)
                    newGame.setStatus("Give up")
                    # update game score
                    newGame.setScore(newGame.gameScore(newGame.currentWord, currentGuess, lettersGuessed))
                    self.gamesPlayed.append(newGame)
                    self.continueGame()
                    break

                elif option == 'l':
                    letter = input("\nEnter a letter: ")
                    if letter.lower() in newGame.currentWord.lower():
                        self.rightLetter(newGame.currentWord, letter)
                        lettersGuessed.append(letter)
                        currentGuess = self.updateCurrentGuess(newGame.currentWord, currentGuess, letter)
                        self.continueGame()
                    else:
                        # if user guesses wrong letter, add letter to guessedLetters list and set missedLetters
                        self.wrongLetter()
                        newGame.setMissedLetters(1)
                        lettersGuessed.append(letter)
                        self.continueGame()

                elif option == 'q':
                    # display game report if user choses to quit
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.gameReport()
                    return





