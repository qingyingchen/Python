import easygui
easygui.msgbox ("This program converts Fahrenheit to Celcius.") 
fahrenheit= easygui.enterbox("Type in a temperature in Fahrenheit: ")
celcius= ((float(str(fahrenheit)))-32)*5.0/9
easygui.msgbox ("That is %0.1f degree Celcius."%(celcius))

