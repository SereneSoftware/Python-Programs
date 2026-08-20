print("****** WELCOME TO VOWEL COUNTING SIMULATOR ******")
string = input("Enter the string: ")
stringNew = string.lower()
vowels = (
    stringNew.count("a") + 
    stringNew.count("e") + 
    stringNew.count("i") + 
    stringNew.count("o") + 
    stringNew.count("u"))
print(f"The given string has {vowels} vowels.")