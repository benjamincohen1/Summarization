#!/usr/bin/env python

import re
import sys
import string

# This program builds an inverted index
# from a list of normalized sentences.

# One argument: 
#    * the list of sentences you wish to index (sents.txt.norm)

# Output format:
#   word sentid1:count-of-word sentid2:count-of-word sentid3:count-of-word...

# The curent scoring algorithm (in the next script) 
# does not use the count-of-word information. 

# You might be able to improve performance by using that
# information later on. In particular, you can think about
# calculating tf*idf using this information where
# tf=count-of-word and df=doc frequency (i.e., length of the list).

# dict for storing the docs (values) containing each word (key)
word2sent = {}  

sentid = 0  

file = sys.argv[1]
sents = open(file)
for line in sents:

    # indexing is slow, so print out the progress
    # so you know it's actually working

    line = line.rstrip("\n")
    parts = line.split("\t")
    sent = parts[-1]

    # break the normalized sentence into words
    words = sent.split()
    for w in set(words):
        newlistitem = str(sentid) + ":" + str(words.count(w))

        # if the word is already in the dict, append this to the value
        if w in word2sent:
            word2sent[w].append(newlistitem)

        # otherwise, create a new key-value pair in the dict    
        else:
            word2sent[w] = [newlistitem]
    sentid += 1

# print out the index          
for key in word2sent.keys():
    print(key),
    sents = word2sent[key]
    for s in sents:
        print(s + "\t"),
    print
