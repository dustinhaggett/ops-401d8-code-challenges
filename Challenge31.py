import os

def search_files(directory, filename):
    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for fname in filenames:
            if filename in fname:
                matches.append(os.path.join(root, fname))
    return matches

def main():
    # Prompt the user for input
    filename = input("Enter the file name to search for: ")
    directory = input("Enter the directory to search in: ")

    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Search for the files
    found_files = search_files(directory, filename)

    # Print the results
    for file in found_files:
        print(f"Found: {file}")

    print(f"\nTotal files searched: {len(found_files)}")
    print(f"Total hits found: {len([f for f in found_files if filename in f])}")

if __name__ == "__main__":
    main()




# Attribution to chatgpt4 code interpreter and codefellows github