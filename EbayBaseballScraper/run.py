from scrapy import cmdline
import sys
cmdline.execute("scrapy crawl {} -o output/{}.json".format(sys.argv[1], sys.argv[1]).split())
