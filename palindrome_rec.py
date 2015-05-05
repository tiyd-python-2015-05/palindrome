sentence = input("Enter a sentence: ").lower()
#user_input = makealpha(sentence)


def makealpha(sentence):
    my_string = ""
    for char in sentence:
        if char.isalpha():
            my_string += char
    return my_string

def check_pal(user_input):
    if len(user_input) > 1:
        if user_input[0] == user_input[-1]:
            return check_pal(user_input[1:-1])
            #return "Palindrome"
        return "This sentence is not a palindrome"
    else:
        return "This sentence is a palindrome"

user_input = makealpha(sentence)
print(check_pal(user_input))
