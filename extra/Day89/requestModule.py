# this is get request
import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)
print(x.content)
print(x.status_code)
print(x.headers)
print(x.url)
# print(x.json)
# request module allow us to send http request using python
# the http request returns a response object with all the response data (content, encoding, status, etc)
