import time
import getpass  # Import the getpass module

# Part 1: Dictionary Iterator Function (Mode 1)
# This function takes a file path as input, opens the file, and iterates through each word in the file.
# It then prints each word to the screen with a delay of 1 second between each word.
def dictionary_iterator(file_path):
    with open(file_path, 'r', errors='ignore') as file:
        for line in file:
            word = line.strip()  # remove newline characters
            print(word)
            time.sleep(1)  # delay for 1 second

# Part 2: Password Recognized Function (Mode 2)
# This function takes a string and a file path as input. It opens the file and checks if the string appears in the file.
# If the string is found in the file, it prints a message indicating that the string was found.
# Otherwise, it prints a message indicating that the string was not found.
def password_recognized(string, file_path):
    with open(file_path, 'r', errors='ignore') as file:
        if string in file.read():
            print(f"The string '{string}' was found in the word list.")
        else:
            print(f"The string '{string}' was not found in the word list.")

# Part 3: Password Complexity Function (Mode 3)
# This function takes a password string as input and evaluates its complexity based on certain metrics.
# The metrics checked include the length of the password, the presence of capital letters, numbers, and symbols.
# It prints whether each metric is satisfied by the password and then gives an overall SUCCESS or FAILURE message.
def password_complexity():
    password = getpass.getpass("Enter a password: ")  # Use getpass to securely get the password from the user
    metrics = {
        'length': len(password) >= 8,  # replace 8 with your desired length
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

# Part 4: Main Function
# This function is the main entry point of the script.
# It prompts the user to select a mode and takes appropriate actions based on the chosen mode.
# For mode 1, it asks for the path to the word list file and calls the dictionary_iterator function.
# For mode 2, it asks for a string and the path to the word list file and calls the password_recognized function.
# For mode 3, it calls the password_complexity function.
def main():
    print("Select a mode:")
    print("1: Offensive; Dictionary Iterator")
    print("2: Defensive; Password Recognized")
    print("3: Defensive; Password Complexity")
    mode = int(input("Enter the number of your chosen mode: "))

    if mode == 1:
        file_path = input("Enter the path to the word list file: ")
        dictionary_iterator(file_path)
    elif mode == 2:
        string = input("Enter a string: ")
        file_path = input("Enter the path to the word list file: ")
        password_recognized(string, file_path)
    elif mode == 3:
        password_complexity()
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()




# Sources: openai.com, github.com/codefellows