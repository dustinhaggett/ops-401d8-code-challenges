def main():
    host = "8.8.8.8"  # Specify the IP address you want to monitor
    interval = 2  # Interval between each ping in seconds

    sender_email = input("Enter your email address: ")
    sender_password = getpass("Enter your email password: ")
    recipient_email = input("Enter the recipient's email address: ")
    
    previous_status = None
    
    while True:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")
        if ping(host):
            current_status = "Network Active"
        else:
            current_status = "Network Inactive"
        
        if previous_status is not None and current_status != previous_status:
            subject = "Server Status Notification"
            if current_status == "Network Active":
                body = "Your server came back up."
            else:
                body = "Your server went down."
            
            body += f"\nTimestamp: {timestamp}"
            send_email(sender_email, sender_password, recipient_email, subject, body)
        
        print(f"{timestamp} {current_status} to {host}")
        
        previous_status = current_status
        time.sleep(interval)
    
    # Send email as a test when the loop breaks
    subject = "Test Email"
    body = "This is a test email to confirm that the script is running successfully."
    send_email(sender_email, sender_password, recipient_email, subject, body)
