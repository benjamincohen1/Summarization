#!/bin/bash

# Step 1: Split sentences
# This takes all the documents for a query,
# finds the sentence boundaries, and
# writes the sentences, one per line, to a
# new file called sents.txt.

ls -d $PWD/docs/* | while read i; do
    echo $i;
   python code/splitsent.py $i > $i/sents.txt
done

# Step 2: Normalize sentences
# This normalizes the text of each sentence
# in each sents.txt file and writes
# the output to a new file, sents.txt.norm.

ls docs/*/sents.txt | while read i; do
    echo $i
    python code/normalize.py $i > $i.norm
done

# Step 3: Build index
# This builds an index of sents.txt.norm.

ls docs/*/*norm | while read i; do
    echo $i;
    newi=`echo $i | sed 's/sents.txt.norm/index.txt/g'`
    echo $newi
    python code/buildindex.py $i > $newi
done


# Step 4: Generate the summaries
# Score and rank sentences to generate summaries.

ls docs/ | while read i; do
    echo $i
    python code/selectsent.py docs/$i/query.txt docs/$i/index.txt docs/$i/sents.txt > peers/$i.txt
done


# Step 5: Score the summaries
# Use the simple Java implementation of
# ROUGE to score the summaries you generated.

java -jar jrouge.jar  -p peers -g gold -n 1
java -jar jrouge.jar  -p peers -g gold -n 2
java -jar jrouge.jar  -p peers -g gold -n 4
