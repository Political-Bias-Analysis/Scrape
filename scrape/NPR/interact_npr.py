from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from collections import defaultdict
import sys

sys.path.insert(0, "/Users/tramla/Desktop/UCI Courses/Senior-Project/scrape/ReadWriteFiles")
import read_write_links


def get_websites(query, all_links):
    driver = webdriver.Chrome()
    driver.get('https://www.npr.org/search/')
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "ais-SearchBox-input").send_keys(query)
    time.sleep(1)

    articles = defaultdict(list)
    
    while True:
        results = driver.find_elements(By.CLASS_NAME, "item")
        for item in results:
            href = item.find_element(By.CLASS_NAME, "title").find_element(By.TAG_NAME, 'a').get_attribute("href")
            all_links.add(href)
            print(href)
            date = item.find_element(By.CLASS_NAME, "date").text
            articles[get_year(date)].append(href)
        next_pg = driver.find_elements(By.CLASS_NAME, "ais-InfiniteHits-loadMore")
        if len(next_pg):
            next_pg[0].click()
            time.sleep(1)
        else:
            break
            
    return articles

def get_year(date):
    return int(date.split(" ")[-2])
    

if __name__ == "__main__":
    
    MEDIA_NAME = "NPR"
    MAIN_BIAS, EXISTS = "immigration", False
    biases = ["immigration", "undocumented", "refugees", "asylum seekers", "nationalism", "border", "Dreamers", "xenophobia"]
    
    cur_bias = biases[0]
    
    all_links = read_write_links.get_all_links(MEDIA_NAME)
    dict_links = get_websites(f"president election {cur_bias}", all_links)
    
    read_write_links.write_all_links(MEDIA_NAME, all_links)

    if not EXISTS:
        read_write_links.write_links_by_year(dict_links, MAIN_BIAS, MEDIA_NAME)
    else:
        read_write_links.write_more_links_by_year(dict_links, MAIN_BIAS, cur_bias, MEDIA_NAME)