
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.remote.webdriver import WebElement
import random
from selenium.webdriver.common.action_chains import ActionChains
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from .models import Article

class Scrapper(object):
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-gpu') 
        self.options.add_argument('--disable-dev-shm-usage')
        self.data = []


    def run(self):
        driver = webdriver.Chrome(options=self.options, executable_path='/usr/local/bin/chromedriver')
        driver.get("https://www.bbc.com")
        driver.implicitly_wait(10)
        executor = ThreadPoolExecutor(max_workers=10)

        try:
            
            articles = driver.find_elements(by=By.XPATH, value='//a[@class="media__link"]')
            articles_url = []
            for article in articles:
                articles_url.append(article.get_attribute("href"))

            print(f'Articles Count {len(articles_url)}')
            print(f'Articles {articles_url}')
            it = executor.map(Scrapper().get_article, tuple(articles_url), chunksize=1)
            for data in it:
                print(f'Received Data: URL: {data["url"]} Title: {data["title"]} ')
                a  = Article(url=data['url'], title=data['title'], body=data['body'])
                a.save()


        except Exception as e:
            print(f'Exception Occured : {e}')

    def get_article(self, url):
        print(f'Executing get_article for {url}')
        driver = webdriver.Chrome(options=self.options, executable_path='/usr/bin/chromedriver')
        driver.get(url)
        driver.implicitly_wait(10)
        
        try:
            data = {}
            data['url']= url
            title = driver.find_element(by=By.TAG_NAME, value="h1")
            data['title']= title.text

            body = ""
            ps = driver.find_elements(by=By.TAG_NAME, value="p")
            for p in ps:
                body += p.text
            data['body'] = body
            #print(data)
            return data

        except Exception as e:
            print(f'Exception Occured : {e} for {url}')
            return {}

    

def main():
    b = Scrapper()
    b.run()
    

if __name__ == "__main__":
    main()