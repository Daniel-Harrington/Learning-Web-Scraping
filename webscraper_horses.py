from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd

def launchBrowser():
    url = 'https://woodbine.com/statistics'
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    driver.get(url)
    x = 0
    jockey = []
    while(x < 4):
        print('got here')
        tableShit = driver.find_elements_by_tag_name('td')
        for tableShit in tableShit:
            jockey.append(tableShit.text)
        nextPage = driver.find_element_by_xpath('//*[@id="grid"]/div[3]/a[3]')
        nextPage.click()
        x+=1
    jockey_list = []
    n = 8
    jockey_list = [jockey[i:i + n] for i in range(0, len(jockey), n)]
    return jockey_list

df = pd.DataFrame(launchBrowser(),columns= ['Name', 'Date Updated', 'Starts', 'Earnings', 'Firsts', 'Seconds', 'Thirds', 'Fourths'])
df.to_csv(path_or_buf=r'C:/Users/novus/Documents/Web Projects/JockeyData.csv')
