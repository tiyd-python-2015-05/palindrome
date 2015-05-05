theinput = input("What is your text? ")

theinput = theinput.lower()

mywords = theinput.split(" ")

myletters = []

isPalindrome = False

for word in mywords:
    for letter in word:
        if letter.isalpha():
            myletters.append(letter)
        else:
            pass

#print (myletters)

def checkPalindrome(letters):
    letterslength = len(letters)
    idx = 0
    idx2 = letterslength - 1
    while idx <= idx2:
        if letters[idx] == letters[idx2]:
            isPalindrome = True
            idx += 1
            idx2 -= 1
        else:
            isPalindrome = False
            return isPalindrome
    return isPalindrome

palindrome = checkPalindrome(myletters)

if palindrome:
    print("This is a palindrome")
else:
    print("This is not a palindrome")
