import sys
from scapy.all import *

def scan_port(ip, port):
    pkt = IP(dst=ip) / TCP(dport=port, flags='S')
    response, _ = sr1(pkt, timeout=2, verbose=0)
    
    if response:
        if response[TCP].flags == 0x12:
            send_rst = IP(dst=ip) / TCP(dport=port, flags='R')
            send(send_rst, verbose=0)
            return "open"
        elif response[TCP].flags == 0x14:
            return "closed"
    return "filtered"

def icmp_ping(ip):
    pkt = IP(dst=ip) / ICMP()
    response = sr1(pkt, timeout=2, verbose=0)
    return response is not None

def port_scan(ip):
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    for port in range(start_port, end_port + 1):
        status = scan_port(ip, port)
        print(f"Port {port} is {status}")

def main():
    target_ip = input("Enter the target IP: ")
    
    # First, ping the IP address
    if icmp_ping(target_ip):
        print(f"{target_ip} is responsive to ICMP echo requests.")
        # If the host is responsive, scan its ports
        port_scan(target_ip)
    else:
        print(f"{target_ip} is not responsive to ICMP echo requests.")

if __name__ == "__main__":
    main()









# Attribution to chatgpt4 code interpreter and codefellows github