import time
from BaseApp import BasePage
from selenium.webdriver.common.by import By


class Locators:
    LOCATOR_WOMEN_TAB = (By.XPATH, "//*[@id='block_top_menu']/ul/li[1]/a")
    LOCATOR_DRESS = (By.XPATH, "//*[@id='special_block_right']/div/ul/li/a/img")
    LOCATOR_ADD_CART_BUTTON = (By.NAME, "Submit")
    LOCATOR_DRESS_IN_CART = (By.XPATH, "//*[@id='layer_cart']/div[1]/div[1]/h2")

class Cart_Helper(BasePage):

    def women_tab(self):
        search_women_tab = self.find_element(Locators.LOCATOR_WOMEN_TAB)
        search_women_tab.click()
        time.sleep(1.0)
        return search_women_tab

    def select_dress(self):
        search_dress = self.find_element(Locators.LOCATOR_DRESS)
        search_dress.click()
        time.sleep(1.0)
        return search_dress

    def add_to_cart(self):
        search_button_cart = self.find_element(Locators.LOCATOR_ADD_CART_BUTTON)
        search_button_cart.click()
        time.sleep(1.0)
        return search_button_cart

    def dress_in_cart(self):
        search_message = self.find_element(Locators.LOCATOR_DRESS_IN_CART).text
        assert "Product successfully added to your shopping cart" == search_message


