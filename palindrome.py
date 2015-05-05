sentence = input("Enter a sentence: ").lower()
user_input = ""

for char in sentence:
    if char.isalpha():
        user_input += char

for i in range(len(user_input) // 2):
    backwards = i * -1 - 1

    if user_input[i] == user_input[backwards]:
        if i == (len(user_input) // 2 - 1):
            print("This sentence is a palindrome.")
    elif i == (len(user_input) // 2 - 1):
        print("This sentence is not a palindrome.")
