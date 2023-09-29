from random import randint
import player

def assign_word():
    words = ["hello", "bye", "test", "hang", "man"]
    word = words[randint(0, len(words)-1)]
    return word


def game(entity):
    guesses = 5
    word = list(assign_word())
    print(word)
    while guesses > 0 and len(word) > 0:
        letter = entity.guess_letter()
        print(letter)
        if letter not in word:
            print("Wrong")
            guesses -= 1
            entity.score_counter(-1)
        if letter in word:
            print("Correct")
            remove_items(word, guesses)
            entity.score_counter(2)
    
    if guesses == 0:
        print("Out Of Guesses")
    
    if len(word) == 0:
        print("Guessed Word Correct")


def remove_items(test_list, item):
    res = [i for i in test_list if i != item]
    return res

