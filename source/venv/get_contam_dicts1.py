from bs4 import BeautifulSoup
import requests
import re
from get_contaminent_details1 import  get_contaminent_details
from assign_data1 import  assign_data
from pprint import pprint


def get_contam_dicts(contam_dict):
    """get the dictionary of contaminating chemicals for a particular city"""
    city_contams = {}
    for c in contam_dict.keys():
        city_contams[c] = assign_data(c, contam_dict[c])
    return city_contams


if __name__ == "__main__":
    URL = 'https://www.ewg.org/tapwater/system.php?pws=WA5372250'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    contam_dict = get_contaminent_details(soup)
    city_contams = get_contam_dicts(contam_dict)
    pprint(city_contams)

