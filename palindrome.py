

def sanitize(text,evil_char):
    return "".join(text.split(evil_char))

def wash_with_acid(text):
    bad_chars = [" ",",",".","?","!",":"]
    cleaner_text = text
    for c in bad_chars:
        cleaner_text = sanitize(cleaner_text,c)
    cleaner_text = cleaner_text.lower()
    return cleaner_text

def pd(text):
    print("  call of recursive test: "+text)
    if len(text)<=1:
        return True
    elif (text[0]!=text[len(text)-1]):
        return False
    else:
        return pd(text[1:len(text)-1])

user_text = input("Enter a text to test for palindromicity: ")
text = wash_with_acid(user_text)

if (pd(text)):
    print("is a palindrome")
else:
    print("is not a palindrome")
