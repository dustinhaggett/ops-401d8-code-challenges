import os
import platform
import subprocess
import time
import smtplib
from email.message import EmailMessage
from getpass import getpass

def ping(host):
    # Determine the operating system and construct the ping command accordingly
    ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1 -W 1"

    # Ping the host and capture the output
    output = subprocess.getoutput(f"ping {ping_str} {host}")
    
    # Check if the ping was successful
    if "TTL=" in output:
        return True
    else:
        return False

def send_email(sender_email, sender_password, recipient_email, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

def main():
    host = "8.8.8.8"  # Specify the IP address you want to monitor
    interval = 2  # Interval between each ping in seconds

    sender_email = input("Enter your email address: ")
    sender_password = getpass("Enter your email password: ")
    recipient_email = input("Enter the recipient's email address: ")
    
    previous_status = None
    
    while True:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")
        if ping(host):
            current_status = "Network Active"
        else:
            current_status = "Network Inactive"
        
        if previous_status is not None and current_status != previous_status:
            subject = f"Host Status Change - {host}"
            body = f"Status change at {timestamp}:\nPrevious Status: {previous_status}\nCurrent Status: {current_status}"
            send_email(sender_email, sender_password, recipient_email, subject, body)
        
        print(f"{timestamp} {current_status} to {host}")
        
        previous_status = current_status
        time.sleep(interval)

if __name__ == "__main__":
    main()
