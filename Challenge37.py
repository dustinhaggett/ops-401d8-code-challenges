import requests

# URL for the website you want to interact with
URL = 'https://example.com'  # Replace with the actual URL

# 1. Get/Set HTTP Headers Using Python Requests Module

# Get server response HTTP headers
response = requests.get(URL)
print(f"Server Response Headers: {response.headers}")

# Add custom headers to the HTTP request
custom_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'hello': 'hello_888'
}
response_with_custom_headers = requests.get(URL, headers=custom_headers)
print(f"Response with Custom Headers: {response_with_custom_headers.text}")

# 2. Get/Set Cookies Using Python Requests Module

# Python get HTTP cookies
print(f"HTTP Cookies: {response.cookies}")

# Send HTTP cookies to the web server
response_with_cookies = requests.get(URL, cookies=response.cookies)
print(f"Response with Cookies: {response_with_cookies.text}")

# 3. Use Session in Python Requests Module

# Create a session
session = requests.session()
response_session = session.get(URL)
print(f"Session Cookies: {session.cookies}")

print("Cookie Monster is proud!")









# Attribution to chatgpt4 code interpreter and codefellows github