import re


def palindrome_check(a_string, end, start):
    """Takes a string and checks to see if it is a palindrome.
    Note: It does not format the string at all before testing it.

    Keyword Arguments:
    a_string -- The string to be tested
    start -- where in the string to begin checking for palindrome-ity
    end -- where in the string to begin working backwards from to check
            against the character referenced by "start" """


    if start == end or start == end + 1:
        return "Yes, that is a palindrome."
    else:
        if a_string[start] == a_string[end]:
            return palindrome_check(a_string, end-1, start+1)
        else:
            return "No, that is not a palindrome."



def test_input_palindrome():
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
        return palindrome_check(test_string, (len(test_string)-1), 0)





print(test_input_palindrome())
