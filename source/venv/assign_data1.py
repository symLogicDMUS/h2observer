from bs4 import BeautifulSoup
import requests
import re
from get_contaminent_details1 import  get_contaminent_details
from pprint import pprint

def assign_data(contam_name, contam_data):
    """given the name of a contamination and the data for it, assign by dict values
    contam_name: str
    contam_data: list
    """
    contam_dict = {}
    if len(contam_data) != 9:
        print('error: data missing')
    for i in range(9):
        if i == 0:
            contam_dict['potential_effect'] = contam_data[i]
        elif i == 1:
            contam_dict['times_greater_than_legal'] = contam_data[i]
        elif i == 4:
            contam_dict['ppb'] = contam_data[i]
        elif i == 6:
            contam_dict['health_guideline'] = contam_data[i]
        elif i == 8:
            contam_dict['legal_limit'] = contam_data[i]

    return contam_dict

if __name__ == "__main__":
    URL = 'https://www.ewg.org/tapwater/system.php?pws=WA5372250'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    contam_dict = {}
    contam_dict0 = get_contaminent_details(soup)
    for c in contam_dict0.keys():
        contam_dict[c] = assign_data(c, contam_dict0[c])
    pprint(contam_dict)




