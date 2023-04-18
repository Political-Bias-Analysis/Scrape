from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from collections import defaultdict
import sys

sys.path.append("/Users/tramla/Desktop/UCI Courses/Senior-Project/Scrape/scrape/")
from ReadWriteFiles.read_write_links import *

def get_websites(bias, all_articles):
    driver = webdriver.Chrome()
    driver.get('https://www.cnn.com/search?q=news&from=0&size=10&page=1&sort=newest&types=all&section=')
    search_bar = driver.find_element(By.CLASS_NAME, "search__input")
    search_bar.clear()
    time.sleep(2)
    search_bar.send_keys(f"election {bias}")
    time.sleep(1)
    driver.find_elements(By.CLASS_NAME, "facet__item__label")[1].click()
    
    articles = defaultdict(list)

    filters = ["section_us", "section_politics", "section_opinion"]
    filters_query = ["us", "politics", "opinion"]
    for elem, query in zip(filters, filters_query):
        driver.find_element(By.CLASS_NAME, "search__dropdown__sections").click()
        time.sleep(2)
        driver.find_element(By.ID, elem).click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "search__button.icon.icon--search").click()
        time.sleep(1)

        from_next, page_next = 0, 1
        query_bias = bias.replace(" ", "+")
        while True:
            results = driver.find_elements(By.CLASS_NAME, "container__link.__link")
            if len(results) == 0:
                break
            for item in results:
                href = item.get_attribute("href")
                if href not in all_articles:
                    all_articles.add(href)
                    date = item.find_element(By.CLASS_NAME, "container__text.__text").find_elements(By.TAG_NAME, 'div')[1].text
                    articles[get_year(date)].append({"link": href, "bias": bias})         
            driver.get(f'https://www.cnn.com/search?q=election+{query_bias}&from={from_next}&size=50&page={page_next}&sort=newest&types=article&section={query}')
            from_next += 50
            page_next += 1
            time.sleep(1)
            
    return articles


def get_year(date):
    return int(date.split(' ')[-1])


if __name__ == "__main__":

    MEDIA_NAME = "CNN"
    MAIN_BIAS, EXISTS = "socioeconomic", True
    biases = ["socioeconomic", "poverty line", "working class", "middle class", "medicare"]
    cur_bias = biases[4]

    all_links = get_all_links(MEDIA_NAME)

    dict_links = get_websites(cur_bias, all_links)
    write_all_links(MEDIA_NAME, all_links)

    if not EXISTS:
        write_links_by_year(dict_links, MAIN_BIAS, MEDIA_NAME)
    else:
        write_more_links_by_year(dict_links, MAIN_BIAS, cur_bias, MEDIA_NAME)
