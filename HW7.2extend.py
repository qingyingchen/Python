gender= input("Enter your gender: ")
if gender=="f" or "female":
    age = int(input("Enter your age: "))
    if 10 <= age <= 12:
        print ("You are welcome to join!")
    else:
        print ("Sorry, we only need girls from 10-12 years old")
else:
    print ("Sorry, only girls are allowed in this game!")
    
