import sys
from scapy.all import *

def scan_port(ip, port):
    # Create a TCP packet with the specified destination IP and port
    pkt = IP(dst=ip) / TCP(dport=port, flags='S')
    
    # Send the packet and capture the response
    response, _ = sr1(pkt, timeout=2, verbose=0)
    
    if response:
        # Check for SYN-ACK flag (0x12)
        if response[TCP].flags == 0x12:
            # Send a RST packet to close the connection
            send_rst = IP(dst=ip) / TCP(dport=port, flags='R')
            send(send_rst, verbose=0)
            return "open"
        
        # Check for RST flag (0x14)
        elif response[TCP].flags == 0x14:
            return "closed"
    
    # If no response, the port is filtered
    return "filtered"

def main():
    # Define the target IP and port range
    target_ip = input("Enter the target IP: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    # Scan each port in the range
    for port in range(start_port, end_port + 1):
        status = scan_port(target_ip, port)
        print(f"Port {port} is {status}")

if __name__ == "__main__":
    main()







# Attribution to chatgpt4 code interpreter and codefellows github# Attribution to chatgpt4 code interpreter and codefellows github