# Write a program that takes in 3 integers between 1 and 11 (including both) and returns:
# (1) If their sum is less than or equal to 21, return their sum.
# (2) If their sum exceeds 21 and there's an 11, reduce the sum by 10.
# (3) If their sum exceeds 21 (even after adjustment), return "BUST".
# I/P: blackjack(5,6,7)
# O/P: 18
# I/P: blackjack(9,9,9)
# O/P: 'BUST'
# I/P: blackjack(9,9,11)
# O/P: 19

"""
**************************************************************
**************************************************************
"""

def blackjack (num1, num2, num3):
    total = num1 + num2 + num3
    if (total <= 21):
        return total
    elif (11 in [num1, num2, num3]) and ((total - 10) <= 21):
        return (total - 10)
    else:
        return "BUST"

print (blackjack (5,6,7))
print (blackjack (9,9,9))
print (blackjack (9,9,11))
