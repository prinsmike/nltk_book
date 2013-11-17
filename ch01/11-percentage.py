#!/usr/bin/env python2.7

from __future__ import division
from nltk.book import *

# What percentage of the text is taken up by a word.

print 100 * text4.count('a') / len(text4)