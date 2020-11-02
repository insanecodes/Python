from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# set webdriver path here it may vary
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

website_URL = "https://www.python.org/"
driver.get(website_URL)

# After how many seconds you want to refresh the webpage
# Few website count view if you stay there
# for a particular time
# you have to figure that out
refreshrate = int(5)

# This would keep running until you stop the compiler.
while True:
    time.sleep(refreshrate)
    driver.refresh()
