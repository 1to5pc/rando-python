import time
import os
def progress(percent=0, width=20):
    # The number of hashes to show is based on the percent passed in. The
    # number of blanks is whatever space is left after.
    hashes = width * percent // 100
    blanks = width - hashes

    print('\r[', hashes*'#', blanks*' ', ']', f' {percent:.0f}%', sep='',
        end='', flush=True)

print("Welcome to Terminalx")
print("This is a 'terminal emulator' in python")
cmd = input("Enter your command: ")
if cmd == "py":
    print("Entering python.")
    time.sleep(0.16)
    print("P-Y-T-H-O-N")
    time.sleep(0.3)
    print("[OK] Python3 Opened")
elif cmd == "exit":
    print("exiting terminalx")
    time.sleep(0.08)
    time.sleep(0.2)
    for i in range(101):
     progress(i)
     time.sleep(0.01)
    print()
    print("[OK] Quit 'Terminalx'")
    time.sleep(2)