import requests
import re
from bs4 import BeautifulSoup

# 기업에 대한 정보를 크롤링하는 함수입니다.
def crawling(soup):
    stock =[]
    rows = soup.find_all("div", class_="box_type_l")[1].find("tbody").find_all("tr")
    for row in rows:
        if row.find("td", class_= "name"):
            name = row.find("td", class_= "name").find("a").get_text()
            prices = row.find_all("td", class_="number")
            curP = prices[0].get_text()
            change_p = prices[1].get_text() 
            change_r = prices[2].get_text()
            stock.append([name+' ', curP, refine(change_p), refine(change_r)])
            #이름 뒤에 스페이스도 꼭 포함시켜야 하나???
    return stock

def refine(text):
    return text.replace("\t", "").replace("\n","")

def main() :
    # 주어진 url을 크롤링하세요.
    
    url = "https://finance.naver.com/sise/sise_group_detail.nhn?type=upjong&no=235"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    stock = crawling(soup)
    print(stock)
    
    data={}
    for s in stock:
        if s[3][0] =='+':
            data[s[0]] = int(s[1].replace(',',''))#현재가는 정수 자료형
    # 현재가가 오름차순이 되도록 data 딕셔너리를 출력하세요.
    data = sorted(data.items(), key = lambda x:x[1])
    print(data)

if __name__ == "__main__" :
    main()

