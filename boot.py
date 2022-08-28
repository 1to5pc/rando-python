#boot Sequence
from cgi import print_arguments
import imp
from multiprocessing.connection import wait
import time
print("Initiating bootloader")
time.sleep(0.3)
contbt = input("Boot into pyOS 20.69? (Y)es/(N)o")
if contbt == "Y":
    print("Initiating boot sequence")