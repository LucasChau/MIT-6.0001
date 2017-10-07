import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_random_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    return all(letter in letters_guessed for letter in secret_word)

def get_guessed_word(secret_word, letters_guessed):
    return ''.join(list(map(lambda x: x if x in letters_guessed else '_ ', secret_word)))

def get_available_letters(letters_guessed):
    return ''.join(filter(lambda x: x not in letters_guessed,string.ascii_lowercase))

def hangman(secret_word):
    guesses = 6
    warnings = 3
    letters_guessed = []
    guessed_word = ""
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+str(len(secret_word))+" letters long.")
    print("You have "+str(warnings)+" warnings left.")
    print("------------")
    while(guesses > 0 and not is_word_guessed(secret_word, letters_guessed)):
        print("You have "+str(guesses)+" guesses left.")
        print("Available letters: "+get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ")
        if(str.isalpha(guess) and str.lower(guess) not in letters_guessed):
            guess = str.lower(guess)
            letters_guessed.append(guess)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            if(guess in secret_word):
                print("Good guess: "+guessed_word)
            else:
                if(guess in ['a','e','i','o','u']):
                    guesses -= 2
                else:
                    guesses -= 1
                print("Oops! That letter is not in my word: "+guessed_word)
        else:
            if(not str.isalpha(guess)):
                reason = "Oops! That is not a valid letter."
            else:
                reason = "Oops! You've already guessed that letter."
            if(warnings == 0):
                guesses -= 1
                print(reason+" You have no warnings left so you lose one guess: "+guessed_word)
            if(warnings > 0):
                warnings -= 1
                print(reason+" You have "+str(warnings)+" warnings left: "+guessed_word)
        print("------------")
    if(is_word_guessed(secret_word, letters_guessed)):
        print("Congratulations, you won!")
        print("Your total score for this game is: "+str(guesses * len(set(secret_word))))
    else:
        print("Sorry, you ran out of guesses. The word was "+secret_word+".")

def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(" ","")
    return len(my_word) == len(other_word) and all(c == "_" or (c == other_word[i] and my_word.count(c) == other_word.count(c)) for i,c in enumerate(my_word))



def show_possible_matches(my_word):
    matches = list(filter(lambda w: match_with_gaps(my_word,w),wordlist))
    return " ".join(matches) if len(matches) > 0 else "No matches found"



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass

if __name__ == "__main__":
    secret_word = choose_random_word(wordlist)
    #hangman(secret_word)