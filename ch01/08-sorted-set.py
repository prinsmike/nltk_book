#!/usr/bin/env python2.7

from nltk.book import *

# set() groups duplicate tokens together.

print sorted(set(text3))
print len(set(text3))