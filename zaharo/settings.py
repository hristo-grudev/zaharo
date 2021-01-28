BOT_NAME = 'zaharo'

SPIDER_MODULES = ['zaharo.spiders']
NEWSPIDER_MODULE = 'zaharo.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'zaharo.pipelines.ZaharoPipeline': 100,

}