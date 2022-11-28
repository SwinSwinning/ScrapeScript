from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.scrapespider import ScrapeSpider

if __name__ == "__main__":
    # Testmode limits the amount of items returns. Set to "false" to scrape all items.
    testmode = True

    settings = get_project_settings()
    settings['FEEDS'] = {'output.json': {'format': 'json', 'overwrite': 'true'}}
    if testmode:
        settings['CLOSESPIDER_ITEMCOUNT'] = 50
        settings['EXTENSIONS'] = {
            'scrapy.extensions.closespider.CloseSpider' : 500
        }

    settings['USER_AGENT'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.100.0' # Make user agent default to browser used.

    playstation = {  'start_url': 'https://store.playstation.com/nl-nl/pages/browse/1',
                     'item_links': True,
                     'item_css': '//a[@class="psw-link psw-content-link"]',
                     'next_page_url': '//button[@data-qa="ems-sdk-grid#ems-sdk-top-paginator-root#next"]',
                     'next_page_url_add': 'value',
                     'attributes_dict':{'title': 'h1.psw-m-b-5',
                                        'price': 'span[data-qa="mfeCtaMain#offer0#finalPrice"]'}
                     }

    guten = {        'start_url': 'https://www.gutenberg.org/ebooks/search/?sort_order=downloads',
                     'item_links': True,
                     'item_css': '//li[@class="booklink"]//a[@class="link"]',
                     'next_page_url': '//*+[contains(concat( " ", @class, " " ), concat( " ", "booklink", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "statusline", " " ))]//a',
                     'next_page_url_add': 'href',
                     'attributes_dict': {'title': '//h1',
                                         'language': '//*[(@id = "bibrec")]//tr[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]//td'}
                     }

    books = {        'start_url': 'https://books.toscrape.com/catalogue/page-1.html',
                     'item_links': True,
                     'item_css': '//h3/a',
                     'next_page_url': '//li[@class="next"]/a',
                     'next_page_url_add': 'href',
                     'attributes_dict': {'title': '//h1',
                                         'price': '//div[@class="col-sm-6 product_main"]/p[@class="price_color"]'}
                     }

    NHL = {          'start_url': 'https://www.scrapethissite.com/pages/forms/?page_num=1',
                     'item_links' : False,
                     'item_css': '//tr[@class="team"]',
                     'next_page_url': '//a[contains(@aria-label, "Next")]',
                     'next_page_url_add': 'href',
                     'attributes_dict': {'name': '//td[@class="name"]',
                                         'year': '//td[@class="year"]',
                                         'wins': '//td[@class="wins"]',
                                         'losses': '//td[@class="losses"]'}
                     }

    reddit = {       'start_url': 'https://old.reddit.com/',
                     'item_links' : True,
                     'item_css': '//*[@class="first"]',
                     'next_page_url': '//span[@class="next-button"]/a',
                     'next_page_url_add': 'href',
                     'attributes_dict': {'title': '//p[@class="title"]/a',
                                         'upvotes': '//div[@class="score"]/span[1]',
                                         'perc_upvotes' : '//div[@class="score"]',
                                         'comments': '//a[@class="bylink comments may-blank"]'
                                         }
                     }

    process = CrawlerProcess(settings=settings)
    process.crawl(ScrapeSpider, export_settings=reddit)
    process.start()
