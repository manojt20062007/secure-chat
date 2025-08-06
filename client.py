import requests

BASE_URL = "https://secure-chat111.onrender.com"
username = None

def signup():
    global username
    username = input("Enter new username: ")
    password = input("Enter password: ")

    res = requests.post(f"{BASE_URL}/signup", json={"username": username, "password": password})
    
    try:
        print(res.json()["message"])
    except Exception as e:
        print("[ERROR] Server returned non-JSON response:")
        print("Status Code:", res.status_code)
        print("Response Text:", res.text)

def login():
    global username
    username = input("Enter username: ")
    password = input("Enter password: ")

    res = requests.post(f"{BASE_URL}/login", json={"username": username, "password": password})
    if res.status_code == 200:
        print("✅ Login successful!")
        return True
    else:
        print("❌", res.json()["message"])
        return False

def send_message():
    while True:
        msg = input("> ")
        if msg.lower() == "exit":
            break
        res = requests.post(f"{BASE_URL}/send", json={"username": username, "message": msg})
        if res.status_code != 200:
            print("❌ Message not sent.")

def fetch_messages():
    res = requests.get(f"{BASE_URL}/messages")
    messages = res.json().get("messages", [])
    print("\n📨 Chat History:")
    for msg in messages:
        print(msg)

def main():
    print("1. Login\n2. Sign Up")
    choice = input("Choose option (1/2): ")
    if choice == "2":
        signup()
    if login():
        fetch_messages()
        send_message()

if __name__ == "__main__":
    main()
