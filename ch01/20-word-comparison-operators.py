#!/usr/bin/env python2.7

s1 = "Moby Dick"
s2 = "Sense and Sensibility"
s3 = "Call me Ishmael"
s4 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness..."
s5 = "0123456789"
s6 = "and we arrived by the 5th."

print "Test if the string starts with t."
t = "Call"
print s1.startswith(t)
print s2.startswith(t)
print s3.startswith(t)
print s4.startswith(t)
print s5.startswith(t)
print s6.startswith(t)
print

print "Test if the string ends with t."
t = "Ishmael"
print s1.endswith(t)
print s2.endswith(t)
print s3.endswith(t)
print s4.endswith(t)
print s5.endswith(t)
print s6.endswith(t)
print

print "Test if t is contained inside the string."
t = "times"
print t in s1
print t in s2
print t in s3
print t in s4
print t in s5
print t in s6
print

print "Test if all cased characters in the string are lowercase."
print s1.islower()
print s2.islower()
print s3.islower()
print s4.islower()
print s5.islower()
print s6.islower()
print

print "Test if all cased characters in the string are uppercase."
print s1.isupper()
print s2.isupper()
print s3.isupper()
print s4.isupper()
print s5.isupper()
print s6.isupper()
print

print "Test if all characters in the string are alphabetic."
print s1.isalpha()
print s2.isalpha()
print s3.isalpha()
print s4.isalpha()
print s5.isalpha()
print s6.isalpha()
print

print "Test if all characters in the string are alphanumeric."
print s1.isalnum()
print s2.isalnum()
print s3.isalnum()
print s4.isalnum()
print s5.isalnum()
print s6.isalnum()
print

print "Test if all characters in the string are digits."
print s1.isdigit()
print s2.isdigit()
print s3.isdigit()
print s4.isdigit()
print s5.isdigit()
print s6.isdigit()
print

print "Test if the string is titlecased (all words in the string have initial capitals)."
print s1.istitle()
print s2.istitle()
print s3.istitle()
print s4.istitle()
print s5.istitle()
print s6.istitle()
print