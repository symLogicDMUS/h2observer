from bs4 import BeautifulSoup
import requests
from pprint import pprint
import re
from get_contaminent_details1 import  get_contaminent_details
from assign_data1 import  assign_data
from get_contam_dicts1 import  get_contam_dicts
from get_util_name1 import  get_util_name
from get_util_details1 import  get_util_details
import json
import os

if __name__ == "__main__":
    util_data = {}
    URL = 'https://www.ewg.org/tapwater/system.php?pws=WA'
    for id_ in [5338100, 5394900, 5369750, 5353263, 5356851, 5368045, 5368045, 5310724, 5305800]:
    # for i in range(5300000, 5399999):
        # print(i)
        # page = requests.get(URL + str(i))
        page = requests.get(URL + str(id_))
        print(id_)
        soup = BeautifulSoup(page.content, 'html.parser')
        util_name = get_util_name(soup)
        util_details = get_util_details(soup)
        if util_name == None:
            continue
        if util_details == {'city':'nan', 'serves':'nan', 'data_available':'nan', 'source':'nan'}:
            continue
        contam_data = get_contaminent_details(soup)
        contam_data = get_contam_dicts(contam_data)
        util_data[util_name] = {}
        util_data[util_name]['contamination_data'] = contam_data
        util_data[util_name]['utility_details'] = util_details
    pprint(util_data)
    with open('./utilities.json', 'w') as json_file:
        json.dump(util_data, json_file)
    json_file.close()


