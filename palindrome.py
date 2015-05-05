import re

def make_text(text):
    """Takes text and removes punctuation and spaces"""
    return (re.sub(r'[^A-Za-z]',"", text)).lower()



def palindrome(text):
    """Takes text and returns 'is a palindrome'
    or 'is not a palindrome'"""
    length = len(text)
    test_a = 0
    test_b = length - 1
    counter = length // 2

    if length == 1:
        return "is a palindrome"

    while counter > 0:
        if text[test_a] != text[test_b]:
            return "is not a palindrome"
        else:
            counter -= 1
    return "is a palindrome"

test_case = input("What is your text? ")
corrected_test = make_text(test_case)

print(palindrome(corrected_test))
