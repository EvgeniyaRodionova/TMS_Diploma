from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://automationpractice.com/index.php"

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)
