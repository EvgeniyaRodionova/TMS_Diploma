from framework.BaseApp import BasePage
from selenium.webdriver.common.by import By


class Locators:
    LOCATOR_SEARCH_FIELD = (By.ID, "search_query_top")
    LOCATOR_SEARCH_BUTTON = (By.NAME, "submit_search")
    LOCATOR_EYE_ICON = (By.CLASS_NAME, "quick-view-mobile")
    LOCATOR_SELECT_OTHER_COLOR = (By.CLASS_NAME, "color_pick")
    LOCATOR_WISHLIST_BUTTON = (By.ID, "wishlist_button")
    LOCATOR_ADD_WISHLIST = (By.CLASS_NAME, "fancybox-error")
    LOCATOR_CLOSE = (By.XPATH, "//*[@id='product']/div[2]/div/div/a")


class WishlistHelper(BasePage):

    def input_goods_name(self):
        search_field = self.find_element(Locators.LOCATOR_SEARCH_FIELD)
        search_field.send_keys("blouse")
        return search_field

    def tap_search_icon(self):
        search_goods = self.find_element(Locators.LOCATOR_SEARCH_BUTTON)
        search_goods.click()
        return search_goods

    def select_other_color(self):
        search_color = self.find_element(Locators.LOCATOR_SELECT_OTHER_COLOR)
        search_color.click()
        return search_color

    def tap_on_heart(self):
        search_wishlist_heart = self.find_element(Locators.LOCATOR_WISHLIST_BUTTON)
        search_wishlist_heart.click()
        return search_wishlist_heart

    def in_wishlist(self):
        search_message = self.find_element(Locators.LOCATOR_ADD_WISHLIST).text
        assert "Added to your wishlist." == search_message

    def close_message(self):
        search_close_icon = self.find_element(Locators.LOCATOR_CLOSE)
        search_close_icon.click()
        return search_close_icon


