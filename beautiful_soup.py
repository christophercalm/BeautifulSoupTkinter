"""
Tutorial to do beautiful soup web scraping
Christopher Calmes
4/18/2018

Uses Bloomberg.com and expects web pages to be in a specific format
"""

# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup


class BeautifulData:

    # gets data from bloomberg and returns data into a tuple
    @property
    def get_data(self):
        # page to scrape
        quote_pages = ['http://www.bloomberg.com/quote/SPX:IND', 'http://www.bloomberg.com/quote/CCMP:IND',
                       'http://www.bloomberg.com/quote/INDU:IND', 'http://www.bloomberg.com/quote/NYA:IND',
                       'http://www.bloomberg.com/quote/IBEX:IND']
        data = []

        for pg in quote_pages:
            # open page
            page = urlopen(pg)
            # parse the html using beautiful soap and store in variable `soup`
            soup = BeautifulSoup(page, 'html.parser')

            # Take out the <div> of name and get its value
            name_box = soup.find('h1', attrs={'class': 'name'})
            name = name_box.text.strip()  # strip() is used to remove starting and trailing

            # get the index price
            price_box = soup.find('div', attrs={'class': 'price'})
            price = price_box.text.strip()

            # save the data in tuple
            data.append((name, price))

        return data
