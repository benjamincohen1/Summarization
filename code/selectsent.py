#!/usr/bin/env python

import re
import sys
import string
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.wordnet import WordNetLemmatizer
import nltk
# This program reads in the query, 
# scores and ranks the sentences, and
# prints out a summary using that ranking.

# Three arguments: 
#    * the query file
#    * the index
#    * the list of sentences

# Output (currently): a summary 

# We start with the following stupid algorithm:

# For each non stopword in the query, add every
# sentence containing that word to a list of
# possible sentences for the final summary.
# Then, rank the sentences according to how 
# many words they share with the query.

stops = set(stopwords.words("english"))
stemmer = WordNetLemmatizer()
# First step: normalizing the query

# ****NOTE****
# Make sure you do the exact same normalization
# here as you did in normalize.py!!!

query = open(sys.argv[1]).read()
query = re.sub('[a-zA-Z]+[0-9]+[a-zA-Z]*','SYMB',query)
query = query.lower()
query = query.rstrip("\n")                  # remove EOL
query = re.sub(r'-', ' ', query)            # replace - with space
query = re.sub('[0-9]+', 'num', query)
query = query.translate(string.maketrans("",""), string.punctuation) # remove punct
query = re.sub(r'^\d\d\d ', '', query)      # remove the topic ID 
qwords = [w for w in nltk.word_tokenize(query) if not w in stops] # remove stop words
# qwords = [stemmer.lemmatize(w) for w in qwords]
# Second step: build list of candidate sentences
sentlist = []
indexfile = open(sys.argv[2])
for line in indexfile:
    parts = line.split()
    word = parts[0]
    if word in qwords:
        sentlist = sentlist + parts[1:]

# Third step: rank sentences according to how many
# words they share with query.

# Make a copy of the sentlist with the words counts removed.
# (Recall that the baseline system doesn't use the word counts.)
newsentlist = []
for s in sentlist:
    bits = s.split(":")
    newsentlist.append(bits[0])


# Dumb idea:
# Rank sentences according to the order in which they were
# added to the list of sentences sharing at least one
# word with the query.
rankedsents = newsentlist

#do somekind of cosine distance here


# This is a fancy way of taking a list, counting how many
# times each item appears in that list, and then sorting
# those (item, count) pairs in decreasing order by count.
# rankedsents = Counter(newsentlist).most_common()


# read in sentences
sentfile = open(sys.argv[3])
sents = sentfile.read().splitlines()

# Final step: print out ranked sentences until you hit 250 words
wordcount = 0
for rs in rankedsents:
    sentid = rs[0]
    bits = sents[int(sentid)].split("\t") 
    print(bits[-1] + " "),
    wordcount =+ wordcount + len(bits[-1].split())
    if (wordcount > 250):
        break

print("\n")
