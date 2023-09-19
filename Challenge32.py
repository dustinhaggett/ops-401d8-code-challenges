import os
import hashlib
from datetime import datetime

def generate_md5(file_path):
    """Generate MD5 hash for a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        # Read and update hash in chunks to avoid using too much memory
        for chunk in iter(lambda: file.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def search_and_hash_files(directory):
    for root, dirnames, filenames in os.walk(directory):
        for fname in filenames:
            file_path = os.path.join(root, fname)
            md5_hash = generate_md5(file_path)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file_size = os.path.getsize(file_path)
            print(f"Timestamp: {timestamp}, File Name: {fname}, File Size: {file_size} bytes, MD5 Hash: {md5_hash}, File Path: {file_path}")

def main():
    # Prompt the user for input
    directory = input("Enter the directory to search in: ")

    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Search and hash files
    search_and_hash_files(directory)

if __name__ == "__main__":
    main()









# Attribution to chatgpt4 code interpreter and codefellows github