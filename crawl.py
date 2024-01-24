import requests
from bs4 import BeautifulSoup


def search(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    return [link['href'] for link in links if 'http' in link['href']]
