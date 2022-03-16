import allure

from .base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):
    locators = CartPageLocators

    @allure.step('возвращает сообщение о том, что товар в корзине')
    def product_in_cart(self) -> bool:
        return self.is_element_present(*self.locators.PRODUCT_IN_CART)

    @allure.step('возвращает сообщение о то, что корзина пуста')
    def empty_cart_message(self) -> bool:
        return self.is_element_present(*self.locators.EMPTY_CART_MESSAGE)
