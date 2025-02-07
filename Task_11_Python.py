from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DragAndDropAutomation:
    #Class to automate drag-and-drop operation using Selenium

    def __init__(self):
        #Initialize WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Assign driver to self
        self.driver.maximize_window()

    def open_website(self, url):
        """Open the specified website"""
        self.driver.get(url)

    def perform_drag_and_drop(self):
        #Perform the drag-and-drop operation
        self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, "iframe"))  # Switch to iframe
        source = self.driver.find_element(By.ID, "draggable")  # White box
        target = self.driver.find_element(By.ID, "droppable")  # Yellow box
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()

    def close_browser(self):
        #Close the browser
        self.driver.quit()

if __name__ == "__main__":
    url = "https://jqueryui.com/droppable/"
    automation = DragAndDropAutomation()
    automation.open_website(url)
    automation.perform_drag_and_drop()
    automation.close_browser()
