from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def encrypt_message(message, key):
    """
    Encrypts a message
    """
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    print(encrypted_message)

def decrypt_message(encrypted_message, key):
    """
    Decrypts an encrypted message
    """
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message.encode())
    print(decrypted_message.decode())

def main():
    mode = input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n")
    if mode not in ['1', '2', '3', '4']:
        print("Invalid mode selected.")
        return
    if mode in ['1', '2']:
        filename = input("Enter the filepath to the target file: ")
    else:
        message = input("Enter the cleartext string: ")
    key = load_key()
    if mode == '1':
        encrypt(filename, key)
    elif mode == '2':
        decrypt(filename, key)
    elif mode == '3':
        encrypt_message(message, key)
    elif mode == '4':
        decrypt_message(message, key)

if __name__ == "__main__":
    main()
