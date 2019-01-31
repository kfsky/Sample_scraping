import pandas as pd
import re
from selenium import webdriver

browser = webdriver.Firefox()

prices = []
all_prices = []
guarantees = []
mileages = []

# 最初のページをブロック単位で取得
for page in range(1, 14):
    if page == 1:
        browser.get('https://www.goo-net.com/usedcar/brand-LEXUS/car-NX/')
    else:
        browser.get('https://www.goo-net.com/usedcar/brand-LEXUS/car-NX/index-{}.html'.format(page))
    elems = browser.find_elements_by_class_name('box_item_detail')

    # 本体価格を取得
    for elem in elems:
        elem_price = elem.find_element_by_class_name('car')
        price = elem_price.find_element_by_tag_name('em').text
        prices.append(price)

        # 支払総額を取得
        elem_allprice = elem.find_element_by_class_name('all')
        all_price = elem_allprice.find_element_by_tag_name('em').text
        all_prices.append(all_price)

        # 保証を取得
        elem_guarantee = elem.find_element_by_class_name('img_desc_02').text
        guarantee = re.search(r'(\d+)', elem_guarantee)
        if guarantee != None:
            guarantees.append(guarantee.group())
        else:
            guarantees.append(guarantee)

        # 走行距離を取得
        elem_table = elem.find_element_by_class_name('section_body')
        mileage_text = elem_table.find_element_by_class_name('w63').text
        mileage = re.match('[0-9].[0-9]', mileage_text)

        if mileage != None:
            mileages.append(mileage.group())
        else:
            mileages.append(mileage)

df = pd.DataFrame()
df['本体価格'] = prices
df['支払総額'] = all_prices
df['保証[ヶ月]'] = guarantees
df['走行距離[万km]'] = mileages

df




