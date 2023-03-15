

# ПЕРЕДЕЛАТЬ И ДОРАБОТАТЬ!!!

# import scrapy
# from datetime import datetime
#
# class CatalogSpiderSpider(scrapy.Spider):
#     name = "catalog_spider"
#     allowed_domains = ["apteka-ot-sklada.ru"]
#     start_urls = ["https://apteka-ot-sklada.ru/catalog/sredstva-gigieny%2Fuhod-za-polostyu-rta%2Fzubnye-niti_-ershiki"]
#     page_count = 5
#
#     # Проходит по всем страницам раздела
#     def start_requests(self):
#         for page in range(1, self.page_count):
#             url = f'https://apteka-ot-sklada.ru/catalog/sredstva-gigieny%2Fuhod-za-polostyu-rta%2Fzubnye-niti_-ershiki?start={page}'
#             yield scrapy.Request(url, callback=self.parse_pages)
#
#     # проходим по всем ссылкам на карточку товаров
#     def parse_pages(self, response, **kwargs):
#         for href in response.css('div.goods-grid__inner a::attr(href)').extract():
#             url = response.urljoin(href)
#             yield scrapy.Request(url, callback=self.parse)
#
#     def parse(self, response, **kwargs):
#         lst = []
#         now = datetime.now()
#         current_time = now.strftime("%H:%M:%S")
#         title = response.css('h1 span::text').get()
#         title_str = ''.join([i for i in title if not i.isdigit()])[:-2]
#         title_int = ''.join([i for i in title if i.isdigit()]) + 'м'
#         price_original = float(response.css('div.goods-offer-panel__price span::text').getall()[1].strip()[:-2])
#         current = float(response.css('div.goods-offer-panel__price span::text').getall()[0].strip()[:-2])
#         if float(response.css('div.goods-offer-panel__price span::text').getall()[0].strip()[:-2]):
#             current = float(response.css('div.goods-offer-panel__price span::text').getall()[0].strip()[:-2])
#         else:
#             price_original = float(response.css('div.goods-offer-panel__price span::text').getall()[1].strip()[:-2])
#         sale_tag = f'Скидка: {round(100 - ((current / price_original) * 100))} %'
#         url = response.request.url
#         section = response.css('li.ui-breadcrumbs__item span::text').getall()
#         stock = True if price_original else False
#         main_image = response.css('div.goods-gallery__view img::attr(src)').get()
#         set_images = response.css('div.goods-gallery__sidebar img::attr(src)').get()
#         description = ''.join(response.css('div.ui-collapsed-content__content p').getall()).strip()
#         country = response.css('div.page-header__description span::text').getall()[0].strip()
#         legal_name = response.css('div.page-header__description span::text').getall()[1].strip()
#         lst.append({
#             'timestamp': current_time,
#             'RPC': None,
#             'url': url,
#             'title': {'name': title_str, 'volume': title_int},
#             'section': section,
#             'price_data': {'current': current, 'original': price_original, 'sale_tag': sale_tag},
#             'stock': {'stock': stock, 'count': 0},
#             'assets': {'main_image': main_image, 'set_images': set_images},
#             'metadata': {'__description': description, 'country': country, 'manufactured': legal_name}
#         })
#         yield lst


















