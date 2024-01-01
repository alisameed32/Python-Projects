from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random


month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
text = ('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s '
        'standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to '
        'make a type specimen book. It has survived not only five centuries, but also the leap into electronic '
        'typesetting, remaining essentially unchanged.')



chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_option)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3779197130&f_AL=true&geoId=103644278&keywords=Python%20developer&location=United%20States&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")


# Automatic Login

driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]").click() # To get into log form
time.sleep(5)
email = driver.find_element(By.XPATH, '//*[@id="username"]') #for getting address of the email field
password = driver.find_element(By.XPATH, '//*[@id="password"]') #for getting address of the password field
email.send_keys("Gmail@gmail.com") #for filling info the email field
password.send_keys("Password") #for filling info the password field
driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click() # To get into log form
#input("Press Enter when you have solved the Captcha: ") # Tackling Capacha
time.sleep(4)

# For easy apply
driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div').click()

# entering num
number = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3779197130-106730010-phoneNumber-nationalNumber"]')
number.send_keys("123456789")

# buttton
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
submit_button.click()

#clicking button
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]').click()

#Entering Data
dumpytext = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3779197130-106730226-text"]')
dumpytext.send_keys("Senior Developer")

dumpytext = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3779197130-106730306-text"]')
dumpytext.send_keys("Micrsoft")

driver.find_element(By.XPATH, '//*[@id="checkbox-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3779197130-106730386-dateRange-present"]/div/label').click()

dropdown = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/div[1]/div/div[1]/div[3]/div[2]/div/div[1]/fieldset[1]/div/span[1]/select")
dropdown.send_keys(random.choice(month))
dropdown = driver.find_element(By.XPATH, '//*[@id="date-range-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3779197130-106730386-dateRange-range-start-date-year-select"]')
dropdown.send_keys(random.choice(years))


dumpytext = driver.find_element(By.XPATH, '//*[@id="single-typeahead-entity-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3779197130-106730466-city-WORK-LOCATION-CITY-1"]')
dumpytext.send_keys("New York, United States")
dumpytext = driver.find_element(By.XPATH, '//*[@id="multiline-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3779197130-106730714-text"]')
dumpytext.send_keys(text)

#buttons
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/div[1]/div/div[2]/button[2]').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]').click()

