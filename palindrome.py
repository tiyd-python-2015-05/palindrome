import re

def main():
  tester = getPal()

  print(isIt(tester, 0, len(tester)-1))
  #return isIt(tester, 0, len(tester)-1)

def getPal():
  palindrome = input("What is your palindrome?: ")

  tester = re.sub('[^A-Za-z0-9]', '', palindrome)
  tester = tester.lower()

  return  tester

def isIt(tester, start, end):
    if len(tester) < 2:
        return "This is not a good sentence, dude."
    elif start == end or start == end +1:

        return "This is a palindrome"
    else:
        if tester[start] == tester[end]:
            return isIt(tester,start+1,end-1)
        elif tester[start] != tester[end]:
            return "This is not a palindrome"

main()
