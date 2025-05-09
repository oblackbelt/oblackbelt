#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
from getpass import getpass

# Get sudo password
passwd = getpass("Before you start, enter sudo password: ")

# All the commands
commands = ("apt update", "apt upgrade -y", "apt full-upgrade -y", "apt install", "apt autoremove -y", "apt autoclean -y",
            "apt remove --purge", "add-apt-repository", "ls /etc/apt/sources.list.d/", "ppa-purge", "apt -f install", 
            "dpkg --configure -a", "dpkg -i", "fail2ban-client status sshd", "service --status-all", 
            "service --status-all | grep +", "systemctl daemon-reload")

maxcommands = len(commands)

# Function to execute commands interactively
def funcCommand(index):
    if index not in [4, 7, 8, 10, 13]:
        subprocess.run(["sudo", "-S"] + commands[index - 1].split(), input=passwd + "\n", text=True)
    else:
        arg2 = input("But I miss which one dude! Tell me now: ")
        full_command = commands[index - 1] + " " + arg2
        subprocess.run(["sudo", "-S"] + full_command.split(), input=passwd + "\n", text=True)

# Menu loop
while True:
    try:
        print("\nChoose your destiny...\n\n  0) do the dirt work and exit this shit\n  1) update sources\n \
 2) upgrade system\n  3) upgrade distribution\n  4) install <packet>\n  5) autoremove\n \
 6) autoclean\n  7) remove and purge <packet>\n  8) add repository <ppa>\n  9) list repositories\n \
10) purge repository\n 11) fix dependencies\n 12) reconfigure dpkg\n 13) install .deb <packet>\n \
14) print fail2ban status\n 15) print service --status-all\n 16) print service grep (+)\n \
17) reload daemons\n ^C exit this shit\n")

        choice = input("Live or die? Make your choice: ")
        if not choice.isnumeric():
            choice = 99
        else:
            choice = int(choice)

        if choice == 0:
            command_list = [12, 11, 1, 2, 3, 5, 6, 17]
            print("Starting the whole shit...")
            for i in command_list:
                funcCommand(i)
            print("\nAll the stuff done!! C Ya tomorrow...\n\npowered by doutormarinho\n")
            exit(0)

        elif 0 < choice <= maxcommands:
            print("OK, You're the Master!")
            funcCommand(choice)
        else:
            subprocess.run(["clear"])
            print("\nQue burrrro, try again yo dumb!!!")

        print("\nPress ANY button to format C:\\...\nPress and HOLD power to cancel formatting...")
        input()
        subprocess.run(["clear"])

    except KeyboardInterrupt:
        subprocess.run(["clear"])
        print("Goodbye!!!\n\npowered by doutormarinho\n")
        exit(0)
