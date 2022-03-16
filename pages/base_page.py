import math

import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import BasePageLocators


class BasePage:
    locators = BasePageLocators()

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4) -> bool:
        """
            Ожидание исчезновения элемента
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    @allure.step('переходит на страницу авторизации')
    def go_to_login_page(self):
        login_link = self.browser.find_element(*self.locators.LOGIN_OR_REGISTER_LINK)
        login_link.click()

    @allure.step('проверяет наличие кнопки для регистрации и авторизации ')
    def should_be_login_link(self):
        assert self.is_element_present(*self.locators.LOGIN_OR_REGISTER_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

@allure.step('переходит на страницу Корзины')
    def go_to_cart(self):
        button_go_to_cart = self.browser.find_element(*self.locators.GO_TO_CART)
        button_go_to_cart.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON)
