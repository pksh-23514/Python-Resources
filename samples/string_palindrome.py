# Write a program that checks whether a word or phrase is Palindrome or not.
# Note: A Palindrome is word, phrase, or sequence that reads the same backward as forward.
# Eg.- "Madam" or "nurses run"
# I/P: 'helleh'
# O/P: True

"""
**************************************************************
**************************************************************
"""
def palindrome (phrase):
    phrase = phrase.replace (' ', '')
    phrase = phrase.lower ()
    if (phrase == phrase [::-1]):
        return True
    else:
        return False

print (palindrome ("nurses run"))
print (palindrome ("helleh"))
print (palindrome ("Madam"))
print (palindrome ("Hello"))
