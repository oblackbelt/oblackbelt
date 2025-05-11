#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Call Libraries
import subprocess
from os import system as os_system

# Define Global Variables

## Tuple with all the commands.
commands = ("apt update", "apt upgrade -y", "apt full-upgrade -y", "apt install", 
            "apt autoremove -y", "apt autoclean -y", "apt remove --purge", 
            "add-apt-repository", "ls /etc/apt/sources.list.d/", "ppa-purge", 
            "apt -f install", "dpkg --configure -a", "dpkg -i", 
            "fail2ban-client status sshd", "service --status-all", 
            "service --status-all | grep +", "systemctl daemon-reload")

## Count how many commands
maxcommands = len(commands)

# Function to validate sudo access initially (optional but good for user experience)
def initial_sudo_prompt():
    
    print("Checking sudo access. You may be prompted for your password.")
    try:
        subprocess.run(["sudo", "-v"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Thanks for the confirmation!")
    except subprocess.CalledProcessError:
        print("Warning: OGM! Shit happened. Sudo will prompt if needed.")
    except FileNotFoundError:
        print("Error: 'sudo' command not found. Please ensure it's installed and in your PATH.")
        print("-" * 20)

# Define Main command function
def funcCommand(command_index_1_based):
    base_command_str_template = commands[command_index_1_based - 1]

    # Commands that require an additional argument from the user (1-based indices: 4, 7, 8, 10, 13)
    commands_needing_user_arg = {
        "apt install",
        "apt remove --purge",
        "add-apt-repository",
        "ppa-purge",
        "dpkg -i"
    }

    current_command_str = base_command_str_template
    if base_command_str_template in commands_needing_user_arg:
        user_arg = str(input(f"This command needs an argument ('{base_command_str_template} ___'). Tell me now: "))
        current_command_str = f"{base_command_str_template} {user_arg}"

    # Determine if sudo is needed. Most system commands do.
    is_sudo_needed = True
    exceptions_no_sudo = [
        "ls /etc/apt/sources.list.d/",  
        "service --status-all",         
        "service --status-all | grep +" 
        "fail2ban-client status sshd"
    ]

    # If the base command itself is in the no_sudo list, don't prepend sudo
    if base_command_str_template in exceptions_no_sudo:
        is_sudo_needed = False

    # Construct the final command
    if is_sudo_needed and not current_command_str.strip().startswith("sudo"):
        # Only add sudo if it's not already part of the command string (for flexibility)
        final_executable_command = f"sudo {current_command_str}"
    else:
        final_executable_command = current_command_str

    print(f"\nCalling: {final_executable_command}")
    try:
        subprocess.run(final_executable_command, shell=True, check=True)
        print(f"Command '{base_command_str_template}' finished successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
    except KeyboardInterrupt:
        print("\nCommand execution interrupted by user.")
    except FileNotFoundError: # e.g. if sudo or the command itself isn't found
        print(f"Error: Command not found. Ensure '{final_executable_command.split()[0]}' is installed and in PATH.")
    print("-" * 30)

# --- Main script logic starts here ---

initial_sudo_prompt()

while True:
    try: # Show the main menu
        print("\nChoose your destiny...\n\n  0) do the dirt work and exit this shit\n  1) update sources\n \
 2) upgrade system\n  3) upgrade distribution\n  4) install <packet>\n  5) autoremove\n \
 6) autoclean\n  7) remove and purge <packet>\n  8) add repository <ppa>\n  9) list repositories\n \
10) purge repository\n 11) fix dependencies\n 12) reconfigure dpkg\n 13) install .deb <packet>\n \
14) print fail2ban status\n 15) print service --status-all\n 16) print service grep (+)\n \
17) reload daemons\n ^C exit this shit\n")

        choose_input = str(input("Live or die? Make your choice: "))
        if not choose_input.isnumeric(): # Test if the input is a number
            choose = 99 # if not, 99 (will trigger 'Que burro' message)
        else:
            choose = int(choose_input) # if yes, convert.

        if choose == 0:

            command_sequence_indices = [12, 11, 1, 2, 3, 5, 6, 17]
            print("\nStarting the whole shit...")
            for i_cmd_index in command_sequence_indices:
                print(f"\n--- Running command from sequence: {commands[i_cmd_index-1]} ---")
                funcCommand(i_cmd_index)
            print("\nAll the stuff done!! C Ya tomorrow...\n"
                  "\npowered by doutormarinho\n")
            exit(0) 

        elif 0 < choose <= maxcommands:
            print("OK, You're the Master!")
            funcCommand(choose)

        else:
            os_system("clear")
            print("\nQue burrrro, try again yo dumb!!!")

        print("\nPress ANY button to format C:...\n"
        "Press and HOLD power to cancel formatting...")
        input()
        os_system("clear")

    except KeyboardInterrupt:
        os_system("clear")
        print("\nGoodbye!!!\n")
        print("powered by doutormarinho\n")
        exit(0)
# End of story