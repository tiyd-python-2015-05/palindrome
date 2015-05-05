
import re



pal = input("What is your palindrome?: ")
length = len(pal)
ix = 0
pal = re.sub('[^A-Za-z0-9]', '', pal).lower()
print (pal)
print(length)
print(pal[-ix])
while ix < length // 2 + 1:
    if pal[ix] != pal[-ix - 1]:
        print("This is not a palindrome")

    ix+=1
else:
    print( "This is a palindrome")
