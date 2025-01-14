from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import Service from the right module

# Specify the path to the ChromeDriver
service_obj = Service("C:/Users/vidhy/PycharmProjects/driver/chromedriver.exe")

# Initialize the WebDriver with the service object
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.google.com")

print(driver.title)