# import all nessecery modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

# Its Open Instagram in Crome browser
driver.get("https://www.instagram.com/")
sleep(4)

# Enters your username in username's section
driver.find_element_by_xpath(
    "//input[@name=\"username\"]").send_keys("nex_roxx")
# Enters your password in password's section
driver.find_element_by_xpath(
    "//input[@name=\"password\"]").send_keys("Passcrack40")
# Clicks Login Button
driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
sleep(3)

# Clicks on Not Now button on save login info section
driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
sleep(3)
# Clicks on Not Now button on Turns On Notification section
driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()


# loops for how many followers you wanty to follow (3*5=15)
for i in range(3):
    for i in range(5):
        driver.find_element_by_xpath('//button[text()="Follow"]').click()
        sleep(2)
    driver.refresh()
    sleep(3)

driver.close()
