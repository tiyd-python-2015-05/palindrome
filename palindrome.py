import re
string = input("Enter your Text: ")
string = re.sub(r'[^A-Za-z]',"",string)
string = string.lower()


def ite(inp):
  inp = inp[:]
  while len(inp)>1:
      if inp[0]==inp[-1]:
          inp = inp[1:-1]
      else:
          return False
  return True

if ite(string):
    print("\"{}\" is a palindrome!".format(string))
else:
    print("\"{}\" is not a palindrome!".format(string))
