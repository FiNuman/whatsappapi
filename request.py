import requests

text = "Hello, Bard AI!"

response = requests.get("http://127.0.0.1:5000//get_bard_response/" + text)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Request failed with status code:", response.status_code)