import time
import getpass

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

# Main Function
if __name__ == "__main__":
    while True:
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Defensive, Password Complexity
4 - Exit
Please enter a number: 
""")
        if mode == "1":
            dictionary_iterator()
        elif mode == "2":
            password_recognized()
        elif mode == "3":
            password_complexity()
        elif mode == "4":
            break
        else:
            print("Invalid selection...")





# Sources: openai.com, github.com/codefellows