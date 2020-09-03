length = float(input("Type the length of the room: "))
width = float(input("Type the width of the room: "))
area=(length)*(width)
print("The amount of carpets to cover the room: ", int(area), "in squar meters")
area1=9*area
print("The amount of carpets to cover the room: ", int(area1), "in squar inches")
price = float(input("Type the price of carpet for 1 square inch: "))
print("The price for the total carpet is: ", int(area1)*price,)
