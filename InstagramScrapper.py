from selenium import webdriver
from time import sleep
import string
import random

# Defines the broweser we are using.
driver = webdriver.Chrome('C:/Users/nick/InstaPy/assets/chromedriver')
# Navigate to instagram
driver.get('https://www.instagram.com')

def main():
	enterEmail()
	return;


# The function that enters the create user info
def enterEmail():

	# delays checking the javascript elements of a page so it is fully loaded.
	sleep(1.5)

	# Finds the email input field by scraping the js
	emailInput = driver.find_elements_by_xpath("//input[@name='emailOrPhone' and @value='']")[0]

	# clicks the email inputField
	emailInput.click() 

	# Sends the desired email to the email text box
	emailInput.send_keys(generateEmail())

	# Finds the username field
	usernameInput = driver.find_elements_by_xpath("//input[@name='username' and @value='']")[0]

	# Clicks the username field
	usernameInput.click()

	# Enters a randomized username
	usernameInput.send_keys(generateUsername())

	return;

# The function that generates a random email 
def generateEmail():
	randomEmail =''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)])
	return randomEmail + "@gmail.com";

# The function that generates a random username
def generateUsername():
	randomUsername = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)])
	return randomUsername;





main()
