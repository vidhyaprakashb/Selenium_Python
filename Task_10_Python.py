from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By



class InstagramScraper:
    def __init__(self):
        # Initialize the WebDriver
        self.driver = self.initialize_driver()

    def initialize_driver(self):
        """Initialize the Selenium WebDriver."""
        driver = webdriver.Chrome()
        return driver

    def close_popup(self):
        """Close the Instagram login popup if it appears."""
        try:
            popup_close_xpath = "//div[contains(@class,'_abch _abck x1vjfegm _abcm')]//div[contains(@class,'x6s0dn4 x78zum5 xdt5ytf xl56j7k')]"
            close_button = self.driver.find_element(By.XPATH, popup_close_xpath)
            self.driver.execute_script("arguments[0].click();", close_button)  # Force click using JavaScript
        except NoSuchElementException:
            pass  # Popup did not appear


    def fetch_followers_and_following(self, url):
        """Fetch the number of followers and following from the given Instagram URL."""
        try:
            self.driver.get(url)
            # Wait for the page to load completely
            self.driver.implicitly_wait(5)
            self.driver.refresh()
            # Close popup if it appears
            self.close_popup()


            # Use XPATH to locate followers and following counts
            followers_xpath = "(//button[@type='button'])[3]"   # Update if necessary based on actual structure
            following_xpath = "(//button[@type='button'])[4]"   # Update if necessary based on actual structure

            followers = self.driver.find_element(By.XPATH, followers_xpath).text
            following = self.driver.find_element(By.XPATH, following_xpath).text

            return {
                "followers": followers,
                "following": following
            }

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def quit_driver(self):
        """Quit the Selenium WebDriver."""
        self.driver.quit()


if __name__ == "__main__":
    # Instantiate the scraper
    scraper = InstagramScraper()

    # Define the Instagram URL
    url = "https://www.instagram.com/guviofficial/"

    # Fetch followers and following
    data = scraper.fetch_followers_and_following(url)

    if data:
        print(f"Followers: {data['followers']}")
        print(f"Following: {data['following']}")

    # Quit the driver
    scraper.quit_driver()
