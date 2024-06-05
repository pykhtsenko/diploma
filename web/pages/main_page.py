from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from web.locators.locators import (SEARCH_INPUT,
                                         SEARCH_ITEMS,
                                         CATALOG_BUTTON,
                                         IN_CART_BUTTONS,
                                         CART_BUTTON,
                                         CART_TITLE,
                                         PRICE_ITEM,
                                         ORDER_AMOUNT,
                                         TO_ORDER)

time_default = 0.5

class MainPage:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def find_and_click_catalog(self):
        catalog = WebDriverWait(self.driver, time_default).until(es.element_to_be_clickable(CATALOG_BUTTON))
        catalog.click()

    @property
    def search_field_input(self):
        element = (WebDriverWait(self.driver, 1).until(es.visibility_of_element_located(SEARCH_INPUT)).
                   find_element(*SEARCH_INPUT))
        return element

    def input_text_into_search_field(self, text: str):
        self.search_field_input.send_keys(text)

    def select_search_element(self):
        items = (WebDriverWait(self.driver, 2).until(es.visibility_of_element_located(SEARCH_ITEMS)).
                 find_elements(*SEARCH_ITEMS))
        i = 0
        for item in items:
            i = i+1
            if i == 5:
                item.click()
                break

    def add_item_to_cart(self):
        items = (WebDriverWait(self.driver, 1).until(es.visibility_of_element_located(IN_CART_BUTTONS)).
                 find_elements(*IN_CART_BUTTONS))
        for item in items:
            if item.text == 'В корзину':
                item.click()
                break

    def open_cart(self):
        button_cart = WebDriverWait(self.driver, 5).until(es.element_to_be_clickable(CART_BUTTON))
        button_cart.click()

    def element_is_clickable(self):
        order = WebDriverWait(self.driver, 1).until(es.element_to_be_clickable(TO_ORDER))
        order.click()

    def assert_cart_title(self, text: str):
        cart_title = WebDriverWait(self.driver, time_default).until(es.visibility_of_element_located(CART_TITLE))
        assert cart_title.text == text

    def assert_price_items_with_order_amount(self):
        price_item = WebDriverWait(self.driver, time_default).until(es.visibility_of_element_located(PRICE_ITEM))
        order_amount = WebDriverWait(self.driver, time_default).until(es.visibility_of_element_located(ORDER_AMOUNT))
        assert price_item.text == order_amount.text[:len(price_item.text)]