import mysql.connector
f = "name.txt"
#f = open(f, "x")
#def create(file):
 #   f = open(f.txt, 'x')
print("A simple program to input and output your name")
fname = input("Input First Name: ")
lname = input("Input Last Name: ")
print(fname,lname)
choice = input("Save as name in file? [Y/n]")
if choice == "Y":
# f = open(f, "w")
 f.write(fname)
else:
    print("no")