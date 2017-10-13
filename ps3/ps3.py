import math
import random
import functools

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	
def get_word_score(word, n):
    return (sum(map(lambda x: SCRABBLE_LETTER_VALUES[x.lower()],word))) * max(7 * len(word) - 3 * (n - len(word)),1)

def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')
    print()

def deal_hand(n):
    hand={}
    num_vowels = int(math.ceil(n / 3))
    hand["*"] = 1
    
    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

def update_hand(hand, word):
    return {k: v - word.lower().count(k) for k, v in hand.items()}

def is_valid_word(word, hand, word_list):
    return any(word.lower().replace("*", v) in word_list for v in VOWELS) and all(c in hand and hand[c] >= word.lower().count(c) for c in word.lower())

def calculate_handlen(hand):
    return functools.reduce((lambda x, y: x + hand[y]), hand.keys(), 0)

def play_hand(hand, word_list):
    total_score = 0
    while(calculate_handlen(hand) > 0):
        print("Current Hand: ", end='')
        display_hand(hand)
        word = input("Enter word, or \"!!\" to indicate that you are finished: ")
        if(word == "!!"):
            break
        elif(is_valid_word(word ,hand, word_list)):
            word_score = get_word_score(word,calculate_handlen(hand))
            total_score += word_score
            hand = update_hand(hand, word)
            print("\""+word+"\" earned +"+str(word_score)+" points. Total: "+str(total_score))
            print()
        else:
            print("This is not a valid word. Please choose another word.")
    if(calculate_handlen(hand) == 0):
        print("Ran out of letters.")
    print("Total score for this hand: "+str(total_score))
    return total_score


def substitute_hand(hand, letter):
    return dict(zip(map(lambda k: k if k != letter else random.choice(list(filter(lambda x: x not in hand.keys(),VOWELS+CONSONANTS))), hand.keys()), hand.values()))

def play_game(word_list):
    total_score_over_all_hand = 0
    total_number_of_hands = int(input("Enter total number of hands: "))
    for x in range(total_number_of_hands):
        hand = deal_hand(HAND_SIZE)
        print("Current Hand: ", end='')
        display_hand(hand)
        if(input("Would you like to substitute a letter? ") == "yes"):
            hand = substitute_hand(hand, input("Which letter would you like to replace: "))
        while(True):
            total_score_for_current_hand = play_hand(hand, word_list)
            print("----------")
            if(input("Would you like to replay the hand? ") == "no"):
                break
        total_score_over_all_hand += total_score_for_current_hand
    print("Total score over all hands: "+str(total_score_over_all_hand))

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)