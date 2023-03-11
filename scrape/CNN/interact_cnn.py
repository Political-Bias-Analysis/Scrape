from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from collections import defaultdict


def get_websites(query, all_articles):
    driver = webdriver.Chrome()
    driver.get('https://www.cnn.com/search?q=news&from=0&size=10&page=1&sort=newest&types=all&section=')
    search_bar = driver.find_element(By.CLASS_NAME, "search__input")
    search_bar.clear()
    time.sleep(2)
    search_bar.send_keys(query)
    time.sleep(1)

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

    return articles, all_articles


def get_year(date):
    return int(date.split(' ')[-1])


def write_all_links(links):

    with open("../../data/links/CNN/all_links.json", "w") as f:
        in_json = json.dumps(list(links), indent=4)
        f.write(in_json)


def get_all_links():
    with open("../../data/links/CNN/all_links.json") as f:
        return set(json.loads(f.read()))


def write_links_by_year(dict_links, main_bias):

    for year, links in dict_links.items():
        PATH = f"../../data/links/CNN/{main_bias}_{str(year)}.json"
        with open(PATH, "w") as f:
            in_json = json.dumps(prepare_format(links, main_bias, year), indent=4)
            f.write(in_json)


def prepare_format(links, main_bias, year):
    return {"Biases": [main_bias], "Links": links, "Year": year}


def write_more_links_by_year(dict_links, main_bias, new_bias):

    for year, links in dict_links.items():
        cur = None
        PATH = f"../../data/links/CNN/{main_bias}_{str(year)}.json"
        with open(PATH, 'r') as f:
            cur = json.loads(f.read())

        cur["Biases"].append(new_bias)
        cur["Links"] += links

        with open(PATH, "w") as f:
            f.write(json.dumps(cur, indent=4))


if __name__ == "__main__":

    MAIN_BIAS, EXISTS = "immigration", True
    biases = ["immigration", "undocumented", "refugees", "asylum seekers", "nationalism", "border", "Dreamers", "xenophobia"]
    cur_bias = biases[7]

    all_links = get_all_links()

    dict_links, new_links = get_websites(f"election {cur_bias}", all_links)
    write_all_links(new_links)

    if not EXISTS:
        write_links_by_year(dict_links, MAIN_BIAS)
    else:
        write_more_links_by_year(dict_links, MAIN_BIAS, cur_bias)
