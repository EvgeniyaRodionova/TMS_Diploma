from add_cart import Cart_Helper
from login_screen import Login_Helper
from wishlist import Wishlist_Helper


def test_login(browser):
    login_page = Login_Helper(browser)
    login_page.go_to_site()
    login_page.sign_in_button()
    login_page.enter_email()
    login_page.enter_password()
    login_page.submit_login()


def test_wishlist(browser):
    wishlist_page = Wishlist_Helper(browser)
    wishlist_page.input_goods_name()
    wishlist_page.tap_search_icon()
    wishlist_page.select_other_color()
    wishlist_page.tap_on_heart()
    wishlist_page.in_wishlist()
    wishlist_page.close_message()


def test_cart_page(browser):
    cart_page = Cart_Helper(browser)
    cart_page.women_tab()
    cart_page.select_dress()
    cart_page.add_to_cart()
    cart_page.dress_in_cart()

