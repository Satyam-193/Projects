import requests
from bs4 import BeautifulSoup

file = requests.get('https://www.guru99.com/bug-bounty-programs.html')
soup = BeautifulSoup(file, 'lxml')
links = soup.find('h3', class_='toc-ignore')
print(links.text)
