import requests
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "first name": "Rahul",
    "last name": "Sati",
    "roll no": 48
}

headers = {'Content-type': 'application/json; charset=UTF-8'}
response = requests.post(url, headers=headers, json=data)
print(response.text)
