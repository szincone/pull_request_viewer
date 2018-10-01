#! python 3
# scraper.py - opens multiple github pull-requests in new browser
# depending on usernames
from selenium import webdriver
# gets us access to our environment_vars (os needed)
from dotenv import load_dotenv
import os
load_dotenv()

# string of usernames "Fry Bender Leela" turned into list
handles = os.getenv("HANDLES_LIST").split(" ")
# string containing url "github.com/blah/pulls" to be scraped
url = os.getenv("URL")

# selenium
browser = webdriver.Firefox()
browser.get(url)


def find_user_links(handles_list):
    ###
    for user in handles_list:
        print(browser.find_element_by_link_text(user))


find_user_links(handles)
