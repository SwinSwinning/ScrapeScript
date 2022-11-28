import scrapy
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urljoin
from spiders.utils import get_base_url, xpath_or_css


class ScrapeSpider(scrapy.Spider):
    name = 'scraper_spider'

    def __init__(self, *args, **kwargs):
        super(ScrapeSpider, self).__init__(*args, **kwargs)
        self.start_url = self.export_settings["start_url"]
        self.base_url = get_base_url(self.start_url)
        self.item_selector = self.export_settings['item_css']
        self.contain_item_links = self.export_settings['item_links']
        self.attrs_to_scrape = self.export_settings['attributes_dict']

    def start_requests(self):
        yield scrapy.Request(f'{self.start_url}')

    def parse(self, response):
        # This part handles the pagination and crawling through all the pages:
        path = xpath_or_css(response,
                            self.export_settings["next_page_url"],
                            self.export_settings['next_page_url_add'])
        combined = urljoin(self.base_url, path)
        yield scrapy.Request(combined)

        # This part handles the crawling of the individual items and if needed extract data from itempages.
        if self.contain_item_links:
            # if site has item links that need to be accessed, create LinkExtractor Object to help extract item links.
            # ...determine whether the item selector is xpath or css.
            link_extractor = LinkExtractor(restrict_xpaths=self.item_selector) if self.item_selector.startswith(
                '/') else \
                LinkExtractor(restrict_css=self.item_selector)

            for item_link in link_extractor.extract_links(response):  #..create requests for each item link found on page.
                item = {}
                request = Request(item_link.url,
                                  callback=self.parse_page2,
                                  cb_kwargs={ 'item': item })
                yield request

        else:  # If data to scrape is found on the same page...
            rows = response.xpath(self.item_selector)
            for row in rows:
                item = {}
                for k, v in self.attrs_to_scrape.items():
                    item[k] = xpath_or_css(row, v).strip()
                yield item


    def parse_page2(self, response, item):
        # item = response.meta['item']   ---- remove this no longer used as we have added the "item" to the args
        for k,v in self.attrs_to_scrape.items():
            # In case there are multiple selectors given in a list
            if type(v) == list:
                # Loop through each selector...
                for num in range(len(v)):
                    # and see if it gives a valid response
                    if xpath_or_css(response, v[num]):
                        item[k] = xpath_or_css(response, v[num]).strip()
                        break
            else:
                item[k] = xpath_or_css(response, v).strip()
        item['link'] = response.url

        yield item
