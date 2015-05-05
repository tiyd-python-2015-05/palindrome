import re


text = input("Enter a phrase, a sentence, or multiple sentences\n> ")

def make_text(text): #break down sentence to letters only and lowercase
    return re.sub(r'[^A-Za-z]','', text).lower()

def palindrome(clean_text):
    length = len(clean_text) - 1
    index = 0
    if length <= 1:
        return 'is a palindrome'
    elif clean_text[index] == clean_text[length]:
        index += 1
        return palindrome(clean_text[index:length])
    else:
        return 'is not a palindrome'


clean_text = make_text(text)

print(palindrome(clean_text))
