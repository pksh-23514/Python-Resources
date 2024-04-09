# Write a program to return a sentence with the words reversed.
# I/P: master_yoda('I am home')
# O/P: 'home am I'
# I/P: master_yoda('We are ready')
# O/P: 'ready are We'

"""
**************************************************************
**************************************************************
"""

def master_yoda (sentence):
    words = sentence.split ()
    reverse = ' '.join (words [::-1])
    return reverse

print (master_yoda ('I am home'))
print (master_yoda('We are ready'))
