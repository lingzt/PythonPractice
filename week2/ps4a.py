# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    
    For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, 
    then multiply by len('weed') to get (4+1+1+2)*4 = 32). 
    Be sure to check that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!
    """
    score = 0
    letter = ""
    letterPoits = 0
    for letter in word:
        letterPoits = SCRABBLE_LETTER_VALUES[letter.lower()]
        score += letterPoits
    score *= len(word)
    if len(word) == n:
        score += 50
    return score
    




#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    
        updated = hand.copy()
    for i in word:
        updated[i] = updated[i] - 1
    return updated
    
    """
    updated = hand.copy()
    for key in list(updated):
        for letter in word:
            if key == letter:
                if updated[key]>0:
                    updated[key] -= 1
    return updated




#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    if word not in wordList:
        return False
    hand = hand.copy()
    for letter in word:
        if not hand.get(letter, 0):
            return False
        else:
            hand[letter] = hand.get(letter, 0) - 1
    return True      



#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    length = 0
    for key in list(hand):
        length += hand[key]
    return length




def playHand(hand, wordList, n):
    # Keep track of the total score
    score = 0
    # As long as there are still letters left in the hand:
    
        # Display the hand
    aString = ''
    for letter in hand.keys():
        for j in range(hand[letter]):
            aString += (' ' +letter)
    print("Current Hand: "+ aString)
        
        # Ask user for input
    word = input('Enter word, or a "." to indicate that you are finished: ')      
        # If the input is a single period:
    if word == '.':
            # End the game (break out of the loop)
        print('Goodbye! Total score:  '+str(score)+'  points.')
        return          
        # Otherwise (the input is not a single period):
    else:
            # If the word is not valid:
        if not isValidWord(word, hand, wordList):
                # Reject invalid word (print a message followed by a blank line)
            print('Invalid word, please try again.'+'\n')

            # Otherwise (the word is valid):
        else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            score += getWordScore(word, n)
            print('" '+word+' " earned '+str(getWordScore(word, n))+' points. Total:'+str(score)+' points \n')
                # Update the hand 
        hand = updateHand(hand, word)
        playHand(hand, wordList, n)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Run out of letters. Total score: '+str(score)+' points.')


#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    userInput = ''
    lastHand = ''
    while userInput != 'e':
        userInput = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        # If the user inputs 'n', let the user play a new (random) hand.
        if userInput == 'n':
            userChoice = input('Enter u to have yourself play, c to have the computer play:')
            if userChoice == 'u':
                lastHand = dealHand(HAND_SIZE)
                playHand(lastHand, wordList, HAND_SIZE)
            elif userChoice == 'c':
                lastHand = dealHand(HAND_SIZE)
                compPlayHand(lastHand, wordList, HAND_SIZE)
            else:
                print('Invalid command.')
            continue
        # If the user inputs 'r', let the user play the last hand again.
        elif userInput == 'r':
            if lastHand == '':
                print('You have not played a hand yet. Please play a new hand first!')
                continue
            else:
                userChoice = input('Enter u to have yourself play, c to have the computer play:')
                if userChoice == 'u':
                    lastHand = dealHand(HAND_SIZE)
                    playHand(lastHand, wordList, HAND_SIZE)
                elif userChoice == 'c':
                    lastHand = dealHand(HAND_SIZE)
                    compPlayHand(lastHand, wordList, HAND_SIZE)
                else:
                    print('Invalid command.')
                continue
        elif userInput == 'e':
            break
        else:
            print('Invalid command.')
            continue
   



#
# Build data structures used for entire session and play game
#

wordList = loadWords()

playGame(wordList)

#print(isValidWord(hammer, {'h': 1, 'e': 1, 'm': 2, 'r': 1, 'a': 1}, <edX internal wordList>))
#print(" should equal to")
#print(True)
