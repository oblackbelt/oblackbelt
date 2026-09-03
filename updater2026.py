#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import sys

# Define Global Commands (Structured as lists for subprocess execution without shell=True)
COMMAND_MAP = {
    1: {"name": "apt update", "cmd": ["apt", "update"], "sudo": True},
    2: {"name": "apt upgrade", "cmd": ["apt", "upgrade", "-y"], "sudo": True},
    3: {"name": "apt full-upgrade", "cmd": ["apt", "full-upgrade", "-y"], "sudo": True},
    4: {"name": "apt autoremove", "cmd": ["apt", "autoremove", "--purge", "-y"], "sudo": True},
    5: {"name": "apt autoclean", "cmd": ["apt", "autoclean"], "sudo": True},
    6: {"name": "apt install <package>", "cmd": ["apt", "install"], "sudo": True, "arg": True},
    7: {"name": "apt remove --purge <package>", "cmd": ["apt", "remove", "--purge"], "sudo": True, "arg": True},
    8: {"name": "apt-add-repository", "cmd": ["apt-add-repository"], "sudo": True, "arg": True},
    9: {"name": "list sources", "cmd": ["ls", "-la", "/etc/apt/sources.list.d/"], "sudo": False},
    10: {"name": "ppa-purge", "cmd": ["ppa-purge"], "sudo": True, "arg": True},
    11: {"name": "fix broken dependencies", "cmd": ["apt", "--fix-broken", "install"], "sudo": True},
    12: {"name": "reconfigure dpkg", "cmd": ["dpkg", "--configure", "-a", "--force-confmiss", "--force-depends"], "sudo": True},
    13: {"name": "install .deb package", "cmd": ["dpkg", "-i"], "sudo": True, "arg": True},
    14: {"name": "fail2ban status", "cmd": ["fail2ban-client", "status", "sshd"], "sudo": True},
    15: {"name": "list services", "cmd": ["service", "--status-all"], "sudo": False},
    16: {"name": "active services", "cmd": ["sh", "-c", "service --status-all | grep '+'"], "sudo": False},
    17: {"name": "reload daemons", "cmd": ["systemctl", "daemon-reload"], "sudo": True},
    18: {"name": "install essentials", "cmd": ["apt", "install", "byobu", "baobab", "ufw", "gufw", "fail2ban", "gparted"], "sudo": True},
}

def initial_sudo_prompt():
    print("Checking if U R the Man... Gimme your pass.")
    try:
        subprocess.run(["sudo", "-v"], check=True)
        print("U R the Maaaaaan!")
    except (subprocess.CalledProcessError, KeyboardInterrupt):
        print("Oh! No... You failed!!!")

def execute_command(choice_num):
    cmd_info = COMMAND_MAP.get(choice_num)
    if not cmd_info:
        return

    full_cmd = list(cmd_info["cmd"])

    if cmd_info.get("arg"):
        user_arg = input(f"This command needs an argument ('{' '.join(full_cmd)} ___'). Tell me now: ").strip()
        if not user_arg:
            print("No argument provided. Aborting command.")
            return
        full_cmd.append(user_arg)

    if cmd_info["sudo"] and os.geteuid() != 0:
        full_cmd.insert(0, "sudo")

    print(f"\nCalling: {' '.join(full_cmd)}")
    try:
        subprocess.run(full_cmd, check=True)
        print(f"Command '{cmd_info['name']}' finished successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
    except FileNotFoundError:
        print(f"Error: Command '{full_cmd[0]}' not found.")
    print("-" * 30)

def run_dirty_work():
    # Sequence: reconfigure dpkg -> fix deps -> update -> full-upgrade -> autoremove -> autoclean -> daemon-reload
    sequence = [12, 11, 1, 2, 3, 4, 5, 17]
    print("\nStarting the whole shit...")
    for seq_id in sequence:
        print(f"\n--- Running step: {COMMAND_MAP[seq_id]['name']} ---")
        execute_command(seq_id)
    print("\nAll the stuff done!! C Ya tomorrow...\npowered by doutormarinho\n")

def main():
    initial_sudo_prompt()

    menu_text = """
Choose your destiny...

  0) do the dirty work and exit this shit
  1) update sources
  2) upgrade system
  3) upgrade distribution
  4) autoremove unneeded packages
  5) autoclean cached files
  6) install <package>
  7) remove and purge <package>
  8) add repository
  9) list repository files
 10) remove repository
 11) fix broken dependencies
 12) reconfigure dpkg
 13) install .deb <package>
 14) print fail2ban status
 15) list active systemd services
 16) list active services only
 17) reload daemons
 18) install essentials
 ^C exit this shit
"""

    while True:
        try:
            print(menu_text)
            choose_input = input("Live or die? Make your choice: ").strip()
            
            if not choose_input.isdigit():
                os.system("clear")
                print("\nQue burrrro, try again yo dumb!!!")
                continue

            choose = int(choose_input)

            if choose == 0:
                run_dirty_work()
                sys.exit(0)
            elif choose in COMMAND_MAP:
                print("OK, You're the Master!")
                execute_command(choose)
            else:
                os.system("clear")
                print("\nQue burrrro, try again yo dumb!!!")

            input("\nPress ENTER to continue...\n(Press and HOLD power to cancel formatting...)")
            os.system("clear")

        except KeyboardInterrupt:
            os.system("clear")
            print("\nGoodbye!!!\npowered by doutormarinho\n")
            sys.exit(0)

if __name__ == "__main__":
    main()
