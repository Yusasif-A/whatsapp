import requests
try:
    response = requests.get("https://api.langgraph.com", timeout=10)
    print(response.status_code, response.text)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")