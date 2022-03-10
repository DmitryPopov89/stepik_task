from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    locators = ProductPageLocators()

    def add_product_to_cart(self):
        add_product = self.browser.find_element(*self.locators.BUTTON_ADD_PRODUCT_IN_CART)
        add_product.click()

    def should_be_product_name_in_alert(self):
        product_name = self.browser.find_element(*self.locators.PRODUCT_NAME).text
        product_name_in_alert = self.browser.find_element(*self.locators.PRODUCT_NAME_IN_ALERT).text
        assert product_name == product_name_in_alert, f'ожидали {product_name}, получили {product_name_in_alert}'

    def should_be_product_price_in_alert(self):
        product_price = self.browser.find_element(*self.locators.PRODUCT_PRICE).text
        product_price_in_alert = self.browser.find_element(*self.locators.PRODUCT_PRICE_IN_ALERT).text
        assert product_price == product_price_in_alert, f'ожидали {product_price}, получили {product_price_in_alert}'

