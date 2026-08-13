print("----- HELLO CLASS! TODAY'S TOPIC IS VOWELS -----")
ans = input("Do you want to know what vowels are? : ")
if (ans == "yes" or ans == "Yes"):
    print("Wow! Really excited to teach you! There are 5 types of vowels in English language.\n1. A\n2. E\n3. I\n4. O\n5. U")
    vowel = input("Enter a vowel: ")
    match vowel:
        case ("A" | "a"):
            print("A is for Apple.")
        case ("E" | "e"):
            print("E is for Elephant.")    
        case ("I" | "i"):
            print("I is for Igloo.")    
        case ("O" | "o"):
            print("O is for Orange.")    
        case ("U" | "u"): 
            print("U is for Umbrella.")        
        case _:
            print("Please select from the given Vowels.")  
else:
    print("Ok, Come to study again!")            
print("****     THANKYOU STUDENTS    *****")            
