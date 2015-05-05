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

def palindromeTest(letters,idx,idx2):
    if letters[idx] == letters[idx2]:
        isPalindrome = True
        idx += 1
        idx2 -= 1
        if idx > idx2:
            return isPalindrome
        else:
            return palindromeTest(letters,idx,idx2)
    else:
        isPalindrome = False
        return isPalindrome

palindrome = palindromeTest(myletters,0,(len(myletters)-1))

if palindrome:
    print("This is a palindrome")
else:
    print("This is not a palindrome")
