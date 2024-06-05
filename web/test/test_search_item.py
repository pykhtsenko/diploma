import pytest
import time

from web.pages.main_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


class TestAddItemToCart:

    def test_critical_path(self, main_page):

        main_page.find_and_click_catalog()

        main_page.input_text_into_search_field(text='стиральная машина Bosch')

        main_page.select_search_element()

        main_page.add_item_to_cart()

        main_page.open_cart()

        main_page.assert_cart_title(text='Корзина')

        main_page.assert_price_items_with_order_amount()

        main_page.element_is_clickable()