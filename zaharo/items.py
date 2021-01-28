import scrapy


class ZaharoItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
