Simple flashcard application

The user reveals the answer by pressing `spacebar`, and then moves to the next card by again pressing `spacebar`. 

The application can be configured using the command line flags to allow the user to guess either the Spanish (`-s`) or the English (`-e`) side. Additionally, any deck (in yaml format) can be passed in with the `-d` flag.

![Alt Text](https://imgur.com/a/PjDzWsl.gif)

### Usage

```
# activate english mode
$ sudo python3 flashcards.py -e

# activate spanish mode
$ sudo python3 flashcards.py -s

# use a flashcard deck with a name other than 'cards.yaml'
$ sudo python3 flashcards.py -s -d verbs.yaml
```
