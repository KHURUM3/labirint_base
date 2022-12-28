
BOT_NAME = 'labirint_base'

SPIDER_MODULES = ['labirint_base.spiders']
NEWSPIDER_MODULE = 'labirint_base.spiders'

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 16

FEED_EXPORT_ENCODING = 'utf-8'

FEED_FORMAT = "csv"

FEED_URI = "labirintcsv"

ITEM_PIPELINES = {

      'labirint_base.pipelines.SavingToMySQLPipeline' : 100,

}
