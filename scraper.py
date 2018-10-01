#! python 3
# scraper.py - opens multiple github pull-requests in new browser depending on usernames
from selenium import webdriver
# gets us access to our environment_vars (os needed)
from dotenv import load_dotenv
import os
load_dotenv()

handles = os.getenv("HANDLES_LIST") # list of usernames ['Fry', 'Bender']
url = os.getenv("URL") # string containing url "github.com/blah/pulls" to be scraped

# selenium
browser = webdriver.Firefox()
browser.get(url)

def find_user_links(handles_list):

	for user in handles_list:
		# print(browser.find_element_by_css_selector('.muted-link[title="Open pull request created by str(user.replace('"', ''))"]'))
		print(browser.find_element_by_css_selector(f'.muted-link['))


find_user_links(handles)
