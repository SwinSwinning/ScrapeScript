print(" Loading Dependencies")

from scrapy.crawler import CrawlerProcess
print(" Loading Dependencies 1")
from scrapy.utils.project import get_project_settings
print(" Loading Dependencies 2")
from spiders.scrapespider import ScrapeSpider
import yaml

print(" Loading main script")
if __name__ == "__main__":
    # Testmode limits the amount of items returns. Set to "false" to scrape all items.
    testmode = True
    print(" Loading project settings")
    settings = get_project_settings()
    settings['FEEDS'] = {'output.json': {'format': 'json', 'overwrite': 'true'}}
    if testmode:
        settings['CLOSESPIDER_ITEMCOUNT'] = 5
        settings['EXTENSIONS'] = {
            'scrapy.extensions.closespider.CloseSpider' : 500
        }

    settings['USER_AGENT'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.100.0' # Make user agent default to browser used.

    print("Loading selectors from selectors.yaml")
    with open('selectors.yaml', 'r') as f:
        all_selectors = yaml.safe_load(f)

    # CHOOSE WHICH SITE TO SCRAPE HERE
    # The key should match one of the keys in your selectors.yaml file
    site_to_scrape = "old_reddit"
    site_settings = all_selectors[site_to_scrape]

    print("attempting scrape task with following settings: ", site_settings)

    process = CrawlerProcess(settings=settings)
    process.crawl(ScrapeSpider, export_settings=site_settings)
    process.start()

    print("scrape completed")
   # input("Press any key to exit")

