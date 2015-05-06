import re

#Get input
text = input("Give a word or sentence to know whether it is a palindrome\n>")

#Clean text
def make_text(text):
    return re.sub(r'[^A-Za-z]','', text).lower()

clean_text = make_text(text)

#Check the string's index recursively, coming from both ends to see
#if it is equal both ways

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

print(palindrome(clean_text))
