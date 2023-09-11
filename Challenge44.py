#!/usr/bin/python3

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# TODO: Set a timeout value here. For example, 1 second.
timeout = 1
sockmod.settimeout(timeout)

# TODO: Collect a host IP from the user. For example, input("Enter host IP: ")
hostip = input("Enter host IP: ")

# TODO: Collect a port number from the user and convert it to an integer.
portno = int(input("Enter port number: "))

def portScanner(portno):
    try:
        # Using connect_ex() function which returns an error indicator
        result = sockmod.connect_ex((hostip, portno))
        if result == 0:
            print("Port open")
        else:
            print("Port closed")
    except socket.error as e:
        print(f"Error: {e}")

portScanner(portno)
