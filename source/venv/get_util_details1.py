import requests
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import re
from get_contaminent_details1 import  get_contaminent_details
from assign_data1 import  assign_data
from get_contam_dicts1 import  get_contam_dicts
from get_util_name1 import  get_util_name
import json
from pprint import  pprint

def get_util_details(soup):
    """get the utility details: the city, the number of people utility serves, the dates data available, and source"""
    ud = soup.find('ul', class_="served-ul")
    if ud == None:
        return {'city':'nan', 'serves':'nan', 'data_available':'nan', 'source':'nan'}
    list_items = ud.find_all('li')
    if list_items == None:
        return {'city':'nan', 'serves':'nan', 'data_available':'nan', 'source':'nan'}
    util_details = []
    for li in list_items:
        util_details.append(li.text.strip())
    if len(util_details) != 4:
        return {'city':'nan', 'serves':'nan', 'data_available':'nan', 'source':'nan'}
    return {'city':util_details[0], 'serves':util_details[1], 'data_available':util_details[2], 'source':util_details[3]}

if __name__ == "__main__":
    for id_ in [5338100, 5394900, 5369750, 5353263, 5356851, 5368045, 5368045, 5310724, 5305800]:
        URL = 'https://www.ewg.org/tapwater/system.php?pws=WA' + str(id_)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        util_details = get_util_details(soup)
        pprint(util_details)

