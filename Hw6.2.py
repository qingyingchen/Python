import easygui
name = easygui.enterbox("What is your name?")
apt = easygui.enterbox("What is your apt. number?")
Ave = easygui.enterbox("What is the Avenue?")
city = easygui.enterbox("What is the City?")
state = easygui.enterbox("What is the state?")
zipcode = easygui.enterbox("What is the zipcode?")
easygui.msgbox(name+"\n"+Ave+" Ave, "+"Apt "+apt+"\n"+city+", "+state+"\n"+str(zipcode))
