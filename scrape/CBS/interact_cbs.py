from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from collections import defaultdict
import sys

sys.path.append("/Users/tramla/Desktop/UCI Courses/Senior-Project/scrape/")
from ReadWriteFiles.read_write_links import *

CURRENT_YEAR = 2023

def get_websites(bias, all_articles):

    driver = webdriver.Chrome()
    driver.get('https://www.cbsnews.com/#search-form:')
    time.sleep(2)
    
    driver.find_element(By.CLASS_NAME, "site-nav__item-anchor.site-nav__item-anchor--level-1.site-nav__item--search-link").click()
    time.sleep(2)
    
    driver.find_element(By.CLASS_NAME, "search-field").send_keys(f"election {bias}")
    time.sleep(1)
    
    articles = defaultdict(list)

    page = 1
    while True:
        try:
            next_pg = driver.find_element(By.XPATH, f'//*[@id="component--search-from"]/div/div/div/div[2]/div[2]/div/section/div[2]/a[{page}]')
            next_pg.click()
            page += 1
            time.sleep(2)
        except:
            print(page)
            break

    table = driver.find_element(By.CLASS_NAME, "component__item-wrapper")
    results = table.find_elements(By.CLASS_NAME, "item.item--type-article")
    
    for item in results:
        href = item.find_element(By.CLASS_NAME, "item__anchor").get_attribute("href")
        if href not in all_articles:
            date = item.find_element(By.CLASS_NAME, "item__date").text
            all_articles.add(href)
            articles[get_year(date)].append({"link": href, "bias": bias})
            
    return articles
                
                    
def get_year(date):
    if date == "":
        return 0
    if "AGO" in date:
        return CURRENT_YEAR
    return int(date.split(" ")[-1])


if __name__ == "__main__":
    MEDIA_NAME = "CBS"
    MAIN_BIAS, EXISTS = "immigration", False
    biases = ["immigration", "undocumented", "refugees", "asylum seekers", "nationalism", "border", "Dreamers", "xenophobia"]
    
    cur_bias = biases[0]
    
    all_links = get_all_links(MEDIA_NAME)
    
    dict_links = get_websites(cur_bias, all_links)
    write_all_links(MEDIA_NAME, all_links)

    if not EXISTS:
        write_links_by_year(dict_links, MAIN_BIAS, MEDIA_NAME)
    else:
        write_more_links_by_year(dict_links, MAIN_BIAS, cur_bias, MEDIA_NAME)
