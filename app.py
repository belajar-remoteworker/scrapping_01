import bs4
import requests

url = 'https://jadwalsholat.pkpu.or.id/?id=308'
contents = requests.get(url)
#print(contents.text)

response = bs4.BeautifulSoup(contents.text, "html.parser")

print(response)
