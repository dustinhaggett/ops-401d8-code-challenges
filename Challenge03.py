#!/usr/bin/python3

# import libraries
import os, time, datetime
import smtplib
from getpass import getpass


# Requirements
# Ask the user for an email address and password to use for sending notifications
# Send an email to the administrator if a host status changes (from "up" to "down" or "down" to "up").
# Clearly indicate in the message which host staus changed, the status before and after, and a timestamp of the event.

# Declare variables
email = input("Enter your email: ")
password = getpass("Enter your passowrd: ")
ip = input("Please provide an ip address: ")
up = "Host is active"
down = "Host is down"

# Check that status change
last = 0
ping_result = 0




# Declare functions

# Function that handles when the host goes from down to up
def send_upAlert():
        
    # Gets timestamp
    now = datetime.datetime.now()

    # Start stmp session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # Start TLS
    s.starttls()

    # Authentication
    s.login(email, password)

    message = "Your server came back up"

    # Send the email
    s.sendmail(mailbot@codefellows.com, email, message)

    # Close the session
    s.quit()




# Function that handles when the host goes from up to down
def send_upAlert():
        
    # Gets timestamp
    now = datetime.datetime.now()

    # Start stmp session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # Start TLS
    s.starttls()

    # Authentication
    s.login(email, password)

    message = "Your server went down"

    # Send the email
    s.sendmail(mailbot@codefellows.com, email, message)

    # Close the session
    s.quit()




# Function that handles my ping
def check ping(ip):

    global ping_result
    global last

    # Sends a single ping to the target and puts the response into a variable

    # Check the change of status from up to down and down to up
    if ((ping_result !=last) and (ping_result == up))
        last = up
        send_upAlert()
    elif ((ping_result != last) and (ping_result == down))
        send_downAlert()
        last = down

    response = os.system("ping -c 1 " + ip)
    return ping_status



# Handle the function output








