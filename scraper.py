import requests
from bs4 import BeautifulSoup
import json

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        dd_tags = soup.find_all("dd")
        words = []
        for dd_tag in dd_tags:
            word = dd_tag.find("a").text
            words.append(word)
        return words
        
    else:
        print("Couldn't access data", response.status_code)
        return None
    

page_data = scrape_website("https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Korean_5800")

print(page_data)