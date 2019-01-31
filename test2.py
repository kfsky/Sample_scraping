import requests
from bs4 import BeautifulSoup
import re
import json

GOONET_BASE_SOURCE = 'https://www.goo-net.com/'
target_url = 'https://www.goo-net.com/usedcar/brand-LEXUS/car-NX/'

# response を保存
res = requests.get(target_url)
with open('./test.html', mode='w', encoding='utf-8') as f:
    f.write(res.text)
# response保存データの読み込み
with open('./test.html', 'r', encoding='utf-8') as f:
    html = f.read()


soup = BeautifulSoup(html, 'html.parser')
blocks = soup.find_all('div', attrs={'class', 'box_item_detail'})


def stripping(strings):

    if type(strings) is not str:
        return False

    aset = {
        1: [' ', ''],
        2: ['  ', ''],
        3: ['¥n', '']
    }

    for i in aset.values():
        strings = strings.replace(i[0], i[1])

    return strings


cars = []
car = {
    'price': None,
    'all_price': None,
    'guarantee': None,
    }
# reモジュール（正規表現）でvalueに格納
PRICE = r'本体価格(.+?)万円'
ALL_PRICE = r'支払総額(.+?)万円'
GUARANTEE = r'¥[保証付]:(.+?)ヶ月'

for block in blocks:
    s = stripping(block.find('td').text)

    print(s)

    m = re.search(GUARANTEE, s)

    if m is not None:
        print(m.group(1))
    else:
        print('not match')

#    print(re.search(PRICE, s).group(1))
#    print(re.search(ALL_PRICE, s).group(1))
#    print(re.search(GUARANTEE, s).group(1))

SCRAPING_ASET = {
    'price': PRICE,
    'All_price': ALL_PRICE,
    'guarantee': GUARANTEE
}


def scrapping(strings):
    if type(strings) is not str:
        return False

    car_data = {}
    for k, v in SCRAPING_ASET.items():
        result = re.search(v, strings)
        if result:
            car_data[k] = result.group(1)

    return car_data


for block in blocks:
    s = stripping(block.find('td').text)
    print(scrapping(s))

datas = []
for block in blocks:
    s = stripping(block.find('td').text)
    datas.append(scrapping(s))
    print(scrapping(s))

with open('./test.json', 'w') as f:
    json.dump(
        datas,
        f,
        indent=4,
        ensure_ascii=False
    )