#!/usr/bin/env python2.7

from nltk.book import *

# Create a frequency distribution.
fdist1 = FreqDist(FreqDist([len(w) for w in text1]))
fdist2 = FreqDist(FreqDist([len(w) for w in text2]))
# Count the number of times a given sample occurred.
print fdist1['that']
print fdist2['that']
print
# Frequency of a given sample.
print fdist1.freq('that')
print fdist2.freq('that')
print
# Total number of samples
print fdist1.N()
print fdist2.N()
print
# The samples sorted in order of decreasing frequency.
print fdist1.keys()
print fdist2.keys()
print
# Sample with the greatest count.
print fdist1.max()
print fdist2.max()
print
# Tabulate the frequency distribution.
print fdist1.tabulate()
print fdist2.tabulate()
print
# Graphical plot of the frequency distribution.
print fdist1.plot()
print fdist2.plot()
print
# Cumulative plot of the frequency distribution.
print fdist1.plot(cumulative=True)
print fdist2.plot(cumulative=True)
print
# Test if samples in fdist1 occur less frequently than in fdist2
print fdist1 < fdist2
