#!/usr/bin/env python2.7

from nltk.book import *

print [len(w) for w in text1]
print
fdist = FreqDist([len(w) for w in text1])
print fdist
print
print fdist.keys()