from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from collections import defaultdict
import sys

sys.path.append("/Users/tramla/Desktop/UCI Courses/Senior-Project/scrape/")
from ReadWriteFiles.read_write_links import *

def get_websites(bias, all_links):
    driver = webdriver.Chrome()
    driver.get('https://www.npr.org/search/')
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "ais-SearchBox-input").send_keys(f"election {bias}")
    time.sleep(1)

    articles = defaultdict(list)
    count = 0
    while count < 500:
        results = driver.find_elements(By.CLASS_NAME, "item")
        for item in results:
            href = item.find_element(By.CLASS_NAME, "title").find_element(By.TAG_NAME, 'a').get_attribute("href")
            if check_valid(href) and href not in all_links:
                all_links.add(href)
                print(href)
                date = item.find_element(By.CLASS_NAME, "date").text
                articles[get_year(date)].append({"links": href, "bias": bias})
                count += 1
        next_pg = driver.find_elements(By.CLASS_NAME, "ais-InfiniteHits-loadMore")
        if len(next_pg):
            next_pg[0].click()
            time.sleep(1)
        else:
            break
            
    return articles

def get_year(date):
    return int(date.split(" ")[-2])


def check_valid(href):
    
    if "templates/story" in href:
        return False
    if "npr.org/series" in href:
        return False
    return True


if __name__ == "__main__":
    
    MEDIA_NAME = "NPR"
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