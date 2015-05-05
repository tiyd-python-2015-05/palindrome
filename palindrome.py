from re import *

def isapalindrome( ):
    '''returns True when text is a palindrome'''
    # user_text_lower
    text = input("Write some text: ")
    text_lower = text.lower()

    # sub(pattern, repl, string, count=0, flags=0)
    cleaned_text = sub(r'[^A-Za-z]', "", text_lower)

    # determine if the text is palindrome or not
    if cleaned_text == cleaned_text[::-1]:
        print("is a palindrome")
    else:
        print("is not a palindrome")
    # let the user know if it is a palindrome or not

# ask the user to input some text
#user_text = input("Enter some text: ")



def reverseChar(word = '' ):

    reversed_word = ''
    for letter in word:
        if len(word) == 1:
            reversed_word = reversed_word + word
        else:
            reversed_word =  reversed_word+word[-1]
            word = word[:len(word)-1]
            reverseChar(word)

    return reversed_word


word = input("Write some text: ")

# determine if the text is palindrome or not
reversed_word = sub(r'[^A-Za-z]', "",reverseChar(word))
original_word = sub(r'[^A-Za-z]', "", word)
if original_word.lower() == reversed_word.lower():
    print("is a palindrome")
else:
    print("is not a palindrome")
