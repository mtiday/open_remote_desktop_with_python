"""This program will open a connection to a server you choose from a
list, or specify a name not on the list. Build a text file named
servers.txt and save it in the same directory this program is ran
from. Please make sure not to have any extra spaces before or at the
end of the name of the servers. One name per line. Example:
server1
server2
Created by Michael Tiday.
"""
import os
import time


def start():
    """Main function, will call other functions from this one."""
    # Create needed variables
    list_of_servers = build_list_of_servers()
    r_desktop_to_connect = connect_to(list_of_servers)
    print(f'Connecting to {r_desktop_to_connect}...')

    # Build BAT file that will call MSTC.exe with the correct switches
    build_bat_file(r_desktop_to_connect)

    # Connect to device via RDP
    time.sleep(1)
    os.startfile(os.path.join(os.getcwd(), 'rdesktop.bat'))


# build a list of devices to choose from
def build_list_of_servers():
    """Have user specify which server to connect to"""
    # From servers.txt file, create a variable list that will contain
    # servers to choose from
    list_of_machines = []
    with open('servers.txt', 'r') as westmoreland_servers:
        # Build list removing /n and making all letters uppercase
        for server in westmoreland_servers:
            list_of_machines.append(server.replace('\n', '').upper())
    # return servers in alphabetical order
    return sorted(list_of_machines)


# user input of device to connect to
def connect_to(list_of_servers):
    """Have user choose which device to connect to via
    Remote Desktop
    :param: list list_of_servers: List of devices the user picks from
    """
    choose_device = True
    # Print list of devices to choose from
    print_list_of_devices(list_of_servers)

    while choose_device:
        print('\nPlease choose from the list above')
        print('Enter number of device, M for a manual entry not in the list.')
        print('or "Q" to quit')
        user_choice = input('Enter choice: ')
        if user_choice.casefold() == 'q':
            print('Have a great day. Goodbye!')
            time.sleep(3)
            raise SystemExit
        if user_choice.casefold() == 'm':
            return input('Enter name of server then <Enter>: ')

        try:
            print(f'You choose {list_of_servers[int(user_choice)-1]}')
            return list_of_servers[int(user_choice)-1]

        except IndexError:
            print_list_of_devices(list_of_servers)
            print('Try again, number entered didn\'t correspond to a device.')

        except ValueError:
            print_list_of_devices(list_of_servers)
            print('You didn\'t enter an integer')


# print out list of servers
def print_list_of_devices(list_of_servers):
    """Print list of devices to choose from
    :param: list list_of_servers: list of devices to choose from
    """
    device_number = 0
    for device in list_of_servers:
        device_number += 1
        # if statements used so device names align if more than 10
        if device_number < 10:
            print(f'{device_number}  {device}')
        else:
            print(f'{device_number} {device}')


# Build the custom BAT file that will open the selected device
def build_bat_file(r_desktop_to_connect):
    """Build a BAT file that will RDP to the correct device
    :param: string r_desktop_to_connect: User's choice to connect
    """
    with open('rdesktop.bat', 'w') as rdesktop:
        rdesktop.write(f'start mstsc.exe /v:{r_desktop_to_connect} exit 0')


if __name__ == '__main__':
    # If not ran in a Windows OS, close the program
    if os.name != 'nt':
        print('Sorry, this program will only run on Windows')
        time.sleep(3)
        raise SystemExit
    start()
