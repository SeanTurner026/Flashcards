Simple flashcard application

The user reveals the answer by pressing `spacebar`, and then moves to the next card by again pressing `spacebar`. 

The application can be configured using the command line flags to allow the user to guess either the Spanish (`-s`) or the English (`-e`) side. Additionally, any deck (in yaml format) can be passed in with the `-d` flag.

<blockquote class="imgur-embed-pub" lang="en" data-id="QGEs1Cy"><a href="//imgur.com/QGEs1Cy">View post on imgur.com</a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>

### Usage

```
# activate english mode
$ sudo python3 flashcards.py -e

# activate spanish mode
$ sudo python3 flashcards.py -s

# use a flashcard deck with a name other than 'cards.yaml'
$ sudo python3 flashcards.py -s -d verbs.yaml
```
