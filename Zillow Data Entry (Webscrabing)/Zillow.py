#Author: ALI SAMEED ARBANI

import time
import requests
from bs4 import BeautifulSoup
from CONSTANTS import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Webscrabing_DataEntry:

    def __init__(self):
        page = requests.get(ZILLOW)
        soup = BeautifulSoup(page.text, 'html.parser')
        self.dataEntry(soup)


    def price(self, soup):
        prices = []
        price_element = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
        for i in price_element:
            price = i.getText(strip=True)
            price = price.replace("+/mo", "")
            price = price.replace("/mo", "")
            price = price.replace("+ 1bd", "")
            price = price.replace("+ 1 bd", "")
            prices.append(price)
        return prices



    def address(self, soup):
        addresses = []
        address_element = soup.select(".StyledPropertyCardDataWrapper address")
        for i in address_element:
            address = i.getText(strip=True)
            addresses.append(address)
        return addresses


    def link(self, soup):
        links = []
        all_links = soup.select(".StyledPropertyCardDataWrapper a")
        for i in all_links:
            # link = i.getText()
            link = i['href']
            links.append(link)
        return links


    def dataEntry(self, soup):
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                       options=self.chrome_option)

        self.driver.get(FORM)
        time.sleep(2)

        prices = self.price(soup)
        addresses = self.address(soup)
        links = self.link(soup)

        for i in range(0, 15):
            time.sleep(1)
            address = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div'
                                                         '/div[2]/div/div[1]/div/div[1]/input')
            link = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]'
                                                      '/div/div[1]/div/div[1]/input')
            price = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address.send_keys(addresses[i])
            price.send_keys(prices[i])
            link.send_keys(links[i])

            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]'
                                               '/div/span/span').click()

            time.sleep(2)
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()












