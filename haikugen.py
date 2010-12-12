#!/usr/bin/env python

"""Creates random Haiku poems from set of words."""

import sys
import csv
import random

nouns = ''
verbs = ''
articles = ''
adjectives = ''
prepositions = ''

dictionary = [nouns,verbs,articles,adjectives,prepositions]

form1 = [['article','adjective','adjective','noun'],['preposition','article','adjective','noun'],['noun','verb']]

select = {  
             'noun': 0
            ,'verb': 1
            ,'article': 2
            ,'adjective': 3
            ,'preposition': 4
      }

def gen(vocab):
    return random.sample(dictionary[select[vocab]],1)[0]

def haiku(form):
    poem = ''
    for line in form:
        output = ''
        for vocab in line:
            output += str(gen(vocab))+' '
        poem += output+'/'

    poem = poem[:-1]+' #7'

    return poem

def main():
    if len(sys.argv) < 2:
        print 'Error'

    input_file = csv.reader(open(sys.argv[1],"r"))

    i = 0
    for row in input_file:
        dictionary[i] = row
        i = i + 1

    print "~~~~~~~~ Haiku ~~~~~~~\n"
    print haiku(form1)

if __name__ == "__main__":
    main()

