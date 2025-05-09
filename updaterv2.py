#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import pty
from getpass import getpass

# Ask for sudo password once (optional, not used in PTY)
getpass("Before you start, enter sudo password (used during command run): ")

# List of commands
commands = (
    "apt update", "apt upgrade", "apt full-upgrade", "apt install", "apt autoremove",
    "apt autoclean", "apt remove --purge", "add-apt-repository", "ls /etc/apt/sources.list.d/",
    "ppa-purge", "apt -f install", "dpkg --configure -a", "dpkg -i", "fail2ban-client status sshd",
    "service --status-all", "service --status-all | grep +", "systemctl daemon-reload"
)

def run_in_pty(command):
    pid, fd = pty.fork()
    if pid == 0:
        os.execvp("bash", ["bash", "-c", f"sudo {command}"])
    else:
        try:
            while True:
                output = os.read(fd, 1024)
                if not output:
                    break
                os.write(1, output)
        except OSError:
            pass

def funcCommand(index):
    if index not in [4, 7, 8, 10, 13]:  # these require extra input
        run_in_pty(commands[index - 1])
    else:
        arg = input("Which one? Tell me now: ")
        run_in_pty(f"{commands[index - 1]} {arg}")

while True:
    try:
        print("""
Choose your destiny...

  0) do the dirt work and exit this shit
  1) update sources
  2) upgrade system
  3) upgrade distribution
  4) install <packet>
  5) autoremove
  6) autoclean
  7) remove and purge <packet>
  8) add repository <ppa>
  9) list repositories
 10) purge repository
 11) fix dependencies
 12) reconfigure dpkg
 13) install .deb <packet>
 14) print fail2ban status
 15) print service --status-all
 16) print service grep (+)
 17) reload daemons

^C exit this shit
""")
        choice = input("Live or die? Make your choice: ")
        if not choice.isdigit():
            choice = 99
        else:
            choice = int(choice)

        if choice == 0:
            for i in [12, 11, 1, 2, 3, 5, 6, 17]:
                funcCommand(i)
            print("\nAll the stuff done!! C Ya tomorrow...\n\npowered by doutormarinho\n")
            exit(0)
        elif 0 < choice <= len(commands):
            print("OK, You're the Master!")
            funcCommand(choice)
        else:
            os.system("clear")
            print("\nQue burrrro, try again yo dumb!!!")

        input("\nPress ANY button to format C:\\...\nPress and HOLD power to cancel formatting...")
        os.system("clear")

    except KeyboardInterrupt:
        os.system("clear")
        print("Goodbye!!!\n\npowered by doutormarinho\n")
        exit(0)
