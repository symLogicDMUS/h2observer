import requests
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import re

def get_util_name(soup):
    """get the name of the utility from the full html file soup object"""
    if re.search(r'<title>EWG\s+Tap\s+Water\s+Database\s+\|\s+|[:,a-zA-Z\s\-]+</title>', str(soup)) == None:
        return None
    m_obj = re.search(r'\|\s+[:,a-zA-Z\s\-]+', str(soup))
    util_name = m_obj.group(0)
    util_name = util_name.replace('|', '')
    util_name = util_name.strip()
    return util_name


if __name__ == "__main__":
    URL = 'https://www.ewg.org/tapwater/system.php?pws=WA'
    page_ids = [5338100, 5394900, 5369750, 5353263, 5356851, 5368045, 5368045, 5310724, 5305800]
    for id_ in page_ids:
        page = requests.get(URL + str(id_))
        soup = BeautifulSoup(page.content, 'html.parser')
        print(get_util_name(soup))



