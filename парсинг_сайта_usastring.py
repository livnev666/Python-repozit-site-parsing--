import requests
from bs4 import BeautifulSoup
import fake_useragent
import json
import pandas as pd



user = fake_useragent.UserAgent().random
headers = {
    'user-agent': user,
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
link = 'https://usastrings.ru/'

response = requests.get(link, headers=headers).text
soup = BeautifulSoup(response, 'lxml')
button_strings = soup.find('a', class_='with-child dropdown-toggle').get('href')

response_2 = requests.get(url=button_strings, headers=headers).text
soup2 = BeautifulSoup(response_2, 'lxml')
string_6 = str(soup2.find('div', class_='box')).split()[33][6:-2]
response_3 = requests.get(url=string_6, headers=headers).text

with open('string_index.html', 'w', encoding='utf-8') as file:
    file.write(response_3)

with open('string_index.html', encoding='utf-8') as file:
    response = file.read()

soup = BeautifulSoup(response, 'lxml')


list_all_6_strings = soup.find('div', class_='row rowf flex_height_row').find_all('div', class_='gtile-i-wrap')


def downloads_img(url):

    image_number = 0
    res = requests.get(url, stream=True).content
    with open(f'C:/Users/Admin/Desktop/photos_string/{image_number}.jpg' + url.split(), 'wb') as file:
        file.write(res)
    image_number += 1

def get_url_ip():

    for group in range(1, 10 + 1):
        for item in list_all_6_strings:
            get_href = item.find('a').get('href')
            yield get_href


def arrows_north():

    for i in get_url_ip():
        res = requests.get(i, headers=headers).text
        soup_2 = BeautifulSoup(res, 'lxml')
        name_string = soup_2.find('h1', class_='pr_h1').text
        description_string = soup_2.find('div', class_='desc_hide_pr').text
        price_string = soup_2.find('span', class_='autocalc-product-special').text
        image_link = soup_2.find('div', class_='col-xs-12 col-sm-12').find('img').get('src')
        downloads_img(image_link)
        nun = soup_2.find('div', class_='attribute_groups attr_shot').find_all('ul', class_='atr')
        dict_value = {}
        lst = []
        for j in nun:
            key_name = j.find('span').text
            value_key = j.find_all('span')[1].text
            dict_value[key_name] = value_key
            # lst.append(dict_value)
            yield name_string, description_string, price_string, image_link







