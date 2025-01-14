from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import title_is
import time

#initialize the browser setup
driver = webdriver.Chrome()

#Navigate to the URL
driver.get("https://www.saucedemo.com/")

#Attribute and its values
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()
time.sleep(3)


title = driver.title # To fetch the title of the page
current_url = driver.current_url # To fetch the current URL
page_source = driver.page_source # To fetch the content of the currently opened web page

#To save the webpage content in "Webpage_task_11.txt" file
with open(".venv/Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(page_source)

#To print the Output
print("Title of the webpage : ", title)
print("The current URL of the webpage : ", current_url)
print("content of the webpage is printer in Webpage_task_11.txt file")

driver.quit()