from mode_scrape import *
from mod_selenium import *
from mod_files import *

def main():
    file = './proxy.csv'
    url = 'https://hidemyna.me/en/proxy-list/'
    num_pages_to_search = 2

    clear_csv_file(file)
    navigate_to_page(url)
    do_scraping(num_pages_to_search, file)

if __name__ == '__main__':
    main()
