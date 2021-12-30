
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
    # chrome_options.add_argument("--window-size=1920x1080")
    book = str(input("What is the book title ")).replace(' ', '+')
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

    #Get rid of the weird popup
    try:
        dismiss = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/button")
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(dismiss, 5, 5)
        action.click()
        action.perform()
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    except:
        dismiss2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div/button")
        action.move_to_element_with_offset(dismiss2, 5, 5)
        action.click()
        action.perform()
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        pass

    click_shelves = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[1]/div[2]/div[5]/div[7]/div/div[2]/div/a")
    click_shelves.click()
    tags = driver.find_elements(By.XPATH,"//div[@class='shelfStat']")
    dictionary = {}
    print(ourtags.returntags())
    for i in tags:
        if i.text.split()[0] in ourtags.returntags():
            dictionary.update({f"{i.text.split()[0]}": f"{i.text.split()[1]}"})
    # tags_to_users = 
    print(dictionary)
    #randomize_sleep(3, 4)

    # driver.close()

    

web_scraper()