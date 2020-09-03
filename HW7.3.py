size=float(input("Size of tank: "))
percentage= float(input("percentage full: "))
kmperliter = float(input("km per liter: "))
distance = kmperliter*percentage*size/100
print ("You can go another: ",distance, "km")
actualdistance = float (kmperliter*percentage*(size-5)/100)
if actualdistance > 200:
    print("The next gas station is 200 km away. ""\n""You can wait for the next station")
else:
    print("The next gas station is 200 km away. ""\n""Get gas now!")
