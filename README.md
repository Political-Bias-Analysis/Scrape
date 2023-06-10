# Senior-Project

# How to scrape articles from CNN, Fox News, NPR, CBS

## Requirements:

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
4. Place the main biased term in the ```MAIN_BIAS``` variable
5. Place the biased terms that you would like to scape (should all relate to one main term) in the ```biases``` variable
6. Place the year you would like to scrape in the ```year``` variable
7. Place the current term you would like to scrape by changing the index of ```bias``` term
8. If you are scraping the links of the first term, toggle ```EXISTS``` to False, else leave it as True
9. Run the script using the command: ```python3 interact_fox.py```

### II. Scrape Articles Using Acquired Links

1. Open the scrape_fox.py file in your text editor
2. Scroll down to ```if __name__ == "__main__":``` block
3. Place the biased term you would like to scrape in the ```MAIN_BIAS``` variable
4. Place the year you would like to scrape in the ```YEAR``` variable
5. Run the script using the command: ```python3 scrape_fox.py```

## C. How to scrape Articles From NPR

### I. Acquire article links using Selenium

1. cd into scrape/NPR
2. Open the interact_npr.py file in your text editor
3. Scroll down to ```if __name__ == "__main__":``` block 
4. Place the main biased term in the ```MAIN_BIAS``` variable
5. Place the biased terms that you would like to scape (should all relate to one main term) in the ```biases``` variable
6. Place the current term you would like to scrape by changing the index of ```cur_bias``` variable
7. If you are scraping the links of the first term, toggle ```EXISTS``` to False, else leave it as True
8. Run the script using the command: ```python3 interact_npr.py```

### II. Scrape Articles Using Acquired Links

1. Open the scrape_npr.py file in your text editor
2. Scroll down to ```if __name__ == "__main__":``` block
3. Place the biased term you would like to scrape in the ```MAIN_BIAS``` variable
4. Place the year you would like to scrape in the ```YEAR``` variable
5. Run the script using the command: ```python3 scrape_npr.py```

## D. How to scrape Articles From CBS

### I. Acquire article links using Selenium

1. cd into scrape/CBS
2. Open the interact_cbs.py file in your text editor
3. Scroll down to ```if __name__ == "__main__":``` block 
4. Place the main biased term in the ```MAIN_BIAS``` variable
5. Place the biased terms that you would like to scape (should all relate to one main term) in the ```biases``` variable
6. Place the current term you would like to scrape by changing the index of ```cur_bias``` variable
7. If you are scraping the links of the first term, toggle ```EXISTS``` to False, else leave it as True
8. Run the script using the command: ```python3 interact_cbs.py```

### II. Scrape Articles Using Acquired Links

1. Open the scrape_cbs.py file in your text editor
2. Scroll down to ```if __name__ == "__main__":``` block
3. Place the biased term you would like to scrape in the ```MAIN_BIAS``` variable
4. Place the year you would like to scrape in the ```YEAR``` variable
5. Run the script using the command: ```python3 scrape_cbs.py```

# How to insert article data into database

## Required softwares and libraries

1. PostgreSQL: https://www.postgresql.org/
2. psycopg2: https://pypi.org/project/psycopg2/

## Create Articles database and schemas

1. Open the Scrape/SQL/create_tables_articles.sql in a text editor
2. Create the Articles database in your PostgreSQL server using the provided create database command
3. Create the required schemas: biases, all_articles, and media_source using the provided commands

## Insert articles data into Articles database

1. Input the year and source of the file that you would like to insert data into the database
2. Input all the sub-biased terms that you used to scrape articles from
3. Edit the path name that store the intended file in the ```path``` variable
4. In the terminal, run ```python3 insert_data.py``` to start inserting data into the database