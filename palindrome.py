import re
string = input("Enter your Text: ")
string = re.sub(r'[^A-Za-z]',"",string)
string = string.lower()
print(string)
def rec(inp):
  inp = inp[:]

  if len(inp)>2:
      if inp[0]==inp[-1]:
          return rec(inp[1:-1])
      else:
          return False

  else:
      if(len(inp)==1):
          return True
      else:
          if inp[0]==inp[-1]:
              return True
          else:
              return False

if rec(string):
    print("\"{}\" is a palindrome!".format(string))
else:
    print("\"{}\" is not a palindrome!".format(string))
