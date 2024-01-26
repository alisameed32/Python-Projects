#Author: ALI SAMEED ARBANI

import time
from constants import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException


class InstaFollower:

    def __init__(self):
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=self.chrome_option)


    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)
        self.emailLabel = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]'
                                                             '/section/main/div/div/div[1]/div[2]/form/div/div[1]'
                                                             '/div/label/input')
        self.pwdLabel = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]"
                                                           "/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/"
                                                           "label/input")
        self.emailLabel.send_keys(INSTAGRAM_EMAIL)
        self.pwdLabel.send_keys(INSTAGRAM_PWD)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div'
                                           '/div[1]/div[2]/form/div/div[3]').click()
        time.sleep(8)
        self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]").click()


        pass


    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNTS}")
        time.sleep(5)
        #My Intial Task was to follow the followers but since instagram has 666M followers so I decided to
        # follow their following and follow one more especial person which is @Ali Sameed Arbani
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]'
                                             '/section/main/div/header/section/ul/li[3]').click()

        time.sleep(5.2)
        # The xpath of the modal that shows the followers will change over time. Update yours accordingly.
        scrollable_popup = ("/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]")
        scrol = self.driver.find_element(by=By.XPATH, value=scrollable_popup)
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrol)
            time.sleep(2)


    def follow(self):
        #Here I learned how css selector works even though I take the code of my instructor from this part
        # but I learned how its worked

        buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
