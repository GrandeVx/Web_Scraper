from bs4 import BeautifulSoup
import search
import requests

# Request the URL of The Page
url = input(":: Inserire Indirizzo :> ")

# Open a Session and clone the page
response = requests.get(url)

# Generate a Soup Object of The Source Code
soup = BeautifulSoup(response.text,'html.parser')

sito = search.Search(soup)

sito.Dati()

# bsurl = "maxcdn.bootstrapcdn.com"

# link = soup.find_all(name = "link")

# bootstrap = False


# for x in link:
#     if bsurl in str(x.get("href")):
#         print("ciao")