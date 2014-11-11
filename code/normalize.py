#!/usr/bin/env python

import re
import sys
import string
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import nltk

# This program normalizes the file of sentences
# extracted from the set of documents.

# One argument: 
#    * the file you wish to normalize (e.g., sents.txt)

# Output format:
#   docid <tab> sentid <tab> normalized sentence

# Current normalization:
#   strip out punctuation
#   remove stop words

# You might be able to improve ROUGE by using
# more aggressive normalization, e.g.,
#   smart tokenization
#   downcasing (or clever case adjustment)
#   stemming
#   lemmatization
#   throwing out sentences with garbage
# Rememeber that NLTK can do a lot of this for you!  
stemmer = WordNetLemmatizer()

stops = set(stopwords.words("english"))

file = sys.argv[1]
sents = open(file)
for line in sents:
    line = line.rstrip("\n")
    parts = line.split("\t")
    sent = parts[-1]
    sent = re.sub('[a-zA-Z]+[0-9]+[a-zA-Z]*','SYMB',sent)
    sent = sent.lower()
    sent = re.sub('[0-9]+', 'num', sent)
    sent = re.sub(r'-', ' ', sent)  # replace hyphen with space
    out = sent.translate(string.maketrans("",""), string.punctuation) # remove punctuation 
    outwords = nltk.word_tokenize(out)
    outwords_nostops = [w for w in outwords if not w in stops] # remove stop words
    # outwords_nostops = [stemmer.lemmatize(w) for w in outwords_nostops]
    out = " ".join(outwords_nostops)
    print(parts[0] + "\t" + parts[1] + "\t" + out)
sents.close()
