#!/usr/bin/env python2.7

from nltk.book import *

print [len(w) for w in text1]
print
fdist = FreqDist([len(w) for w in text1])
print fdist
print
print fdist.keys()
print
print fdist.items()
print
print fdist.max()
print
print fdist[3]
print
print fdist.freq(3)