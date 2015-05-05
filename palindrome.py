import re


def clean_text(text):
    """Remove punctuation and spaces from string text and make lowercase"""
    return re.sub(r'[^A-Za-z]', '', text).lower()


def i_palindrome(text):
    """Check for palindrome with an iterative method"""
    for index, char in enumerate(text):
        mirror_index = -1 * (index + 1)
        mirror_char = text[mirror_index]
        if char == mirror_char :
            print(char, '==', mirror_char, ' , ', end='')
        else:
            print(text[:index + 1], ' != ', text[:mirror_index-1:-1])
            return False
    return True


def r_palindrome(text):
    """Check for palindrome with a recursive method"""

    if text == '':
        return True
    elif text[0] == text[-1]:
        print(text[0], '==', text[-1], " , ", end='')
        return r_palindrome(text[1:-1])
    else:
        print(text[0], '!=', text[-1])
        return False


def e_palindrome(text):
    """Check for palindrome the easy way"""
    return text == text[::-1]


def test_palindrome(text, style='iterative'):
    """Test for palindrome using chosen style (iterative/recursive/easy)"""

    is_palindrome = False

    if style == 'iterative':
        print('\n...Testing iteratively...')
        is_palindrome = i_palindrome(text)
    elif style=='recursive':
        print('\n...Testing recursively...')
        is_palindrome = r_palindrome(text)
    else:
        print('\n...Testing the easy way...')
        is_palindrome = e_palindrome(text)

    if is_palindrome:
        print('That is a palindrome!')
    else:
        print('That is not a palindrome!')


#text = 'A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama!'
text =  input("Gimme some text:")
text = clean_text(text)
test_palindrome(text, 'iterative')
test_palindrome(text, 'recursive')
test_palindrome(text, 'easy')
