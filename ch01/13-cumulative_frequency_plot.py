#!/usr/bin/env python2.7

from nltk.book import *

fdist1 = FreqDist(text1)

fdist1.plot(50, cumulative=True)