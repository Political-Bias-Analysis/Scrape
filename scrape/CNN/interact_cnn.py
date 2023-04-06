from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from collections import defaultdict
import sys

sys.path.insert(0, "/Users/tramla/Desktop/UCI Courses/Senior-Project/scrape/ReadWriteFiles")
import read_write_links

def get_websites(query, all_articles):
    driver = webdriver.Chrome()
    driver.get('https://www.cnn.com/search?q=news&from=0&size=10&page=1&sort=newest&types=all&section=')
    search_bar = driver.find_element(By.CLASS_NAME, "search__input")
    search_bar.clear()
    time.sleep(2)
    search_bar.send_keys(query)
    time.sleep(1)
    driver.find_elements(By.CLASS_NAME, "facet__item__label")[1].click()

    articles = defaultdict(list)

    filters = ["section_us", "section_politics", "section_opinion"]
    for elem in filters:
        driver.find_element(By.CLASS_NAME, "search__dropdown__sections").click()
        time.sleep(2)
        driver.find_element(By.ID, elem).click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "search__button.icon.icon--search").click()
        time.sleep(1)

        while True:
            results = driver.find_elements(By.CLASS_NAME, "container__link.__link")
            for item in results:
                href = item.get_attribute("href")
                if href not in all_articles:
                    all_articles.add(href)
                    date = item.find_element(By.CLASS_NAME, "container__text.__text").find_elements(By.TAG_NAME, 'div')[1].text
                    articles[get_year(date)].append(href)

            next_pg = driver.find_elements(By.CLASS_NAME, "pagination-arrow.pagination-arrow-right.search__pagination-link.text-active")
            if len(next_pg):
                next_pg[0].click()
                time.sleep(1)
            else: 
                print(articles)
                break

    return articles


def get_year(date):
    return int(date.split(' ')[-1])


def prepare_format(links, main_bias, year):
    return {"Biases": [main_bias], "Links": links, "Year": year}


if __name__ == "__main__":

    MEDIA_NAME = "CNN"
    MAIN_BIAS, EXISTS = "immigration", True
    biases = ["immigration", "undocumented", "refugees", "asylum seekers", "nationalism", "border", "Dreamers", "xenophobia"]
    cur_bias = biases[7]

    all_links = read_write_links.get_all_links(MEDIA_NAME)

    dict_links = get_websites(f"election {cur_bias}", all_links)
    read_write_links.write_all_links(MEDIA_NAME, all_links)

    if not EXISTS:
        read_write_links.write_links_by_year(dict_links, MAIN_BIAS, MEDIA_NAME)
    else:
        read_write_links.write_more_links_by_year(dict_links, MAIN_BIAS, cur_bias, MEDIA_NAME)
