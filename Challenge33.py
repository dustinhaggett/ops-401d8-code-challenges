import os
import hashlib
from datetime import datetime
import requests

VIRUSTOTAL_API_URL = "https://www.virustotal.com/api/v3/files/"
API_KEY = os.environ.get("API_KEY_VIRUSTOTAL")

def generate_md5(file_path):
    """Generate MD5 hash for a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def check_virustotal(md5_hash):
    """Query VirusTotal for a given MD5 hash."""
    headers = {
        "x-apikey": API_KEY
    }
    response = requests.get(VIRUSTOTAL_API_URL + md5_hash, headers=headers)
    if response.status_code == 200:
        json_response = response.json()
        positives = json_response["data"]["attributes"]["last_analysis_stats"]["malicious"]
        return positives
    return None

def search_and_hash_files(directory):
    for root, dirnames, filenames in os.walk(directory):
        for fname in filenames:
            file_path = os.path.join(root, fname)
            md5_hash = generate_md5(file_path)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file_size = os.path.getsize(file_path)
            positives = check_virustotal(md5_hash)
            if positives is not None:
                print(f"Timestamp: {timestamp}, File Name: {fname}, File Size: {file_size} bytes, MD5 Hash: {md5_hash}, File Path: {file_path}, VirusTotal Positives: {positives}")
            else:
                print(f"Timestamp: {timestamp}, File Name: {fname}, File Size: {file_size} bytes, MD5 Hash: {md5_hash}, File Path: {file_path}")

def main():
    # Prompt the user for input
    directory = input("Enter the directory to search in: ")

    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Check if API key is set
    if not API_KEY:
        print("VirusTotal API key not set. Please set it as an environment variable named 'API_KEY_VIRUSTOTAL'.")
        return

    # Search and hash files
    search_and_hash_files(directory)

if __name__ == "__main__":
    main()






# Attribution to chatgpt4 code interpreter and codefellows github