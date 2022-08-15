import mysql.connector
print("A simple program to input and output your name")
fname = input("Input First Name: ")
lname = input("Input Last Name: ")
print(fname,lname)
choice = input("Save as name in Database? [Y/n]")
if choice == "Y":
    name = mysql.connector.connect(
        firstN=fname,
        lastN=lname
    )
else:
    print("Not saving to Database")