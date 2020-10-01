import requests
from bs4 import BeautifulSoup


url = 'https://www.strava.com/segments/902554?filter=overall'

page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')

mydivs = soup.findAll("td")

for div in mydivs:
    print(div)

i = 0

while (i < len(mydivs)):
    rank = mydivs[i]
    name = mydivs[i + 1]
    i += 3
    print(rank, name)

