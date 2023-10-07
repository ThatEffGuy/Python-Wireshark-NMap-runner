import os, getpass
program = int(input("what tool to run? \n 1: wireshark \n 2: Nmap \n 3: Exit \n Select a number: "))

#enters a loop until valid number is given
#if option 1

if program == 1 :
    print("starting wireshark")
    os.system('start wireshark') #starts wireshark

elif program == 2 :
    print("starting Nmap")
    os.system('start zenmap') #starts NMap gui vers zenmap

else:
    print("Exiting program...")
    exit()