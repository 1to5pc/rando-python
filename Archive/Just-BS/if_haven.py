import time
import os
age = input("Input your age: ")
name = input("Input your name: ")
print("Your age is:",age,"Your name is: ",name)
checks = int((input("Is the above info accurate? (1 for Yes, 0 for No): ")))
if checks == 1:
  print("Good. Your Info Will Be Saved Into Pdata.txt")
elif checks == 0:
  print("oh")
else:
    print("Invalid Input")
    time.sleep(2)