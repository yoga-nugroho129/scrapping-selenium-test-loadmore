from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

browser_options = Options()
browser_options.add_argument('--headless')

url = "https://www.reuters.com/search/news?blob=soybean&sortBy=date&dateRange=all"
driver = webdriver.Chrome('/home/yoga_nugroho129/chromedriver')
driver.get(url)
html = driver.page_source.encode('utf-8')
page_num = 0
load_more_btn = driver.find_element_by_css_selector('.search-result-more-txt')

while load_more_btn:
    load_more_btn.click()
    page_num += 1
    print("getting page number "+str(page_num))
    time.sleep(1)

html = driver.page_source.encode('utf-8')

driver.close()

# print(html)