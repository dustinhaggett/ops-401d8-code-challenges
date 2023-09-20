import sys
from scapy.all import *
from netaddr import IPNetwork

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

def icmp_ping_sweep(network):
    online_hosts = 0
    for ip in IPNetwork(network):
        # Exclude network and broadcast addresses
        if ip != network.network and ip != network.broadcast:
            pkt = IP(dst=str(ip)) / ICMP()
            response = sr1(pkt, timeout=2, verbose=0)
            
            if response:
                if response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]:
                    print(f"{ip} is actively blocking ICMP traffic.")
                else:
                    print(f"{ip} is responding.")
                    online_hosts += 1
            else:
                print(f"{ip} is down or unresponsive.")
    
    print(f"\n{online_hosts} hosts are online.")

def main():
    while True:
        print("\nNetwork Security Tool")
        print("1. TCP Port Range Scanner")
        print("2. ICMP Ping Sweep")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            target_ip = input("\nEnter the target IP: ")
            start_port = int(input("Enter the start port: "))
            end_port = int(input("Enter the end port: "))
            for port in range(start_port, end_port + 1):
                status = scan_port(target_ip, port)
                print(f"Port {port} is {status}")

        elif choice == "2":
            network = input("\nEnter the network address (e.g., 10.10.0.0/24): ")
            icmp_ping_sweep(IPNetwork(network))

        elif choice == "3":
            print("Exiting...")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()







# Attribution to chatgpt4 code interpreter and codefellows github