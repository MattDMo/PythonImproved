from ast import literal_eval
from datetime import datetime as dt
import random

with open("ID_Start.txt") as start, open("ID_Continue.txt") as cont:
    starters = [word.strip() for word in start.readlines()]
    continuers = [word.strip() for word in cont.readlines()]

allchars = starters + continuers
word_num = 50
timestamp = dt.now().strftime("%Y.%m.%d.%H.%M.%S")
with open("output." + timestamp + ".py", "w") as output:
    for i in range(word_num):
        length = random.randint(1, 10)
        word = literal_eval(random.choice(starters))
        for j in range(length):
            if len(word) == j:
                break
            else:
                word += literal_eval(random.choice(allchars))
        output.write(word + "()\n")
