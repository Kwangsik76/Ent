import requests
from bs4 import BeautifulSoup
import html

URL = "http://www.k-apt.go.kr/bid/bidList.do?search_bid_gb=bid_gb_1&bid_title=&apt_name=&search_date_gb=reg&date_start=2023-05-26&date_end=2023-06-26&date_area=1&bid_state=&code_auth=&code_way=&code_auth_sub=&code_suc_way=&code_classify_type_1=&code_classify_type_2=&code_classify_type_3=&pageNo=1&type=4&bid_area=11&bid_num=&bid_no=&d_time=1687786803735&main_kapt_code="
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#tblBidList > tbody > tr')

results = []

for tr in trs:
    row_dict = {}

    id = tr.find('td', onclick=lambda value: value.startswith("javascript:goView('"))['onclick']
    id = id.split("'")[1]
    row_dict['id'] = id

    title_text = tr.find('td', class_='txtL', colname='bid_title').text.strip()
    title_text = html.unescape(title_text)
    title = ' '.join(title_text.split())
    row_dict['title'] = title

    apt_name = tr.find('td', class_='txtL', colname='apt_name').text.strip()
    apt_name = html.unescape(apt_name)
    apt_name = ' '.join(apt_name.split())
    row_dict['apt_name'] = apt_name


    create_date = tr.find_all('td')[7].text.strip()
    row_dict['create_date'] = create_date

    results.append(row_dict)

print(results)
