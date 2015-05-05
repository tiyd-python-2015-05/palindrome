

def sanitize(text,evil_char):
    """Removes an evil character from the input text"""
    return "".join(text.split(evil_char))

def wash_with_acid(text):
    """Removes a list of grammatical characters from the text"""
    bad_chars = [" ",",",".","?","!",":"]
    cleaner_text = text
    for c in bad_chars:
        cleaner_text = sanitize(cleaner_text,c)
    cleaner_text = cleaner_text.lower()
    return cleaner_text

def pd_r(text):
    """Recursive test to see if the input text is a palindrome"""
#    print("  call of recursive test: "+text)
    if len(text)<=1:
        return True
    elif (text[0]!=text[len(text)-1]):
        return False
    else:
        return pd_r(text[1:len(text)-1])

def pd_i(text):
    """Iterative text to see if the input text is a plaindrome"""
    result = True # start true, test for false each char
    for i in range(len(text)//2):
        if text[i] != text[len(text)-i-1]:
            result = False
            break
    return result

print("")
user_text = input("Enter a text to test for palindromicity: ")

print("")
print(" Attempting to remove grammar characters from input")
text = wash_with_acid(user_text) # sanitization, removes grammar chars
print("  success, sanitized input: ")
print("   '"+text+"")

print("")
print(" Recursive test to check if the text is a palindrome")
print("  result:")

if (pd_r(text)):
    print("is a palindrome")
else:
    print("is not a palindrome")

print("")
print(" Iterative test to check if the text is a plaindrome")
print("  result:")


if (pd_i(text)):
    print("is a palindrome")
else:
    print("is not a palindrome")

print("")
