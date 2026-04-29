import requests

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            print("API Call Successful")
            print("Title:", data['title'])
            print("Body:", data['body'])
        else:
            print("API Failed:", response.status_code)

    except Exception as e:
        print("Error:", e)

fetch_data()