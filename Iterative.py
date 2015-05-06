import re

#Enter text
text = input("Enter a word or sentence to know whether it is a palindrome: \n")

#Clean Text
def make_text(text):
    return re.sub(r'[^A-Za-z]', '', text).lower()

#Check to see if each letter are equal coming from both ends, iteratively
#cycling through the index of the string
def palindrome():
    clean_text = make_text(text)
    index = 0
    back_index = int(len(clean_text)) - 1
    while index <= back_index:
        if clean_text[index] == clean_text[back_index]:
            index += 1
            back_index -= 1

            if index >= back_index:
                return 'This is a palindrome'
            else:
                continue
        else:
            return 'this not a palindrome'




print(palindrome())
