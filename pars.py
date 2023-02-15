import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9'
              ',image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
list_card_url = []
lst_1 = []

for item in range(1, 5):
    url = 'https://apteka-ot-sklada.ru/catalog/sredstva-gigieny/' \
          'uhod-za-polostyu-rta/zubnye-niti_-ershiki'

    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')

    all_product = soup.find_all('div',
                                class_='ui-card ui-card_size_default ui-card_outlined goods-card goods-grid__cell'
                                       ' goods-grid__cell_size_3')
    for card in all_product:
        link_card = 'https://apteka-ot-sklada.ru' + card.find('a').get('href')
        list_card_url.append(link_card)

for i in list_card_url:

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    response_2 = requests.get(i, headers=headers).text
    soup_2 = BeautifulSoup(response_2, 'lxml')
    block = soup_2.find('div', class_='layout-default__page')
    title = block.find('h1', class_='text text_size_display-1 text_weight_bold').text
    table_head = soup_2.find('div', class_='layout-default__page').find('ul', class_='ui-breadcrumbs__list'). \
        find_all('li', class_='ui-breadcrumbs__item')
    main = table_head[0].text
    catalog = table_head[1].text
    hygiene_products = table_head[2].text
    oral_care = table_head[3].text
    dental_floss = table_head[4].text
    discount = block.find('div', class_='goods-offer-panel__price').find_all('span')[0].text
    if block.find('span',
                  class_='goods-offer-panel__cost goods-offer-panel__cost_old text text_size_title text_weight_medium'):
        original = block.find('span',
                              class_='goods-offer-panel__cost goods-offer-panel__cost_old text text_size_title text_weight_medium').get_text()
        current = block.find('span',
                             class_='goods-offer-panel__cost text text_size_display-1 text_weight_bold goods-offer-panel__cost_new').get_text()
    else:
        original = block.find('div', class_='goods-offer-panel__price').get_text()
    original_pr = float(original[9:-9])
    discount_pr = float(discount[9:-9])
    sale_tag = f'Скидка: {round(100 - ((discount_pr / original_pr) * 100))} %'
    stock = True if original else False
    main_image = 'https://apteka-ot-sklada.ru' + block.find('img').get('src')
    if block.find('div', class_='custom-html content-text'):
        text = block.find('div', class_='ui-collapsed-content__content').text
        text_2 = block.find('div', class_='custom-html content-text').text.replace('\r\n\t', '')
    else:
        text = block.find('div', class_='goods-details-page__other-info').text.replace('\n', '')
    country = block.find('div', class_='page-header__description').find('span').text
    legal_name = str(block.find('div', class_='page-header__description').find_all('span'.split())[1])[27:-7]

    lst_1.append({
        'timestamp': current_time,
        'RPC': 'Отсутствует',
        'url': i,
        'title': title,
        'section': [main, catalog, hygiene_products, oral_care, dental_floss],
        'price_data': {'current': discount_pr, 'original': original_pr, 'sale_tag': sale_tag},
        'stock': {'in_stock': stock},
        'assets': {'main_image': main_image},
        'metadata': {'__description': text, 'Страна производитель': country, 'Название производителя': legal_name,
                     'Артикул': None}
    })

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9'
              ',image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
list_card_url_noose = []
lst_2 = []

