#!/usr/bin/env python

import glob
import sys
import re

# This program splits every document into
# sentences, then writes all of the sentences
# to standard out. The output feeds into 
# the next step, normalization.

# One argument: 
#    * the directory of docs you want to process.

# Output format:
#   docid <tab> sentid <tab> sentence

# Current algorithm:
# Make a new sentence every time you see a period.
# If the sentence you created was more than 30 
# characters long, print it out.

# You might be able to improve your ROUGE score
# by changing how sentence splitting works.
# You might also want to add some features to 
# this file, e.g., what part of the document
# the sentence comes from. Such features might
# come in handy later on when you are ranking
# sentences.

# Another idea: Exclude any sentences the
# are in the References section. 

# Another idea: Exclude documents whose score is
# below some threshold. (The score is the first
# number in the name of the document. Larger is better.)

# Be creative.

####################

# Get all the files in the directory you supply as 
# an argument to this function.
drctry = sys.argv[1] + "/*html*"
files = glob.glob(drctry)

# For every file...
scores = []
for file in files:
    filename = re.sub(r'^.*\/(.*?)$', r'\1', file) 
    score = float('0.' + filename.split('.')[2])
    scores.append(score)

scores = sorted(scores)
cutoff = scores[len(scores)//4]
for file in files:
    counter = 0

    # open the file.
    doc = open(file)
    filename = re.sub(r'^.*\/(.*?)$', r'\1', file) 
    score = float('0.' + filename.split('.')[2])

    
    if score > cutoff:
        for line in doc:
            # if "\n" in line:
            #     print line
            # print line
            # print 'docs'
            # print "\n\n\n"

            line = line.strip('\n')
            sents = line.split("\t")
            # print sents[-1]
            for s in sents:
                if 'acknowledgement' in s.lower() or 'references' in s.lower():
                    break
                # print s.split('.')[0]
                # print '\n\n\n'
                for se in s.split('.')[:]:
                    # if "\n" in se:
                    #     print s
                    if (len(se) > 30):
                        print(filename + "\t" + str(counter) + "\t" + se + '.')
                        counter += 1
                # for se in s.split('.')[-1]:
                #     if (len(se) > 30):
                #         print(filename + "\t" + str(counter) + "\t" + se + '.')
                #         counter += 1
    doc.close()
