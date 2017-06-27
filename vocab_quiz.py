from urllib2 import urlopen
from bs4 import BeautifulSoup
import random


def loading_words():
    #Load data
    content = urlopen('https://www.randomlists.com/random-vocabulary-words')
    #content = urlopen('http://www.sport-histoire.fr/en/Geography/Countries_by_alphabetical_order.php')
    xml = content.read()
    content.close()
    soup = BeautifulSoup(xml, "lxml")
    #Load words
    wordspans = soup.findAll("span", { "class" : "support" })
    words = [span.string for span in wordspans]
    print words
    #Load tips
    tipspans = soup.findAll("span", { "class" : "subtle" })
    tips = [tip.string for tip in tipspans]
    #return list of tuples
    words_tips = dict(zip(words, tips))
    return words_tips

def play_round():
    word_tip_dict = loading_words()
    print word_tip_dict
    word_to_guess = random.choice(list(word_tip_dict.keys()))
    print('\n\nWhat does the word "{}" mean?'.format(word_to_guess))
    guess_counter = 0
    numerator = 0
    result_list = []
    #Create print with answer possibilities
    for word in word_tip_dict:
        numerator += 1
        result_list.append(word)
        print('{}. {}'.format(numerator, word_tip_dict[word]))
    #Guess loop
    while True:
        guess_counter += 1
        answer = int((input('\nPlease enter the number of your answer?>   ')))
        if word_to_guess == result_list[answer-1]:
            print('\nYou guessed right in {} guesses!!! Bravo!'.format(guess_counter))
            break
        else:
            print('try again!')


# Main game
print('Welcome to WordGuess! ')
while True:
    play_round()
    continue_playing = input('\nPress 1 to play one more round any other key to exit ? >   ')
    if continue_playing != 1:
        break
    print('-----------------------------------------------------------')