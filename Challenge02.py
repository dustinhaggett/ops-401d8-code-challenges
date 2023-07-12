import os
import platform
import subprocess
import time

def ping(host):
    # Determine the operating system and construct the ping command accordingly
    ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    
    # Ping the host and capture the output
    output = subprocess.getoutput(f"ping {ping_str} {host}")
    
    # Check if the ping was successful
    if "TTL=" in output:
        return True
    else:
        return False

def main():
    host = "192.168.1.1"  # Specify the IP address you want to monitor
    interval = 2  # Interval between each ping in seconds
    
    while True:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")
        if ping(host):
            status = "Network Active"
        else:
            status = "Network Inactive"
        
        print(f"{timestamp} {status} to {host}")
        time.sleep(interval)

if __name__ == "__main__":
    main()

