#!/usr/bin/env python
"""
flashcard.py reads a yaml file containing flashcards, and presents the user with either keys or
values. The user then presses [SPACEBAR] to reveal the opposite, clear the screen, and
present the next card. Exit the program with [CTRL] + [C].
"""
import os
import random
import sys

import click
import keyboard
import ruamel.yaml


class Flashcards:
    """
    Flashcards class takes a yaml file deck into memory, and reads cards prompting the user to
    reveal the cards reverse when ready using the keyboard module.
    """
    def __init__(self):
        self.deck = ruamel.yaml.YAML()
        self.card = ['key', 'value']

    def load_deck(self, file):
        """
        load_deck() takes and loads yaml file a yaml file into memory, and also prints instructions
        and how many cards are in the deck.

        params
        :file - local yaml file specified via cli
        """
        with open(file, mode='r') as deck:
            self.deck = self.deck.load(deck)

        print('Press [SPACEBAR] to advance. Exit at anytime with [CTRL] + [C]\n'
              'There are {} cards in your deck.\n'.format(len(self.deck)))

    def read_card(self):
        """
        read_card() selects a random card from the deck residing in memory, and prints the key in
        bold. the function then waits for the user to hit [SPACEBAR] to proceed.
        """
        self.card = random.choice(
            list(self.deck.items())
        )
        # bold terminal output
        print('\033[1m' + self.card[0] + '\033[0m')
        keyboard.wait('space')

    def flip_card(self):
        """
        flip_card() checks to see if the value of the card is a yaml list or a string, and prints
        the formatted output accordingly to the terminal. the function then waits for the user to
        hit [SPACEBAR] to proceed.
        """
        if isinstance(self.card[1], ruamel.yaml.comments.CommentedSeq):
            for item in self.card[1]:
                print('» {}'.format(item))
        else:
            print('» {}'.format(
                str(self.card[1]).strip('\n')
            ))
        keyboard.wait('space')
        os.system('clear')

    def run_deck(self):
        """
        run_deck() executes the programs workflow, alternating calls between read_card() and
        flip_card().
        """
        try:
            while True:
                self.read_card()
                self.flip_card()

        except KeyboardInterrupt:
            # removes '^C' from terminal output
            os.system('clear')
            sys.exit(0)

def check_arguments(file):
    """
    check_arguments() ensures that the program is run as sudo (for the keyboard module), and
    also that a yaml file was passed in with the -f flag

    params
    :file - local yaml file specified via cli
    """
    if file is None:
        sys.exit('Please pass a yaml file to the application with the usage -f file.yaml')
    if os.getuid() != 0:
        sys.exit(
            'The keyboard module requires super user privileges. Please run the program as sudo'
        )

@click.command()
@click.option('-f', '--file', help='specifies yaml file to use')
def main(file):
    """
    main() executes the workflow.

    params
    :file - local yaml file specified via cli
    """
    check_arguments(file)
    flashcards = Flashcards()
    flashcards.load_deck(file)
    flashcards.run_deck()

if __name__ == "__main__":
    main()
