import subprocess

def banner_grab_netcat(target, port):
    print("\n[+] Banner grabbing using netcat:")
    try:
        result = subprocess.check_output(f"netcat -v -n -z -w2 {target} {port}", shell=True, stderr=subprocess.STDOUT).decode('utf-8')
        print(result)
    except subprocess.CalledProcessError as e:
        print(e.output.decode('utf-8'))

def banner_grab_telnet(target, port):
    print("\n[+] Banner grabbing using telnet:")
    try:
        result = subprocess.check_output(f"echo 'quit' | telnet {target} {port}", shell=True, stderr=subprocess.STDOUT).decode('utf-8')
        print(result)
    except subprocess.CalledProcessError as e:
        print(e.output.decode('utf-8'))

def banner_grab_nmap(target):
    print("\n[+] Banner grabbing using nmap:")
    try:
        # Scanning well-known ports (1-1024)
        result = subprocess.check_output(f"nmap -sV --script=banner {target} -p 1-1024", shell=True, stderr=subprocess.STDOUT).decode('utf-8')
        print(result)
    except subprocess.CalledProcessError as e:
        print(e.output.decode('utf-8'))

def main():
    target = input("Enter the target URL or IP address: ")
    port = input("Enter the port number: ")

    banner_grab_netcat(target, port)
    banner_grab_telnet(target, port)
    banner_grab_nmap(target)

if __name__ == "__main__":
    main()









# Attribution to chatgpt4 code interpreter and codefellows github