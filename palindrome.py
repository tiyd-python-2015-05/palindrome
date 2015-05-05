import re

print("I am going to check if a given sentence is a palindrome!")
sentence = input("Give me a sentence: ")

def is_palendrome(sentence):

    sentence_with_no_space = re.sub(r'[^A-Za-z]',"",sentence[:])

    x = 0

    while(x <  len(sentence_with_no_space)):
        if sentence_with_no_space[x] == sentence_with_no_space[-(x+1)]:
            x +=1
        else:
            print('This is not a palindrome!')
            return
    print('This is a palindrome!')


is_palendrome(sentence)
