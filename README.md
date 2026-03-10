# Configurable Web Scraper

This is a web scraper built with Scrapy that can be configured to scrape different websites using a YAML file.

### Features
*   **Configurable Targets:** Define multiple scraping configurations in [`selectors.yaml`](selectors.yaml).
*   **Generic Spider:** Uses a single Scrapy spider [`spiders/scrapespider.py`](spiders/scrapespider.py) capable of following pagination links and scraping data from item pages or the main listing page.
*   **Test Mode:** Includes a test mode in [`scrapyscript.py`](scrapyscript.py) to limit the number of items scraped for quick testing.
*   **JSON Output:** Saves all scraped data to `output.json` by default.

### How to Use

#### 1. Configuration

All scraping targets are defined in [`selectors.yaml`](selectors.yaml). Each key in this file (e.g., `playstation`, `guten`, `books`, `old_reddit`) represents a site configuration.

To scrape a specific site, edit [`scrapyscript.py`](scrapyscript.py) and change line 31:
```python
# CHOOSE WHICH SITE TO SCRAPE HERE
# The key should match one of the keys in your selectors.yaml file
site_to_scrape = "old_reddit" 
```
to match your desired configuration key.

#### 2. Execution

Run the main script from the terminal:
```bash
python scrapyscript.py
```
By default, `scrapyscript.py` runs in **Test Mode** (lines 13, 18-21). To scrape all items instead of the limit set in test mode, change `testmode` on line 13 to `False`.

### Installation

1.  **Clone/Navigate to Project:** Ensure you are in the project root directory (`c:/Users/vanopstala/vsCODE/Scraping Projects/ScrapeScript`).
2.  **Install Dependencies:** Install the required Python packages using `pip`. You may need to create and activate a virtual environment first.

    ```bash
    pip install -r requirements.txt
    ```
3.  **Run Scraper:** Follow the instructions in the [How to Use](#how-to-use) section above.
