# script to generate variable-length random "words" consisting of Unicode codepoints.
# 
from ast import literal_eval
from datetime import datetime as dt
import random

# TODO: use argparse to pass word number and length via command line

with open("ID_Start.txt") as start, open("ID_Continue.txt") as cont:
    starters = [word.strip() for word in start.readlines()]
    continuers = [word.strip() for word in cont.readlines()]

allchars = starters + continuers
word_num = 50 # how many words to write to test file
timestamp = dt.now().strftime("%Y.%m.%d.%H.%M.%S")
with open("output." + timestamp + ".py", "w") as output:
    for i in range(word_num):
        length = random.randint(1, 10)  # length of word, between 1 and 10
                                        # make 10 a variable?
        word = literal_eval(random.choice(starters))
        for j in range(length):
            if len(word) == j:
                break
            else:
                word += literal_eval(random.choice(allchars))
        output.write(word + "()\n")
