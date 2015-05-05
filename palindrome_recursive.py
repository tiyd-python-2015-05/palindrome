from re import *

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
