import requests

res = requests.post(
    "https://secure-chat111.onrender.com/signup",
    json={"username": "test", "password": "test123"}
)

print("Status Code:", res.status_code)
print("Response:", res.text)
