import scrapy

from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from w3lib.html import remove_tags

from ..items import ZaharoItem


class ZaharoSpider(scrapy.Spider):
	name = 'zaharo'
	start_urls = ['https://www.zaharo.bg/novini']

	def parse(self, response):
		text = response.xpath('//div[@class="region region-content"]/descendant::node()/text()[not(ancestor::a | ancestor::div[@class="field__label visually-hidden"])]').getall()
		title = ''
		project_text = ''
		projects = []
		for p in text:
			p = remove_tags(p.strip())
			if p[:7].lower() in ['проект ', 'проект:']:
				projects.append({'title': title, 'text': project_text})
				title = p
				project_text = ''
			else:
				project_text += p.strip()
		projects.append({'title': title, 'text': project_text})

		for pro in projects[1:]:
			item = ItemLoader(item=ZaharoItem(), response=response)
			item.default_output_processor = TakeFirst()
			item.add_value('title', pro['title'])
			item.add_value('description', pro['text'])

			yield item.load_item()
