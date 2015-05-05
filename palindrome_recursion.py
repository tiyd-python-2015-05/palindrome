import re

def make_text(text):
    """Takes text and removes punctuation and spaces"""
    return (re.sub(r'[^A-Za-z]',"", text)).lower()



def palindrome(text):
    """Takes text, removes punctuation and spaces, and
    returns 'is a palindrome' or 'is not a palindrome'"""
    length = len(text)
    test_a = 0
    test_b = length - 1
    counter = length

    if counter <= 1:
        return "is a palindrome"
    elif text[test_a] != text[test_b]:
        return "is not a palindrome"
    else:
        return(palindrome(text[(test_a + 1):(test_b)]))
#    length = len(text)
#    if length == 0:
#        return "is a palindrome"
#    else:
#        return "is not a palindrome"

test_case = input("What is your text? ")
corrected_test = make_text(test_case)

print(palindrome(corrected_test))
