import re


def palindrome_check_iter(a_string):
    """Takes a string and checks to see if it is a palindrome.
    Note: It does not format the string at all before testing it.

    Keyword Arguments:
    a_string -- The string to be tested
    """


    for character in a_string:
        if character == a_string[-(a_string.index(character)+1)]:
        #it would be easier to do this using reversed() or a_string[::-1]
            pass
        else:
            return "No, that is not a palindrome"

    return "Yes, that is a palindrome"





def test_input_palindrome_iter():
    """Tests to see if string input by user is a palindrome
    (i.e. is the same backwards as forwards)"""

    #Asks for user input and removes punctuation and capitalization for testing.
    to_test = input("What potential palindrome would you like to test? ")
    test_string = re.sub(r'[^A-Za-z]', '', to_test)
    test_string = test_string.lower()

    #checks the length of the string to see if it is too short
    #and then calls function to check if palindrome
    if len(test_string) < 3:
        return "That is too short.  It is not a palindrome."
    else:
        return palindrome_check_iter(test_string)





print(test_input_palindrome_iter())
