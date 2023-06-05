import scrapy
import json
from urllib.parse import parse_qs, urlparse


class MlbStatsSpider(scrapy.Spider):
    name = "mlb_stats_spider"

    start_urls = []
    for i in range(1900, 2024):
        start_urls.append("https://bdfed.stitch.mlbinfra.com/bdfed/stats/player?stitch_env=prod&season={}&sportId=1&stats=season&group=hitting&gameType=R&limit=250&offset=0&sortStat=onBasePlusSlugging&order=desc".format(i))

    def parse(self, response):
        data = json.loads(response.body)
        for stat in data["stats"]:
            yield stat
