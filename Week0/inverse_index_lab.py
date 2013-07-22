from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0,2)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
''' What I made is a much more convoluted one -> finds the position of the word
ie 1st word is x 2nd word is y 3rd word is x
def makeInverseIndex(strlist):
    inverseIndex = {}
    count = 0
    for line in strlist:
        words = list(enumerate(line.split())) 
        for (index,word) in words:
             if word in inverseIndex.keys():
                 inverseIndex[word].add(count+index) 
             else:
                 inverseIndex[word] = {count+index}
        count += len(words)
    return inverseIndex
'''
'''
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
'''
def makeInverseIndex(strlist):
    inverseIndex = {}
    current_line = 0
    lines = list(enumerate(strlist))
    for line in strlist: 
        words = list(enumerate(line.split())) 
        for (index,word) in words:
             if word in inverseIndex.keys():
                 inverseIndex[word].add(current_line) 
             else:
                 inverseIndex[word] = {current_line}
        current_line += 1
    return inverseIndex


## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    unionset = inverseIndex[query[0]]
    for word in query:
        unionset = unionset | inverseIndex[word]
    return unionset

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    intersectset = inverseIndex[query[0]]
    for word in query:
        intersectset = intersectset & inverseIndex[word]
    return intersectset
