from selenium.common.exceptions import TimeoutException, WebDriverException
from mod_string_manipulation import *
from mod_selenium import *

def do_scraping(num_pages_to_search, file):
    counter = 1

    while counter <= num_pages_to_search:
        try:
            wait_until_visible("//li[@class='arrow__right']/a")

            with open(file, "a") as f:
                table = find_element("//table[@class='proxy__t']")

                for row in table.find_elements_by_xpath(".//tr"):
                    line = [td.text.strip() for td in row.find_elements_by_xpath(".//td")]
                    line = remove_special_char_and_compress(line)
                    if line != '':
                        print(line)
                        f.write(line + "\n")

            counter = navigate_to_the_next_page(counter)

        except (TimeoutException, WebDriverException) as e:
            print("Last page reached")
            break

    quit_selenium_driver()

