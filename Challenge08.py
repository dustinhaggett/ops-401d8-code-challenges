#!/usr/bin/env python3

import ctypes
import os
import logging
from cryptography.fernet import Fernet
from tkinter import filedialog, Tk

# Windows constant to set desktop wallpaper
SPI_SETDESKWALLPAPER = 20  

# Function to generate a new encryption key
def generate_key():
    key = Fernet.generate_key()
    return key

# Function to save the encryption key to a file
def save_key(key):
    try:
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    except Exception as e:
        # Log any exceptions that occur while trying to save the key
        logging.error(f"Failed to save key: {e}")

# Function to load the encryption key from a file
def load_key():
    if os.path.exists("key.key"):
        try:
            return open("key.key", "rb").read()
        except Exception as e:
            # Log any exceptions that occur while trying to load the key
            logging.error(f"Failed to load key: {e}")
    else:
        # If the key file doesn't exist, generate a new key and save it
        key = generate_key()
        save_key(key)
        return key

# Function to process files (either encrypt or decrypt)
def process_files(filename, key, logfile, operation):
    f = Fernet(key)
    if os.path.isdir(filename):
        # If the filename is a directory, recursively process all files in the directory
        for foldername, subfolders, filenames in os.walk(filename):
            for file in filenames:
                process_files(os.path.join(foldername, file), key, logfile, operation)
    else:
        try:
            # Read the file data
            with open(filename, "rb") as file:
                file_data = file.read()
            # Encrypt or decrypt the file data
            processed_data = operation(f, file_data)
            # Write the processed data back to the file
            with open(filename, "wb") as file:
                file.write(processed_data)
            # Log the operation
            logfile.write(f"{operation.__name__.capitalize()}ed {filename}\n")
        except Exception as e:
            # Log any exceptions that occur while processing the file
            logging.error(f"Failed to {operation.__name__} file {filename}: {e}")

# Function to encrypt a file or directory
def encrypt(filename, key, logfile):
    process_files(filename, key, logfile, lambda f, data: f.encrypt(data))

# Function to decrypt a file or directory
def decrypt(filename, key, logfile):
    process_files(filename, key, logfile, lambda f, data: f.decrypt(data))

# Function to simulate a ransomware attack 
def simulate_ransomware():
    ctypes.windll.user32.MessageBoxW(0, "Your files have been encrypted!", "Ransomware Simulation", 1)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "path_to_your_image.jpg", 0)

def main():
    # Set up logging
    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    # Hide the root Tk window (we only want to use the file dialog)
    root = Tk()
    root.withdraw()
    # Ask the user to select a mode
    mode = input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a directory\n4. Decrypt a directory\n5. Ransomware simulation\n")
    if mode not in ['1', '2', '3', '4', '5']:
        print("Invalid mode selected.")
        return
    # Ask the user to select a file or directory
    filename = filedialog.askopenfilename() if mode in ['1', '2'] else filedialog.askdirectory()
    # Load the encryption key
    key = load_key()
    # Open the log file
    logname = 'encryption_log.txt'
    with open(logname, 'a') as logfile:
        # Perform the selected operation
        if mode in ['1', '3']:
            encrypt(filename, key, logfile)
        elif mode in ['2', '4']:
            decrypt(filename, key, logfile)
        elif mode == '5':
            simulate_ransomware()

if __name__ == "__main__":
    main()


# References
# ChatGPT Code Interpreter
# Codefellows Ops 401 GitHub