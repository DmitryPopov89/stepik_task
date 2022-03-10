import pytest
from pages import LoginPage, MainPage
from pages.base_page import BasePage
from pages.cart_page import CartPage


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, 'http://selenium1py.pythonanywhere.com/')
    page.open()
    page.go_to_login_page()


def test_should_be_login_link(browser):
    page = BasePage(browser, "http://selenium1py.pythonanywhere.com/en-gb/")
    page.open()
    page.should_be_login_link()


def test_should_be_login_page(browser):
    page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
    page.open()
    page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
    page.open()
    page.go_to_cart()

    cart = CartPage(browser, browser.current_url)
    assert not cart.product_in_cart()
    assert cart.empty_cart_message()


@pytest.mark.login_quest
class TestLoginFromMainPage:
    def test_quest_can_go_to_login_page(self, browser):
        page = MainPage(browser, "http://selenium1py.pythonanywhere.com")
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, "http://selenium1py.pythonanywhere.com")
        page.open()
        page.should_be_login_link()
