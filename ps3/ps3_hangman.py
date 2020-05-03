# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(dic):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if dic == {}:
      print('Congrats! You won!')
      return True
    else:
      return False



def getGuessedWord(secretWord, lettersGuessed,dic):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    right = list(secretWord)
    for key in dic.keys():
      for pos in dic.get(key):
        right[pos] = '-'
    print('\n\n')
    print(''.join(right))
    
    valid = False
    while not valid:
      guess = input('\nGive me a shot!')
      if guess in lettersGuessed:
        print('You have used this letter before!')
      else:
        valid = True
    lettersGuessed.append(guess)

    if guess in dic.keys():
      print('You got',len(dic.get(guess)),'!\n\n')
      del(dic[guess])
    else:
      print('Sorry! Not this time!\n\n')
    return (lettersGuessed,dic)

        



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    if len(lettersGuessed) == 0:
      print('You still made no guesses...')
    else:
      print("You have already used the following letters: ",lettersGuessed)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('\n\n\n\nYou have 8 guesses to find the correct word!')
    print('Correct word has',len(secretWord),'letters. \n')
    lettersGuessed = []
    dic = {}
    for i,c in enumerate(secretWord):
      if dic.get(c,0) == 0:
        dic[c] = [i]
      else:
        dic.get(c).append(i)
    number_letters = len(dic.keys())
    while (len(lettersGuessed)- (number_letters-len(dic.keys())))< 8 and not isWordGuessed(dic):
      getAvailableLetters(lettersGuessed)
      print('You still have ',8-len(lettersGuessed)- (number_letters-len(dic.keys())),'oportunities...')
      (lettersGuessed, dic) = getGuessedWord(secretWord, lettersGuessed,dic)
    if dic != {}:
      print('Sorry! You lost!')
      print('The correct word is: ',secretWord,'!!')


secretWord = chooseWord(wordlist)
hangman(secretWord)
