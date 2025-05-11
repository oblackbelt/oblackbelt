#!/usr/bin/python
# -*- coding: utf-8 -*-

# Call Libraries
from os import system as sys
from getpass import getpass as gp

# Define Global Variables
## First to grab password
passwd = gp("Before you start, enter sudo password: ")

## Second is a tuple with all the commands I need.
commands = ("apt update", "apt upgrade -y", "apt full-upgrade -y", "apt install", "apt autoremove -y", "apt autoclean -y",
 "apt remove --purge", "add-apt-repository", "ls /etc/apt/sources.list.d/", "ppa-purge", "apt -f install", "dpkg --configure -a",
 "dpkg -i", "fail2ban-client status sshd", "service --status-all", "service --status-all | grep +", "systemctl daemon-reload")

## and than it counts how many commands I got!
maxcommands = len(commands)

# Define
## Main command to do all the stuff works.
def funcCommand(arg1):
    if(arg1 != 4 and arg1 != 7 and arg1 != 8 and arg1 != 10 and arg1 != 13): # do not ask second argument.
    	sys("echo %s|sudo -S %s" % (passwd, commands[arg1-1])) # do the command with one arg.
    else:
        arg2 = str(input("but I miss which one dude! Tell me now: ")) # Asking for second argument
        sys("echo %s|sudo -S %s" % (passwd, commands[arg1-1] + " " + arg2)) # do the command with both args

while True:
    try: # Show the main menu
        print("\nChoose your destiny...\n\n  0) do the dirt work and exit this shit\n  1) update sources\n \
 2) upgrade system\n  3) upgrade distribution\n  4) install <packet>\n  5) autoremove\n \
 6) autoclean\n  7) remove and purge <packet>\n  8) add repository <ppa>\n  9) list repositories\n \
10) purge repository\n 11) fix dependencies\n 12) reconfigure dpkg\n 13) install .deb <packet>\n \
14) print fail2ban status\n 15) print service --status-all\n 16) print service grep (+)\n \
17) reload daemons\n ^C exit this shit\n")

# Ask user its choice
        choose = (str(input("Live or die? Make your choice: ")))
        if(choose.isnumeric() == False): # Test if the input is a number
            choose = 99 # if not, 99
        else:
            choose = int(choose) # if yes, convert.

# If zero, do a lot of stuffs...
        if (choose == 0):
            command = [12, 11, 1, 2, 3, 5, 6, 17]
            print("Starting the whole shit...")
            for i in command:
                funcCommand(i)
# And kiss goodbye
            print("\nAll the stuff done!! C Ya tomorrow...\n"
                  "\npowered by doutormarinho\n")
            exit(0) # break will stop the loop... I wanna jump out!

# If != zero, must be less than max options... Do specific command in tupple
        elif (choose != 0 and choose <= maxcommands):
            print("OK, You're the Master!")
            funcCommand(choose)

# Else means some shit the user did!
        else:
            sys("clear")
            print("\nQue burrrro, try again yo dumb!!!")

# Just one scary message before loop again.
        print("\nPress ANY button to format C:\...\n"
        "Press and HOLD power to cancel formatting...")
        nada = input()
        sys("clear")

# If 0<Choice<Max, this is how user exits the program.
    except KeyboardInterrupt:

# Clear, Bye-Bye, Sign, Kill.
        sys("clear")
        print("Goodbye!!!\n")
        print("powered by doutormarinho\n")
        exit(0)
# End of story
