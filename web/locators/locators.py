from selenium.webdriver.common.by import By


SEARCH_INPUT = By.XPATH, '//input[@class="fast-search__input"]'
SEARCH_ITEMS = By.XPATH, '//li[@class="search__result"]'
CATALOG_BUTTON = By.XPATH, '//span[@class="b-main-navigation__text"][contains(text(),"Каталог")]'
IN_CART_BUTTONS = By.XPATH, '//a[@class="button-style button-style_base-alter button-style_primary product-aside__button product-aside__button_narrow product-aside__button_cart button-style_expletive"]'
CART_BUTTON = By.XPATH, '//a[@class="button-style button-style_another button-style_base-alter product-recommended__button"]'
CART_TITLE = By.XPATH, '//div[@class="cart-form__title cart-form__title_base cart-form__title_nocondensed cart-form__title_condensed-special"]'
PRICE_ITEM = By.XPATH, '//div[@class="cart-form__offers-part cart-form__offers-part_price cart-form__offers-part_price_specific helpers_hide_tablet"]/div[@class="cart-form__description cart-form__description_base-alter cart-form__description_font-weight_semibold cart-form__description_ellipsis cart-form__description_condensed"]'
ORDER_AMOUNT = By.XPATH, '//div[@class="cart-form__offers-part cart-form__offers-part_sum cart-form__offers-part_sum_clover cart-form__offers-part_sum_specific"]/div[@class="cart-form__description cart-form__description_base-alter cart-form__description_font-weight_semibold cart-form__description_ellipsis cart-form__description_condensed"]'
TO_ORDER = By.XPATH, '//a[@class="button-style button-style_small cart-form__button button-style_primary"]'