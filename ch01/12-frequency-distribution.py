#!/usr/bin/env python2.7

from nltk.book import *

fdist1 = FreqDist(text1)
print fdist1

vocabulary1 = fdist1.keys()
print vocabulary1[:50]

print fdist1['whale']