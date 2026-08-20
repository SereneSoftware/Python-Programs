print("----- WELCOME TO THE PALINDROME SIMULATOR -----")
string = input('Enter the string to check if it is a Palindrome: ').lower()
stringInverse = string[::-1]
if (string == stringInverse):
    print(f'The given string: "{string}" is a Palindrome.')
else:
    print(f'The given string: "{string}" is NOT a Palindrome.')    