import os
import crt
f = "name.txt"
#f = open(f, "x")
#def create(file):
 #   f = open(f.txt, 'x')
print("A simple program to input and output your name")
fname = input("Input First Name: ")
lname = input("Input Last Name: ")
flname = fname + " " + lname
print(flname)
choice = input("Save as name in file? [Y/n]")
if choice == "Y":
 f = open(f, "w")
 f.write("name:", flname)
else:
    print("no")