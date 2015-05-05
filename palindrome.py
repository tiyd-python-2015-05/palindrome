from re import *

def isapalindrome( text ):
    '''returns True when text is a palindrome'''
    # user_text_lower
    text_lower = text.lower()

    # sub(pattern, repl, string, count=0, flags=0)
    cleaned_text = sub(r'[^A-Za-z]', "", text_lower)

    # determine if the text is palindrome or not
    if cleaned_text == cleaned_text[::-1]:
        return True
    else:
        return False
    # let the user know if it is a palindrome or not

# ask the user to input some text
user_text = input("Enter some text: ")


if isapalindrome(user_text):
    print("{} is a palindrome".format(user_text))
else:
    print("{} is not a palindrome".format(user_text))
