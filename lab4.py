import requests

# API URL (free public API)
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    # Call API
    response = requests.get(url)

    # Check status
    if response.status_code == 200:
        print("✅ API Call Successful!")
        
        # Convert to JSON
        data = response.json()
        
        # Print response
        print("\n📦 Response Data:")
        print(data)

    else:
        print("⚠️ API Failed with status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("❌ Error occurred:", e)