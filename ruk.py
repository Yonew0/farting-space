from bs4 import BeautifulSoup
import requests
import sys

query = sys.argv[1] if len(sys.argv) > 1 else input('Enter query: ')
url = f'https://www.kiddle.co/s.php?q={query}'

page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')

#print(soup, dir(soup))

for raw_img in soup.find_all('img'):
    link = raw_img('src')
    if link and link.startswith('https'):
        response = requests.get(link)
        with open("./today_avatar.jpg", "wb") as f:
            f.write(response.content)
        print('Аватар найден - today_avatar.jpg')
        break
    else:
        print("Аватар не найден")