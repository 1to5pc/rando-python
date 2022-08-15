import mysql.connector
print("A simple program to input and output your name")
fname = input("Input First Name: ")
lname = input("Input Last Name: ")
print(fname,lname)
choice = input("Save as name in file? [Y/n]")
if choice == "Y":
else:
    print("no")