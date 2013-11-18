#!/usr/bin/env python2.7

from nltk.book import *

V = set(text1)
long_words = [w for w in V if len(w) > 15]
print sorted(long_words)