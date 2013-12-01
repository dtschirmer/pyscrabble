#scrabble.py -- cheating at scrabble!
import argparse
import sys
from operator import itemgetter

parser = argparse.ArgumentParser()
parser.add_argument("RACK", type=str, help="Enter your tiles")
args = parser.parse_args()

# INITIALIZE OUR RACKS
rack  = []
used_rack = []

# GET THE INPUT, CHECK AND CONVERT
if len(sys.argv) == 2:
    raw_rack = sys.argv[1]

# CONVERT INPUT STRING TO AN UPPERCASE LIST
    for t in raw_rack.upper():
        rack.append(t)

# CONVERT OUR DICTIONARY TEXT FILE TO A PYTHON LIST
sowpods = []
f = open('sowpods.txt', 'r+')
for line in f:
    sowpods.append(line.rstrip())

# SEARCH THROUGH THE WORDLIST, FIND OUR VALID WORDS         
valid_words = []
for w in sowpods:
    rack.extend([i.upper() for i in used_rack]) # REFILL THE RACK 
    used_rack = []              # EMPTY THE USED_RACK
    count_used = 0              # SET/RESET THE COUNT
    for l in w:                 # FOR EACH LETTER IN THE WORD
        if l in rack:           # IF IT'S IN THE RACK
            used_rack.append(l) # ADD IT TO THE _OTHER_ "USED" RACK
            rack.remove(l)      # REMOVE IT FROM OUR "NORMAL" RACK
            count_used += 1     # INCREMENT THE COUNTER
    if len(w)  == count_used:
        valid_words.append(w)
    elif len(w) - 1 == count_used and "*" in rack:
        for l in w:
            if l not in used_rack:
                w = w.replace(l, l.lower()) 
        valid_words.append(w)


# FIGURE OUT THE WORD SCORES

scores = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
         "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
         "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
         "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
         "X": 8, "Z": 10}

word_scores = []
for w in valid_words:
    s  = 0
    for l in w:
        if l in scores:
            s += scores[l]
        else:
            s += 0
    word_scores.append(s)     

score_list = zip(valid_words, word_scores)
score_list = sorted(score_list, key=itemgetter(1), reverse=True)        

# PRINT OUT VALID WORDS WITH SCORES
if len(valid_words) == 0:
    print "No words found, sorry..."
else:
    for a, b in score_list:
        print '{0:9s} {1:3d}'.format(a, b)