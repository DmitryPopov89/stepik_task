import time
import pytest
from pages import LoginPage
from pages.cart_page import CartPage
from pages.locators import ProductPageLocators
from pages.product_page import ProductPage


@pytest.mark.need_review
@pytest.mark.parametrize('url', ['promo=offer0', 'promo=offer1', 'promo=offer2', 'promo=offer3', 'promo=offer4',
                                 'promo=offer5', 'promo=offer6', pytest.param('promo=offer7', marks=pytest.mark.xfail),
                                 'promo=offer8', 'promo=offer9'])
def test_guest_can_add_product_to_cart(browser, url):
    page = ProductPage(browser, f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{url}')
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_product_price_in_alert()
    page.should_be_product_name_in_alert()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    page.open()
    page.add_product_to_cart()
    assert page.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_ALERT), 'Элемент присутствует'


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    page.open()
    page.add_product_to_cart()
    assert page.is_disappeared(*ProductPageLocators.PRODUCT_NAME_IN_ALERT)


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/")
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/")
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/")
    page.open()
    page.go_to_cart()

    cart = CartPage(browser, browser.current_url)
    assert not cart.product_in_cart()
    assert cart.empty_cart_message()


@pytest.mark.current
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function")
    def setup(self, browser):
        login_page = LoginPage(browser, 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/')
        login_page.open()
        mail = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(
            email=mail,
            password='333444555666'
        )
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, setup):
        page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_ALERT), 'Element is present'

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser, setup):
        page = ProductPage(browser,
                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019")
        page.open()
        page.add_product_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_product_price_in_alert()
        page.should_be_product_name_in_alert()
