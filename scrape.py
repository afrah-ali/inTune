
from selenium import webdriver
import random
import os
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import ourtags

def web_scraper():
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--window-size=1920x1080")W
    book = str(input("What is the book title? ")).replace(' ', '+')
    global driver
    driver = webdriver.Chrome('./chromedriver.exe') 
    driver.get(f'https://www.goodreads.com/search?utf8=%E2%9C%93&query={book}')
    while(True):
        try:
            click_first = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]/a/span")
            click_first.click()
        except:
            print("Did not find shelves, restart")
        else:
            break
    sleep(3)

    url_index = driver.current_url.rfind('/')
    book_id = driver.current_url[url_index + 1:]
    driver.get(f'https://www.goodreads.com/book/shelves/{book_id}')
    tags = driver.find_elements(By.XPATH,"//div[@class='shelfStat']")
    dictionary = {}
    for i in tags:
        if i.text.split()[0] in ourtags.returntags():
            dictionary.update({f"{i.text.split()[0]}": f"{i.text.split()[1]}"})
    # tags_to_users = 
    print(dictionary)
    #randomize_sleep(3, 4)

    # driver.close()

    

web_scraper()