for item in range(1, 5):
    url_2 = 'https://apteka-ot-sklada.ru/catalog/sredstva-gigieny/nosovye-platki'
    response = requests.get(url_2, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    all_product_url = soup.find_all('div',
                                    class_='ui-card ui-card_size_default ui-card_outlined goods-card goods-grid__cell'
                                           ' goods-grid__cell_size_3')
    for item in all_product_url:
        url_card = 'https://apteka-ot-sklada.ru' + item.find('a').get('href')
        list_card_url_noose.append(url_card)

for elem in list_card_url_noose:

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    response_2 = requests.get(elem, headers=headers).text
    soup_2 = BeautifulSoup(response_2, 'lxml')
    block = soup_2.find('div', class_='layout-default__page')
    title = block.find('h1', class_='text text_size_display-1 text_weight_bold').text
    table_head = soup_2.find('div', class_='layout-default__page').find('ul', class_='ui-breadcrumbs__list'). \
        find_all('li', class_='ui-breadcrumbs__item')
    main = table_head[0].text
    catalog = table_head[1].text
    hygiene_products = table_head[2].text
    handkerchiefs = table_head[3].text

    if block.find('div', class_='goods-offer-panel__price'):
        ori_2 = block.find('span', class_='goods-offer-panel__cost text text_size_display-1 text_weight_bold').text
        original_pr = float(ori_2[9:-9])
    stock = True if original_pr else False
    main_image = 'https://apteka-ot-sklada.ru' + block.find('img').get('src')
    if block.find('div', class_='custom-html content-text'):
        text = block.find('div', class_='ui-collapsed-content__content').text
        text_2 = block.find('div', class_='custom-html content-text').text
    else:
        text = block.find('div', class_='goods-details-page__other-info').text.replace(' ', '')
    country = block.find('div', class_='page-header__description').find('span').text
    legal_name = str(block.find('div', class_='page-header__description').find_all('span'.split())[1])[27:-7]

    lst_2.append({
        'timestamp': current_time,
        'RPC': 'Отсутствует',
        'url': elem,
        'title': title,
        'section': [main, catalog, hygiene_products, handkerchiefs],
        'price_data': {'current': original_pr, 'original': original_pr, 'sale_tag': 0},
        'stock': {'in_stock': stock},
        'assets': {'main_image': main_image},
        'metadata': {'__description': text, 'Страна производитель': country, 'Название производителя': legal_name,
                     'Артикул': None}
    })

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9'
              ',image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
list_card_url_noose = []
lst_3 = []

for item in range(1, 28):

    url_3 = 'https://apteka-ot-sklada.ru/catalog/kosmetika/bannye-serii'
    response = requests.get(url_3, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    all_product_url = soup.find_all('div',
                                    class_='ui-card ui-card_size_default ui-card_outlined goods-card goods-grid__cell'
                                           ' goods-grid__cell_size_3')
    for item in all_product_url:
        url_card = 'https://apteka-ot-sklada.ru' + item.find('a').get('href')
        list_card_url_noose.append(url_card)

for elem in list_card_url_noose:

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    response_2 = requests.get(elem, headers=headers).text
    soup_2 = BeautifulSoup(response_2, 'lxml')
    block = soup_2.find('div', class_='layout-default__page')
    title = block.find('h1', class_='text text_size_display-1 text_weight_bold').text
    title_str = ''.join([i for i in title if not i.isdigit()])[:-2]
    title_numb = ''.join([i for i in title if i.isdigit()]) + ' мл'
    table_head = soup_2.find('div', class_='layout-default__page').find('ul', class_='ui-breadcrumbs__list'). \
        find_all('li', class_='ui-breadcrumbs__item')
    main = table_head[0].text
    catalog = table_head[1].text
    cosmetic = table_head[2].text
    bath_series = table_head[3].text
    if block.find('div', class_='goods-offer-panel__price'):
        ori_2 = block.find('span', class_='goods-offer-panel__cost text text_size_display-1 text_weight_bold').text
        original_pr = float(ori_2[9:-8].replace(' ', ''))
    stock = True if original_pr else False
    main_image = 'https://apteka-ot-sklada.ru' + block.find('img').get('src')
    if block.find('div', class_='custom-html content-text'):
        text = block.find('div', class_='ui-collapsed-content__content').text
        text_2 = block.find('div', class_='custom-html content-text').text
    else:
        text = block.find('div', class_='goods-details-page__other-info').text.replace(' ', '')
    country = block.find('div', class_='page-header__description').find('span').text
    legal_name = str(block.find('div', class_='page-header__description').find_all('span'.split())[1])[27:-7]
    lst_3.append({
        'timestamp': current_time,
        'RPC': 'Отсутствует',
        'url': elem,
        'title': {'название': title_str, 'объем': title_numb},
        'section': [main, catalog, cosmetic, bath_series],
        'price_data': {'current': original_pr, 'original': original_pr, 'sale_tag': 0},
        'stock': {'in_stock': stock},
        'assets': {'main_image': main_image},
        'metadata': {'__description': text, 'Страна производитель': country, 'Название производителя': legal_name,
                     'объем': title_numb, 'Артикул': None}
    })

if __name__ == "__main__":
    print(lst_1)
    print(lst_2)
    print(lst_3)

    with open(f'data_1.json', 'a', encoding='utf-8') as file:
        json.dump(lst_1, file, indent=4, ensure_ascii=False)

    with open(f'data_2.json', 'a', encoding='utf-8') as file:
        json.dump(lst_2, file, indent=4, ensure_ascii=False)

    with open(f'data_3.json', 'a', encoding='utf-8') as file:
        json.dump(lst_3, file, indent=4, ensure_ascii=False)

