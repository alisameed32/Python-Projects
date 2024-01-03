from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from Constants import *
import time

class InternetSpeedTwitterBot:

    def __init__(self):
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=self.chrome_option)
        self.up = 0
        self.down = 0


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]'
                                           '/div[3]/div[1]/a').click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/'
                                                                'div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]'
                                                                '/div/div[2]/span').text

        self.up = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]'
                                                              '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/'
                                                              'div[2]/span').text


        print(f"Up: {self.up}")
        print(f"Down: {self.down}")


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/?lang=en")
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]'
                                           '/div[1]/div/div[3]/div[5]/a').click()

        time.sleep(10)
        self.email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]'
                                                        '/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        self.email.send_keys(TWITTER_EMAIL)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]'
                                           '/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()

        input("Captacha done? ")
        self.password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                                           '/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]'
                                                           '/div/label/div/div[2]/div[1]/input')
        self.password.send_keys(TWITTER_PWD)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]'
                                           '/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()

        up = float(self.up)
        down = float(self.down)

        if(down<PROMISED_DOWN and up<PROMISED_UP):
            tweet = (f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for "
                     f"{PROMISED_DOWN}down/{PROMISED_UP}up?")
            time.sleep(5)
            self.tweetpost = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
            self.tweetpost.send_keys(tweet)
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div'
                                               '/div[3]/div/div[2]/div[1]/div/div/div/div[2]'
                                               '/div[2]/div[2]/div/div/div/div[3]').click()


        elif(down<PROMISED_DOWN):
            tweet = (f"Hey Internet Provider, why is my internet speed {self.down}down when I pay for "
                     f"{PROMISED_DOWN}down?")
            time.sleep(5)
            self.tweetpost = self.driver.find_element(By.XPATH,
                                                      '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
            self.tweetpost.send_keys(tweet)
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div'
                                               '/div[3]/div/div[2]/div[1]/div/div/div/div[2]'
                                               '/div[2]/div[2]/div/div/div/div[3]').click()
        elif(up<PROMISED_UP):
            tweet = (f"Hey Internet Provider, why is my internet speed {self.up}up when I pay for "
                     f"{PROMISED_DOWN}down/{PROMISED_UP}up?")
            time.sleep(5)
            self.tweetpost = self.driver.find_element(By.XPATH,
                                                      '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
            self.tweetpost.send_keys(tweet)
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div'
                                               '/div[3]/div/div[2]/div[1]/div/div/div/div[2]'
                                               '/div[2]/div[2]/div/div/div/div[3]').click()
        else:
            pass


