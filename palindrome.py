from re import *
# ask the user to input some text
user_text = input("Enter some text: ")

# user_text_lower
user_text_lower = user_text.lower()

# sub(pattern, repl, string, count=0, flags=0)
cleaned_text = sub(r'[^A-Za-z]', "", user_text_lower)

# determine if the text is palindrome or not
if cleaned_text == cleaned_text[::-1]:
    print("{} is a palindrome".format(cleaned_text))
else:
    print("{} is not a palindrome".format(cleaned_text))
# let the user know if it is a palindrome or not
