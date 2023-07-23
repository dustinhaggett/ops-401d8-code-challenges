# Set password complexity requirements
Set-LocalUser -Name "Zuko" -PasswordNeverExpires $false

# Disable SMBv1 client
Set-SmbClientConfiguration -EnableSMB1Protocol $false

# Restart the computer
Restart-Computer
