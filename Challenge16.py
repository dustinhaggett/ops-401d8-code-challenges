import time
import getpass

# Part 1: Dictionary Iterator Function (Mode 1)
def dictionary_iterator():
    try:
        filepath = input("Enter your dictionary filepath:\n")
        with open(filepath, encoding="ISO-8859-1") as file:
            for line in file:
                word = line.rstrip()
                print(word)
                time.sleep(1)
        print("Iteration completed!")
    except FileNotFoundError:
        print("File not found. Please provide a valid filepath.")

# Part 2: Password Recognized Function (Mode 2)
def password_recognized():
    try:
        filepath = input("Enter your dictionary filepath:\n")
        string = getpass.getpass("Enter a string: ")
        with open(filepath, encoding="ISO-8859-1") as file:
            if string in file.read():
                print(f"The string '{string}' was found in the word list.")
            else:
                print(f"The string '{string}' was not found in the word list.")
    except FileNotFoundError:
        print("File not found. Please provide a valid filepath.")

# Main Function
if __name__ == "__main__":
    while True:
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Exit
Please enter a number: 
""")
        if mode == "1":
            dictionary_iterator()
        elif mode == "2":
            password_recognized()
        elif mode == "3":
            break
        else:
            print("Invalid selection...")





# Sources: 
# https://github.com/codefellows/seattle-cybersecurity-401d8/blob/main/class-16/challenges/DEMO.md
# https://openai.com 