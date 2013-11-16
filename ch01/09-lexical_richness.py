#!/usr/bin/env python2.7

from __future__ import division
from nltk.book import *

# Calculate a measure of the lexical richness of the text.
# The following example shows that each word is used 16 times on average.

print len(text3) / len(set(text3))