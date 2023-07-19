from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    return key

def save_key(key):
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    if os.path.exists("key.key"):
        return open("key.key", "rb").read()
    else:
        key = generate_key()
        save_key(key)
        return key

def encrypt(filename, key, logfile):
    f = Fernet(key)
    if os.path.isdir(filename):
        for foldername, subfolders, filenames in os.walk(filename):
            for file in filenames:
                encrypt(os.path.join(foldername, file), key, logfile)
    else:
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)
        logfile.write(f"Encrypted {filename}\n")

def decrypt(filename, key, logfile):
    f = Fernet(key)
    if os.path.isdir(filename):
        for foldername, subfolders, filenames in os.walk(filename):
            for file in filenames:
                decrypt(os.path.join(foldername, file), key, logfile)
    else:
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(filename, "wb") as file:
            file.write(decrypted_data)
        logfile.write(f"Decrypted {filename}\n")

def main():
    mode = input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a directory\n4. Decrypt a directory\n")
    if mode not in ['1', '2', '3', '4']:
        print("Invalid mode selected.")
        return
    filename = input("Enter the filepath to the target file or directory: ")
    key = load_key()
    logname = 'encryption_log.txt'
    with open(logname, 'a') as logfile:
        if mode in ['1', '3']:
            encrypt(filename, key, logfile)
        elif mode in ['2', '4']:
            decrypt(filename, key, logfile)

if __name__ == "__main__":
    main()
