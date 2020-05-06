"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here


    file = open(file_path[1]).read()

    return file

open_and_read_file(sys.argv)

input_text = open_and_read_file(sys.argv)

# print(input_text)

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}

    words = text_string.split()
    words.append(None)

    for idx, word in enumerate(words[:-3]):

        key = (word, words[idx + 1], words[idx + 2])
        value = [words[idx + 3]]

        chains[key] = chains.get(key, []) + value

    return chains

make_chains(input_text)

chains = make_chains(input_text)

# print(chains)

def make_text(chains):
    """Return text from chains."""

    key = choice(list(chains.keys()))
    words = [key[0], key[1], key[2]]
    value = choice(chains[key])

    while value is not None:
        key = (key[1], key[2], value)
        words.append(value)
        value = choice(chains[key])

    return " ".join(words)

random_text = make_text(chains)

print(random_text)

# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string


# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
