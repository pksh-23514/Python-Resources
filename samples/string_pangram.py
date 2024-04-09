# Write a program to check whether a sentence is Pangram or not. (Assume the sentence passed does not have any punctuation)
# Note: A Pangram sentence contains all the letters of the alphabet at least once.
# Eg.- "The quick brown fox jumps over the lazy dog"
# I/P: 'abcdefghijklmnopqrstuvwxyz'
# O/P: True

"""
**************************************************************
**************************************************************
"""

import string

def pangram (sentence, alphabet=string.ascii_lowercase):
    alphabet_set = set (alphabet)
    sentence = sentence.replace (' ', '')
    sentence = sentence.lower ()
    str_set = set (sentence)
    if (alphabet_set == str_set):
        return True
    else:
        return False

print (pangram ("The quick brown fox jumps over the lazy dog"))
print (pangram ('abcdefghijklmnopqrstuvwxyz'))
print (pangram ("Hello World"))
