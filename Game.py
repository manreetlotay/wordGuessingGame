class Game:

    def __init__(self):
        self.gameNumber = 0
        self.status = None
        self.badGuesses = 0
        self.missedLetters = 0
        self.currentWord = None
        self.score = 0
    
    # Getters
    def getCurrentWord(self):
        return self.currentWord

    def getGameNumber(self):
        return self.gameNumber

    def getStatus(self):
        return self.status

    def getBadGuesses(self):
        return self.badGuesses

    def getMissedLetters(self):
        return self.missedLetters
    
    def getScore(self):
        return self.score
    

    # Setters
    def setGameNumber(self, newGameNumber):
        self.gameNumber = newGameNumber
    
    def setStatus(self, newStatus):
        self.status = newStatus

    def setBadGuesses(self, addBadGuess):
        self.badGuesses += addBadGuess

    def setMissedLetters(self, newMissedLetters):
        self.missedLetters += newMissedLetters

    def setCurrentWord(self, newCurrentWord):
        self.currentWord = newCurrentWord

    def setScore(self, newScore):
        self.score = newScore

    # letter to frequency
    def getLetterFrequency(self, letter):
         # store letter-frequency pair in dictionary
        letterFrequency = {'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70,
                    'f': 2.23, 'g': 2.02, 'h': 6.09, 'i': 6.97, 'j': 0.15,
                    'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51,
                    'p': 1.93, 'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06,
                    'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97, 
                    'z': 0.07}
        
        frequency = letterFrequency.get(letter, 0)
        return frequency
        

    # calculate score for each game
    def gameScore(self, currentWord, currentGuess, lettersGuessed):

        sum = 0
        penalty = 0

        # case 1: success without requesting letters and without bad guesses
        if self.badGuesses == 0 and not lettersGuessed and self.status == "Success":
            for letter in currentWord:
                self.score += self.getLetterFrequency(letter)

        # case 2: success by requesting correct and maybe incorrect letters (penalty included for wrong guesses)
        elif self.status == "Success":
            for position, letter in enumerate(currentGuess):
                if letter == '-':
                    # Get the corresponding letter in currentWord
                    coveredLetter = currentWord[position]
                    # Add the frequency of the hidden letter to the total frequency
                    sum += self.getLetterFrequency(coveredLetter)
            if self.missedLetters != 0:
                self.score = sum/self.missedLetters
            penalty = self.score*(0.1*self.badGuesses)
            self.score -= penalty

        # case 3: gave up immediately
        elif self.status == "Gave up" and not lettersGuessed and self.badGuesses == 0:
            for letter in currentWord:
                self.score += -self.getLetterFrequency(letter)

        # case 4: gave up after requesting correct and incorrect letters
        elif self.status == "Gave up":
            for position, letter in enumerate(currentGuess):
                if letter == '-':
                    # Get the corresponding letter in currentWord
                    coveredLetter = currentWord[position]
                    # sum the frequencies of the covered letter
                    self.score += -self.getLetterFrequency(coveredLetter)
           
        return round(self.score, 2)













