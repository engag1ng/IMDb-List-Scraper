# IMDb-List-Scraper
Provides a basic python function for scraping titles from a public IMDb list.

The script uses [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) for web-scraping and [selenium](https://www.selenium.dev/documentation/webdriver/) to bypass 'lazy loading' and ensure full lists.

> [!NOTE]
> This only works on **public** lists. If a list is not public an empty list will be returned.

## Usage
1. Copy the `scrape_list.py` file into your project.
2. Import the `scrapeList` function with the following command: `from scrape_list import scrapeList`
3. Use the function using the following command: `scrapeList(<link>)`

Even though this only 40 lines of code and very simple I couldn't find anything that did something similar online. I hope it helps. Thank you, and enjoy!
