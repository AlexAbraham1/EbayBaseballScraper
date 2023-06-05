from scrapy import cmdline
cmdline.execute("scrapy crawl ebay_baseball_spider -o output.json".split())
