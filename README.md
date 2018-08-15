Simple flashcard application. The user reveals the answer by pressing `spacebar`, and then moves to the next card by again pressing `spacebar`. The application can be configured using the command line flags to allow the user to guess either the Spanish (`-s`) or the English (`-e`) side. Additionally, any deck (in yaml format) can be passed in with the `-d` flag.

### Usage

```sudo python flashcards.py -e -d cards.yaml```

```sudo python flashcards.py -s -d cards.yaml```