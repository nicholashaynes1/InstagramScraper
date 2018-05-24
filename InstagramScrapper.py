from selenium import webdriver
from time import sleep

# Defines the broweser we are using.
driver = webdriver.Chrome('C:/Users/nick/InstaPy/assets/chromedriver')
# Navigate to instagram
driver.get('https://www.instagram.com')

def enterEmail():

	# delays checking the javascript elements of a page so it is fully loaded.
	sleep(.2)

	# Finds the email input field by scraping the js
	emailInput = driver.find_elements_by_xpath("//input[@name='emailOrPhone' and @value='']")[0]

	# clicks the email inputField
	emailInput.click()

	# Sends the desired email to the email text box
	emailInput.send_keys("Nick")
	return;

enterEmail()