import time

import allure
import pytest
from pages import LoginPage, MainPage
from pages.base_page import BasePage
from pages.cart_page import CartPage


@allure.title('гость переходит на страницу авторизации')
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, 'http://selenium1py.pythonanywhere.com/')
    page.open()
    page.go_to_login_page()


@allure.title('тест проверяет кнопку регистрации и авторизации')
def test_should_be_login_link(browser):
    page = BasePage(browser, "http://selenium1py.pythonanywhere.com/en-gb/")
    page.open()
    page.should_be_login_link()


@allure.title('проверка наличия страницы регистрации и авторизации')
def test_should_be_login_page(browser):
    page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
    page.open()
    page.should_be_login_page()


@allure.title('гость переходит с главной страницы в корзину с товаром')
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
    page.open()
    page.go_to_cart()

    cart = CartPage(browser, browser.current_url)
    assert not cart.product_in_cart()
    assert cart.empty_cart_message()


@allure.title('гость переходит на страницу авторизации и проверяет страницу авторизации')
@pytest.mark.login_quest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, "http://selenium1py.pythonanywhere.com")
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        time.sleep(5)

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, "http://selenium1py.pythonanywhere.com")
        page.open()
        page.should_be_login_link()
        time.sleep(5)
