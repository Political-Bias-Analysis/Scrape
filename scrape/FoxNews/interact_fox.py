from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def access_search_bar():
    driver = webdriver.Chrome()
    driver.get('https://www.foxnews.com/search-results/search?q=election')

    search_form = driver.find_element(By.CLASS_NAME, "search-form")
    search_bar = search_form.find_element(By.TAG_NAME, "input")
    search_bar.clear()
    time.sleep(2)
    search_bar.send_keys("2016 president election")
    time.sleep(2)


    dates = ["05", "01", "2016", "11", "09", "2016"]

    months = driver.find_elements(By.CLASS_NAME, "sub.month")
    
    time.sleep(2)
    months[0].find_element(By.CLASS_NAME, "select").click()
    time.sleep(2)
    months[0].find_element(By.ID, dates[0]).click()
    
    time.sleep(2)
    months[1].find_element(By.CLASS_NAME, "select").click()
    time.sleep(2)
    months[1].find_element(By.ID, dates[3]).click()
    time.sleep(2)

#---
    days = driver.find_elements(By.CLASS_NAME, "sub.day")

    time.sleep(2)
    days[0].find_element(By.CLASS_NAME, "select").click()
    time.sleep(2)
    days[0].find_element(By.ID, dates[1]).click()
    
    time.sleep(2)
    days[1].find_element(By.CLASS_NAME, "select").click()
    time.sleep(2)
    days[1].find_element(By.ID, dates[4]).click()
    time.sleep(2)

#---

    years = driver.find_elements(By.CLASS_NAME, "sub.year")

    time.sleep(2)
    years[0].find_element(By.CLASS_NAME, "select").click()
    time.sleep(2)
    years[0].find_element(By.ID, dates[2]).click()
    
    time.sleep(2)
    years[1].find_element(By.CLASS_NAME, "select").click()
    time.sleep(2)
    years[1].find_element(By.ID, dates[5]).click()
    time.sleep(2)

    search_form.find_element(By.CLASS_NAME, 'button').click()
    time.sleep(2)

if __name__ == "__main__":
    access_search_bar()
