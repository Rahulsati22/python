from bs4 import BeautifulSoup
import requests
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

# printing all the heading in the given code
for heading in soup.find_all("h2"):
    print(heading.text)

# printing all the paragraph in the given code
for para in soup.find_all("p"):
    print(para.text)

# this above procedure is known as scrapping
