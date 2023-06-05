import scrapy

class EbayBaseballSpider(scrapy.Spider):
    name = "ebay_baseball_spider"
    start_urls = ["https://www.ebay.com/sch/i.html?_from=R40&_nkw=baseball+card&_sacat=0&rt=nc&LH_Sold=1&LH_Complete=1"]

    def parse(self, response):
        html_blocks = response.xpath("//li[starts-with(@id, 'item')]")
        for html_block in html_blocks:
            item = {}

            item["date_sold"] = html_block.xpath(".//div[@class='s-item__caption-section']//text()").get()[6:]
            item['name'] = html_block.xpath(".//a[@class='s-item__link']//span[@role='heading']//text()").get()
            item['link'] = html_block.xpath(".//a[@class='s-item__link']/@href").get()
            item['condition'] = html_block.xpath(".//span[@class='SECONDARY_INFO']//text()").get()
            item['price'] = html_block.xpath(".//span[@class='s-item__price']//text()").get()
            item['num_bids'] = html_block.xpath(".//span[contains(@class, 's-item__bidCount')]//text()").get()
            item['shipping'] = html_block.xpath(".//span[contains(@class, 's-item__shipping')]//text()").get()

            seller_info = html_block.xpath(".//span[@class='s-item__seller-info-text']//text()").get().split(" ")
            item['seller_username'] = seller_info[0]
            item['seller_num_reviews'] = seller_info[1][1:-1]
            item['seller_pct_positive_feedback'] = seller_info[2]

            # Parse through 500 pages
            for pgn in range(2,500):
                new_url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=baseball+card&_sacat=0&rt=nc&LH_Sold=1&LH_Complete=1" + f"&_pgn={pgn}"
                yield scrapy.Request(new_url, callback=self.parse)

            yield item
