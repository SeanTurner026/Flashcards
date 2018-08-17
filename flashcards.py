"""
flashcard.py reads a json file containing flashcards, and presents the user with either
the English or Spanish side. The user then presses [SPACEBAR] to reveal the translation,
clear the screen, and present the next card.
"""
import argparse
import os
import random
import sys

import keyboard
from ruamel.yaml import YAML


def load_cards(card_deck):
    """Load a yaml file containing the flashcards"""
    yaml = YAML()
    with open(card_deck) as file:
        return yaml.load(file)


def read_card(card_deck):
    """Print one side of a random card from the deck"""
    keys = [k for k in card_deck.keys()]
    key = keys[random.randint(0, (len(keys) - 1))]
    print(key.title())
    return key


def flip_card(card_deck, random_card):
    """Print the translation of the random card from the read_card function"""
    print('» {}{}'.format(card_deck[random_card][0].upper(), card_deck[random_card][1:]))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Flashcard program')

    parser.add_argument('-d', '--deck', action='store_false', default=False,
                        help='specifies deck to use')

    parser.add_argument('-e', '--english', action='store_false', default=False,
                        help='specifies english to spanish mode')

    parser.add_argument('-s', '--spanish', action='store_false', default=False,
                        help='specifies spanish to english mode')

    if '-h' in sys.argv[1:]:
        print(parser.parse_args())

    elif sys.argv[1:] == []:
        print('Please specify the proper flags as a command line arguments:\n\n'
              '\tsudo python flashcards.py -e -d cards.yaml\n\n'
              '\t\t\t  or...\n\n'
              '\tsudo python flashcards.py -s -d cards.yaml\n\n'
              'See "python flashcards.py -h" for additional information.')
        sys.exit(0)

    if not any('yaml' in arg for arg in sys.argv[1:]):
        print('Please pass in a flashcard deck after the \'-d\' flag')
        sys.exit(0)

    if '-d' not in sys.argv[1:]:
        print('Please pass in a flashcard deck after the \'-d\' flag')
        sys.exit(0)

    elif '-s' not in sys.argv[1:]:
        if '-e' not in sys.argv[1:]:
            print('Please indicate language by passing in one of the \'-s\' or \'-e\' flags.')

    if '-e' in sys.argv[1:]:
        deck = load_cards([arg for arg in sys.argv if '.yaml' in arg][0])
        # reverse the keys with values so that the user guesses the Spanish word
        deck = dict((v, k) for k, v in deck.items())
        # keyboard.add_hotkey('q', quit)
        os.system('clear')
        print('Press [SPACEBAR] to advance. Exit at anytime with [CTRL] + [C]')
        print('There are {} cards in your deck.\n'.format(len(deck)))
        try:
            while True:
                card = read_card(deck)
                keyboard.wait('space')
                flip_card(deck, card)
                keyboard.wait('space')
                os.system('clear')
        except KeyboardInterrupt:
            os.system('clear')
            sys.exit(0)

    elif '-s' in sys.argv[1:]:
        deck = load_cards([arg for arg in sys.argv if '.yaml' in arg][0])
        # keyboard.add_hotkey('q', quit)
        os.system('clear')
        print('Press [SPACEBAR] to advance. Exit at anytime with [CTRL] + [C]')
        print('There are {} cards in your deck.\n'.format(len(deck)))
        try:
            while True:
                card = read_card(deck)
                keyboard.wait('space')
                flip_card(deck, card)
                keyboard.wait('space')
                os.system('clear')
        except KeyboardInterrupt:
            os.system('clear')
            sys.exit(0)
