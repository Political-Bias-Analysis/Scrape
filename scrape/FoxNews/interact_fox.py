from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import sys

sys.path.append("/Users/tramla/Desktop/UCI Courses/Senior-Project/scrape/")
from ReadWriteFiles.read_write_links import *

def access_websites(bias, dates, all_links):
    driver = webdriver.Chrome()
    driver.get('https://www.foxnews.com/search-results/search?q=election')

    search_form = driver.find_element(By.CLASS_NAME, "search-form")
    search_bar = search_form.find_element(By.TAG_NAME, "input")
    search_bar.clear()

    search_bar.send_keys(f"{dates[2]} election {bias}")
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "filter.content").find_element(By.CLASS_NAME, "select").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'option').find_element(By.TAG_NAME, "li").click()
    time.sleep(1)

    months = driver.find_elements(By.CLASS_NAME, "sub.month")
    
    months[0].find_element(By.CLASS_NAME, "select").click()
    months[0].find_element(By.ID, dates[0]).click()
    
    months[1].find_element(By.CLASS_NAME, "select").click()
    months[1].find_element(By.ID, dates[3]).click()

    #---
    days = driver.find_elements(By.CLASS_NAME, "sub.day")

    days[0].find_element(By.CLASS_NAME, "select").click()
    days[0].find_element(By.ID, dates[1]).click()
    
    days[1].find_element(By.CLASS_NAME, "select").click()
    days[1].find_element(By.ID, dates[4]).click()

    #---

    years = driver.find_elements(By.CLASS_NAME, "sub.year")

    years[0].find_element(By.CLASS_NAME, "select").click()
    years[0].find_element(By.ID, dates[2]).click()
    
    years[1].find_element(By.CLASS_NAME, "select").click()
    years[1].find_element(By.ID, dates[5]).click()
    time.sleep(2)

    search_form.find_element(By.CLASS_NAME, 'button').click()
    time.sleep(2)

    #-- load all 100 articles
    try:
        for i in range(9):
            print(i)
            driver.find_element(By.CLASS_NAME, "button.load-more").click()
            time.sleep(3)
    except:
        print("No more links allowed")

    links = []
    
    articles = driver.find_elements(By.CLASS_NAME, 'm')
    time.sleep(2)
    for elem in articles:
        link = elem.find_element(By.TAG_NAME, 'a').get_attribute('href')
        if check_us_news(link) and link not in all_links: 
            links.append({"link": link, "bias": bias})
            all_links.add(link)
    
    return links


def check_us_news(url):
    url_clean = url.strip('https://').split("/")
    if url_clean[1] in ['world', 'entertainment', 'sports']:
        return False 
    return True


def write_links_new_bias(links_info, bias, year):
    PATH = '../../data/links/FOX/' + bias + '_' + str(year) + '.json'
    with open(PATH, 'w+') as f:
        output = json.dumps(links_info, indent=4)
        f.write(output)



def write_links_exist_bias(main_bias, bias, year, links):
    PATH = '../../data/links/FOX/' + main_bias + '_' + str(year) + '.json'
    
    cur = None
    with open(PATH, 'r') as f:
        cur = json.loads(f.read())

    cur["Biases"].append(bias)
    cur["Links"] += links
    write_links_new_bias(cur, cur['Biases'][0], year)

    
def compose_dict(links, bias, year):
    new_links = dict()
    new_links["Biases"], new_links["Links"], new_links["Year"] = [bias], links, year
    return new_links


if __name__ == "__main__":

    MEDIA_NAME = "FOX"
    ## run this: if new bias, change MAIN_BIAS and EXISTS = false, else only change bias and keep EXISTS = True
    MAIN_BIAS, EXISTS = "immigration", True
    biases = ["immigration", "undocumented", "refugees", "asylum seekers", "nationalism", "border", "Dreamers", "xenophobia"]
    year, bias = 2020, biases[1]
    
    all_links = get_all_links(MEDIA_NAME)
    
    links = access_websites(bias, ["05", "01", year, "11", "09", year], all_links)
    write_all_links(MEDIA_NAME, all_links)
    
    if not EXISTS:
        dict_info = compose_dict(links, bias, year)
        write_links_new_bias(dict_info, bias, year)
    else:
        write_links_exist_bias(MAIN_BIAS, bias, year, links)
