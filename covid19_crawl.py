import requests
import re
from bs4 import BeautifulSoup


def crawling(soup):
    all_data = soup.find("table", id="main_table_countries_today").find("tbody").find_all("tr")
    data = {}
    for d in all_data:
        if d.get("style") != "display: none":
            name = d.find_all("td")[1].get_text()
            each_data ={}
            each_data['확진자'] = clean(d.find_all("td")[2].get_text())
            each_data['사망자'] = clean(d.find_all("td")[4].get_text())
            each_data['완치'] = clean(d.find_all("td")[6].get_text())
            data[name] = each_data
    return data
    
def clean(text):
    text = text.replace(' ','').replace(',','')
    if text == '' or text == 'N/A':
        return 'N/A'
    else:
        return int(text)

def main() :
    html = requests.get("https://www.worldometers.info/coronavirus/")
    soup = BeautifulSoup(html.text, "html.parser")
    covid_data = crawling(soup)

    for d in covid_data:
        print(d, covid_data[d])

if __name__ == "__main__" :
    main()

