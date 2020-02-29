# get the part of the HTML source that list all the contaminents
from bs4 import BeautifulSoup
import requests
from pprint import  pprint


if __name__ == "__main__":
    URL = 'https://www.ewg.org/tapwater/system.php?pws=WA5372250'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_='contaminants-grid')



