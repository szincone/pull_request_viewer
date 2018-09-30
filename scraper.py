#! python 3
# scraper.py - opens multiple github pull-requests in new browser depending on usernames
from selenium import webdriver
# gets us access to our environment_vars (os needed)
from dotenv import load_dotenv
import os
load_dotenv()

handles = os.getenv("HANDLES_LIST")
url = os.getenv("URL")

browser = webdriver.Firefox()
browser.get(url)

def find_user_links(handles_list):

	for user in handles_list:
		# print(browser.find_element_by_css_selector('.muted-link[title="Open pull request created by str(user.replace('"', ''))"]'))
		print(browser.find_element_by_css_selector(".muted-link"))


find_user_links(handles)

# assign global variable for each user in handlers array
# for user in handles:
# 	i = 0
# 	globals()[user] = handlers[i]
# 	i += 1;