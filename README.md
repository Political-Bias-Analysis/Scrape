# Senior-Project

# Requirements:

1. Install BeautifulSoup4
2. Install Selenium

## A. How to Scrape Articles From CNN

### I. Acquire article links using Selenium

1. Run ```cd scrape/CNN```
2. Open the interact_cnn.py file in your text editor
3. Scroll down to ```if __name__ == "__main__":``` block 
4. Place the biased terms that you would like to scape (should all relate to one main term) in the ```biases``` variable
5. Place the main biased term in the ```MAIN_BIAS``` variable
6. If you are scraping the links of the first term, toggle ```EXISTS``` to False, else leave it as True
7. Change the index of the current bias term after each iteration (should start at 0)
8. Run the script using the command: ```python3 interact_cnn.py```

### II. Scrape Articles Using Acquired Links

1. Open the scrape_cnn.py file in your text editor
2. Scroll down to ```if __name__ == "__main__":``` block
3. Place the biased term you would like to scrape in the ```MAIN_BIAS``` variable
4. Place the year you would like to scrape in the ```YEAR``` variable
5. Run the script using the command: ```python3 scrape_cnn.py```

## B. How to scrape Articles From FoxNews

### I. Acquire article links using Selenium

1. cd into scrape/FoxNews
2. Open the interact_fox.py file in your text editor
3. Scroll down to ```if __name__ == "__main__":``` block 
4. Place the biased terms that you would like to scape (should all relate to one main term) in the ```biases``` variable
5. Place the year you would like to scrape in the ```year``` variable
6. Place the current term you would like to scrape by changing the index of ```bias``` term
7. If you are scraping the links of the first term, toggle ```EXISTS``` to False, else leave it as True
8. Run the script using the command: ```python3 interact_fox.py```

### II. Scrape Articles Using Acquired Links

1. Open the scrape_fox.py file in your text editor
2. Scroll down to ```if __name__ == "__main__":``` block
3. Place the biased term you would like to scrape in the ```MAIN_BIAS``` variable
4. Place the year you would like to scrape in the ```YEAR``` variable
5. Run the script using the command: ```python3 scrape_fox.py```
