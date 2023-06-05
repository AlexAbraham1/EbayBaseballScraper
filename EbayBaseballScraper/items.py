# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EbayItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    date_sold = scrapy.Field()
    condition = scrapy.Field()
    price = scrapy.Field()
    num_bids = scrapy.Field()
    shipping = scrapy.Field()
    seller_username = scrapy.Field()
    seller_num_reviews = scrapy.Field()
    seller_pct_positive_feedback = scrapy.Field()

    def __repr__(self):
        return repr({
            "name": self["name"],
            "price": self["price"],
            "date_sold": self["date_sold"]
        })
