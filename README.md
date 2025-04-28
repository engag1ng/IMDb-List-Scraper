# IMDb-List-Scraper
Provides a basic python function for scraping titles from a public IMDb list.

The script uses [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) for web-scraping and [selenium](https://www.selenium.dev/documentation/webdriver/) to bypass 'lazy loading' and ensure full lists.

> [!NOTE]
> This only works on **public** lists. If a list is not public an empty list (array) will be returned.

Even though this only 40 lines of code and very simple I couldn't find anything that did something similar online. I hope it helps. Thank you, and enjoy!

**⭐Please star this repository!**

## Installation
1. Download the script: `$ get https://github.com/engag1ng/IMDb-List-Scraper/blob/main/scrape_list.py`
2. Install dependencies with pip: `$ pip install beautifulsoup4 selenium`
3. Import the `scrapeList` function with the following line in Python: `from scrape_list import scrapeList`

## Usage
Use the function using the following command: `scrapeList(<link>)`

## Contributing
This is a very simple repository. It's simple but it works. If you have any feature suggestions please open an **issue**. For improvements please open a **pull request**.
