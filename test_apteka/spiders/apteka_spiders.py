import scrapy
import requests
from datetime import datetime
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule



class AptekaSpidersSpider(CrawlSpider):
    name = "apteka_spiders"
    allowed_domains = ["apteka-ot-sklada.ru"]
    start_urls = ["https://apteka-ot-sklada.ru/"]
    page_count = 5

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='ui-card__content ui-card__row ui-card__row_size_default']/div[@class='goods-card__name text text_size_default text_weight_medium']/a"), callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[contains(@class, 'item_next')]/a"))

    )

    def start_requests(self):
        for page in range(1, self.page_count):
            url = f'https://apteka-ot-sklada.ru/catalog/sredstva-gigieny%2Fuhod-za-polostyu-rta%2Fzubnye-niti_-ershiki?start={page}'
            yield scrapy.Request(url, callback=self.parse_pages)


    def parse_pages(self, response, **kwargs):
        for href in response.css('div.goods-grid__inner a::attr(href)').extract():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):

        now = datetime.now()
        item = {}
        item["timestamp"] = now.strftime("%H:%M:%S")
        item["RPC"] = None
        item["url"] = response.request.url
        item["title"] = response.xpath('//h1[@class="text text_size_display-1 text_weight_bold"]/span/text()').get()
        # item["price_data"] = {'': list(map(float, ''.join(response.xpath('//div[@class="goods-offer-panel__price"]/span/text()').getall()).strip()[::2].strip().split()))}
        item["price_data"] = {'current': float(response.xpath('//div[@class="goods-offer-panel__price"]/span/text()').getall()[0].strip().split()[0]),
                              'original': float(response.xpath('//div[@class="goods-offer-panel__price"]/span/text()').getall()[0].strip().split()[0])}
                              # Пока не могу понять, как вывести весь список словарей по каждому товару если добавить в словарь вторую цену(без скидки), если прописать
                              # код строки, который ниже, то в json сохранится только словарь с данными по одному товару. Делал разными способами, но пока нет верного
                              # ответа
        # if float(response.xpath('//div[@class="goods-offer-panel__price"]/span/text()').getall()):
        #     item["original"] = float(response.xpath('//div[@class="goods-offer-panel__price"]/span/text()').getall()[1].strip().split()[0])
        #
        # else:
        #     item["price_data"] = {'current': float(response.xpath('//div[@class="goods-offer-panel__price"]/span/text()').getall()[0].strip().split()[0])}
        sale_tag = f'Скидка: {round(100 - ((item["price_data"]["current"] / item["price_data"]["original"]) * 100))} %'
        item["sale_tag"] = sale_tag
        item["section"] = response.css('li.ui-breadcrumbs__item span::text').getall()
        item["stock"] = {'in_stock': True if item["price_data"]["original"] else False}
        item["assets"] = {'main_image': 'https://apteka-ot-sklada.ru' + response.css('div.goods-gallery__view img::attr(src)').get(),
                          'set_image': response.xpath('//div[@class="ui-gallery-modal__preview ui-gallery-modal__preview_active"]/img/@src').getall()}
        item["metadata"] = {'__description': ''.join(response.xpath('//div[@class="custom-html content-text"]/p/text()').getall()),
                            'country': response.css('div.page-header__description span::text').getall()[0].strip(),
                            'legal_name': response.css('div.page-header__description span::text').getall()[1].strip()}
        return item
