#!/usr/bin/env python2.7

from nltk.book import *

fdist5 = FreqDist(text5)
print sorted([w for w in set(text5) if len(w) > 7 and fdist5[w] > 7])