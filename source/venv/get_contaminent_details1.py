from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint

def get_contaminent_details(soup):
    """takes soup object as input and get the type of contaminent-name and number of times over the legal limit""
     :returns
     --------
     dict
     --------
     """
    contams = soup.find_all(class_="contaminant-name")
    if  contams == None:
        return ['nan' for i in range(0, 9)]
    contam_dict = {}
    for contam in contams:
        contam_vals = []
        name = contam.find('h3')
        data = contam.find_all('span')
        for d in data:
            if d != None:
                d = d.text.strip()
                if d == '':
                    contam_vals.append('nan')
                else:
                    contam_vals.append(d)
        if list(filter(lambda val: re.fullmatch(r'Potential[\s]+Effect:[\sA-za-z]+', val), contam_vals)) == []:
            contam_vals.insert(0, 'nan')
        if list(filter(lambda val: re.fullmatch(r'\d+[\.]*[\d]*x', val), contam_vals)) == []:
            contam_vals.insert(1, 'nan')
        if 'NO LEGAL LIMIT' in contam_vals:
            contam_vals.append('nan')
        if 'NO EWG HEALTH GUIDELINE' in contam_vals:
            contam_vals.insert(6, 'nan')
        if len(contam_vals) == 9 and name != None:
            contam_dict[name.text] = contam_vals

    return contam_dict


if __name__ == "__main__":
    URL = 'https://www.ewg.org/tapwater/system.php?pws=WA5372250'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    contam_dict = get_contaminent_details(soup)
    pprint(contam_dict)

