import requests

print("Lab 9 - Final Readiness Task")

try:
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    
    if response.status_code == 200:
        data = response.json()
        print("API Call Successful")
        print("Data:", data)
    else:
        print("API Failed with status:", response.status_code)

except Exception as e:
    print("Error:", e)