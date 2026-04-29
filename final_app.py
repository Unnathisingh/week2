import requests

def main():
    print("🚀 Mini Sprint Challenge")

    try:
        url = "https://jsonplaceholder.typicode.com/users/1"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print("✅ API Call Successful")
            print("👤 Name:", data['name'])
            print("📧 Email:", data['email'])
        else:
            print("⚠️ API Failed:", response.status_code)

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()