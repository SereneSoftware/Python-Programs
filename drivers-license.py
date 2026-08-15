print("----- WELCOME TO DRIVER'S CLUB -----")
print("**** LET US SEE IF U CAN DRIVE? ****")
ans = input(("The drivers license depends upon several factors, Should we dive in?"))
if (ans == "yes" or ans == "Yes"):
    print("Factors include:\n1. Age\n 2. Citizenship\n 3. Aadhar Card")
    age = int(input("What is your age? : "))
    if (age >= 18):
        print("Yay, Let us check for factor 2.")
        ans2 = input(("Are you citizen of India? : "))
        if (ans2 == "yes" or ans == "Yes"):
            print("Wohoo! Let us check for factor 3.")
            ans3 = input("Do you posses an Aadhar Card? : ")
            if (ans3 == "yes" or ans == "Yes"):
                print("*-*-*-*-CONGRATULATIONS!-*-*-*-*\nYOU CAN DRIVE!")
            else:
                print("Sorry, due to NOT POSSESING AADAHR CARD, you are not eligible for driving.")    
        else: 
            print("Sorry, due to NOT BEING CITIZEN OF INDIA, you are not eligible for driving.")    
    else:
        print("Sorry, due to BEING 18+, you are not eligible for driving.") 
else:
    print("ALright, Thank you for contacting.") 
print(".......Visit us again!......")                      