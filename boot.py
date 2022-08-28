#boot Sequence
import imp
import time
print("Initiating bootloader")
time.sleep(0.3)
contbt = input("Boot into pyOS 20.69? (Y)es/(N)o")
if contbt == "Y":
    print("Initiating boot sequence")