#!/usr/bin/env python
"""
flashcard.py reads a yaml file containing flashcards, and presents the user with either the English
or Spanish side. The user then presses [SPACEBAR] to reveal the translation, clear the screen, and
present the next card. Exit the program with [CTRL] + [C].
"""
import argparse
import os
import random
import sys

import keyboard


def load_deck(deck_file):
    """Load a yaml file containing the flashcards

    Returns a list containing lists in the following format:
    [['word', 'translation'],
     ['word', 'translation']]
    """
    with open(deck_file) as file:
        # exclude yaml document header
        if file.readline() is '---':
            return [[line.split(':')[0], line.split(':')[-1][1:].split('\n')[0]]
                    for line in file if line[0] != '#']

        return [[line.split(':')[0], line.split(':')[-1][1:].split('\n')[0]]
                for line in file if line[0] != '#']


def read_card(card_deck):
    """Print one side of a card from the deck"""
    card = random.choice(card_deck)
    print(card[0].title())
    keyboard.wait('space')
    return card


def flip_card(card):
    """Print the translation of the card from read_card()"""
    print('» {}'.format(card[1].capitalize()))
    keyboard.wait('space')
    os.system('clear')
    return None


def run_deck(args):
    """Select language and call read_card() and flip_card() alternatively"""
    deck = load_deck(args['deck'])
    if args['english'] is True:
        # reverse the yaml keys with values so that the user guesses the Spanish word
        deck = [[card[1], card[0]] for card in deck]

    os.system('clear')
    print('Press [SPACEBAR] to advance. Exit at anytime with [CTRL] + [C]\n'
          'There are {} cards in your deck.\n'.format(len(deck)))
    try:
        while True:
            card = read_card(deck)
            flip_card(card)

    except KeyboardInterrupt:
        # removes '^C' from terminal output
        os.system('clear')
        sys.exit(0)

    return None


def parse_command_line():
    """Return the command line arguments as a dictionary"""
    parser = argparse.ArgumentParser(description='Flashcard program')

    parser.add_argument('-d', '--deck', nargs='?', default='cards.yaml',
                        help='specifies deck to use')

    parser.add_argument('-e', '--english', action='store_true', default=False,
                        help='specifies english to spanish mode')

    parser.add_argument('-s', '--spanish', action='store_true', default=False,
                        help='specifies spanish to english mode')

    return vars(parser.parse_args())


def check_parsed_arguments(args):
    """Executes flow control to check cli flags and ensure that the program runs properly"""
    if os.getuid() != 0:
        print('The keyboard module requires super user privileges. Please run the program as sudo')
        sys.exit(0)

    if args.get('deck') is None:
        print('Please pass in a yaml flashcard deck after the \'-d\' flag')
        sys.exit(0)

    if 'deck' not in args:
        print('Please pass in a yaml flashcard deck after the \'-d\' flag')
        sys.exit(0)

    if '.yaml' not in args.get('deck'):
        print('Please pass in a yaml flashcard deck after the \'-d\' flag')
        sys.exit(0)

    elif args.get('spanish') is False:
        if args.get('english') is False:
            print('Please indicate language by passing in one of the \'-s\' or \'-e\' flags.')
            sys.exit(0)

    return None


def main():
    """Only run when the program is run directly"""
    args = parse_command_line()
    check_parsed_arguments(args)
    run_deck(args)


if __name__ == "__main__":

    main()
