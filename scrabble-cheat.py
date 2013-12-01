#scrabble.py -- cheating at scrabble!
import argparse
import sys
from operator import itemgetter

parser = argparse.ArgumentParser()
parser.add_argument("RACK", type=str, help="Enter your tiles")
args = parser.parse_args()

# GET THE INPUT, CHECK AND CONVERT

rack  = []
used_rack = []

if len(sys.argv) == 2:
    raw_rack = sys.argv[1]
# CONVERT TO UPPER, and to a list
    for i in raw_rack.upper():
        rack.append(i)

# CONVERT FILE TO PYTHON LIST
sowpods = []
f = open('sowpods.txt', 'r+')
for line in f:
    sowpods.append(line.rstrip())

# SEARCH THROUGH THE WORDLIST, FIND OUR VALID WORDS         
valid_words = []
for w in sowpods:
    rack.extend(used_rack) # REFILL THE RACK
    used_rack = []  #EMPTY THE USED_RACK
    count_used = 0
    for l in w:
        if l in rack:
            used_rack.append(l)
            rack.remove(l)
            count_used += 1
    if len(w)  == count_used:
        valid_words.append(w)
    elif len(w) - 1 == count_used and "*" in rack:
        for l in w:
            if l not in rack:
                l = '(%s)'.format(l)
        valid_words.append(w)


# FIGURE OUT THE WORD SCORES

scores = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
         "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
         "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
         "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
         "X": 8, "Z": 10, "*": 0}

word_scores = []
for w in valid_words:
    s  = 0
    for l in w:
        s += scores[l]
    word_scores.append(s)     

score_list = zip(valid_words, word_scores)
score_list = sorted(score_list, key=itemgetter(1), reverse=True)        
# PRINT OUT VALID WORDS WITH SCORES
if len(valid_words) == 0:
    print "No words found, sorry..."
else:
    for a, b in score_list:
        print '{0:9s} {1:3d}'.format(a, b)