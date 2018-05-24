from selenium import webdriver
from time import sleep

# Defines the broweser we are using.
driver = webdriver.Chrome('C:/Users/nick/InstaPy/assets/chromedriver')

# Navigate to instagram
driver.get('https://www.instagram.com')

# Finds the email input field
emailInput =driver.find_elements_by_xpath("//input[@name='emailOrPhone' and @value='']")[0]
# clicks the email inputField
emailInput.click()