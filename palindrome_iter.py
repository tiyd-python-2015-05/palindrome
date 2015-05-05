import re


text = input("Enter a phrase, a sentence, or multiple sentences\n> ")

def make_text(text): #break down sentence to letters only and lowercase
    return re.sub(r'[^A-Za-z]','', text).lower()

def palindrome():
    clean_text = make_text(text)
    index = 0
    back_index = int(len(clean_text)) - 1
    while index <= back_index:
        if clean_text[index] == clean_text[back_index]:
            index +=1
            back_index -=1
            if index > back_index:
                return 'is a palindrome'
        else:
            return 'is not a palindrome'


print(palindrome())
