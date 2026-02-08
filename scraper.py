import requests
from bs4 import BeautifulSoup

def fetch_headlines():
    url = "https://news.ycombinator.com/"
    headers = {'User-Agent': 'MyDataScraperBot/1.0'}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    
    # Selecting the headline elements
    links = soup.select('.titleline > a')
    for link in links:
        articles.append({
            'title': link.get_text(),
            'url': link.get('href')
        })
    return articles