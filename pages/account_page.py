import unittest

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class AccountPage(BasePage, unittest.TestCase):

    WOMEN_BUTTON = (By.XPATH, '//a[@id="ui-id-4"]')
    TOPS_BUTTON = (By.XPATH, '//a[@id="ui-id-9"]')
    JACKETS_BUTTON = (By.XPATH, '//a[@id="ui-id-11"]')
    FIRST_ITEM = (By.XPATH, '(//li[@class="item product product-item"])[1]')
    FIRST_ITEM_URL = 'https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html'
    ITEM_NAME = (By.XPATH, '//span[@itemprop="name"]')
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[@title="Add to Cart"]')
    SIZE_ERROR_MESSAGE = (By.XPATH, '//div[@id="super_attribute[143]-error"]')
    COLOUR_ERROR_MESSAGE = (By.XPATH, '//div[@id="super_attribute[93]-error"]')
    SIZE_M_BUTTON = (By.ID, 'option-label-size-143-item-168')
    BLACK_COLOUR_ITEM = (By.XPATH, '//img[@src="https://magento.softwaretestingboard.com/pub/media/catalog/product/cache/d34482110da20c5e24f97c38fb219fb3/w/j/wj12-black_main_1.jpg"]')
    BLACK_COLOUR_BUTTON = (By.XPATH, '//div[@id="option-label-color-93-item-49"]')
    BLUE_COLOUR_ITEM = (By.XPATH, '//img[@src="https://magento.softwaretestingboard.com/pub/media/catalog/product/cache/d34482110da20c5e24f97c38fb219fb3/w/j/wj12-blue_main_1.jpg"]')
    BLUE_COLOUR_BUTTON = (By.XPATH, '//div[@id="option-label-color-93-item-50"]')
    PURPLE_COLOUR_ITEM = (By.XPATH, '//img[@src="https://magento.softwaretestingboard.com/pub/media/catalog/product/cache/d34482110da20c5e24f97c38fb219fb3/w/j/wj12-purple_main_1.jpg"]')
    PURPLE_COLOUR_BUTTON = (By.XPATH, '//div[@id="option-label-color-93-item-57"]')
    CONFIRMATION_MESSAGE = (By.XPATH, '//div[@data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
    ITEMS_IN_CART = (By.XPATH, '//span[@class="counter-number"]')
    PROCEED_TO_CHECKOUT = (By.XPATH, '//button[@id="top-cart-btn-checkout"]')
    SHIPPING_URL = 'https://magento.softwaretestingboard.com/checkout/#shipping'
    NEW_ADDRESS_BUTTON = (By.XPATH, '//*[@id="checkout-step-shipping"]/div[2]/button/span')
    STREET_BOX = (By.XPATH, '//input[@id="RJJCGD7"]')
    CITY_BOX = (By.XPATH, '//input[@id="S4WA7S0"]')
    STATE_BOX = (By.ID, 'S3DE2YA')
    ZIP_BOX = (By.XPATH, '//input[@id="PG20WHJ"]')
    COUNTRY_BOX = (By.ID, 'FEQSX7T')
    PHONE_BOX = (By.XPATH, '//input[@id="WU7RURQ"]')
    CHECKBOX_BUTTON = (By.ID, 'shipping-save-in-address-book')
    SHIP_HERE_BUTTON = (By.XPATH, '//button[@class="action primary action-save-address"]')
    NEXT_BUTTON = (By.XPATH, '//button[@class="button action continue primary"]')
    PAYMENT_URL = 'https://magento.softwaretestingboard.com/checkout/#payment'
    SAME_ADDRESSES = (By.XPATH, '//input[@type="checkbox"]')
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[@class="action action-apply"]')
    SUCCESS_PURCHASE_URL = 'https://magento.softwaretestingboard.com/checkout/onepage/success/'

    def select_product(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(self.WOMEN_BUTTON)).perform()
        actions.move_to_element(self.find_element(self.TOPS_BUTTON)).perform()
        self.find_element(self.JACKETS_BUTTON).click()

    def click_first_item(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FIRST_ITEM))
        self.click(self.FIRST_ITEM)

    def check_item_url(self):
        return self.actual_url() == self.FIRST_ITEM_URL

    def is_item_name_displayed(self):
        return self.is_displayed(self.ITEM_NAME)

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def are_error_messages_displayed(self):
        return self.is_displayed(self.SIZE_ERROR_MESSAGE), self.is_displayed(self.COLOUR_ERROR_MESSAGE)

    def check_error_messages(self, err):
        return self.get_text(self.SIZE_ERROR_MESSAGE) == err, self.get_text(self.COLOUR_ERROR_MESSAGE) == err

    def click_size(self):
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SIZE_M_BUTTON))
        self.click(self.SIZE_M_BUTTON)

    def change_colour(self):
        if self.is_displayed(self.BLACK_COLOUR_ITEM):
            self.click(self.BLUE_COLOUR_BUTTON)
        elif self.is_displayed(self.BLUE_COLOUR_ITEM):
            self.click(self.PURPLE_COLOUR_BUTTON)
        else:
            self.click(self.BLACK_COLOUR_BUTTON)

    def check_if_colour_match(self):
        if self.is_selected(self.BLACK_COLOUR_BUTTON) and self.is_displayed(self.BLACK_COLOUR_ITEM):
            self.click_add_to_cart()
        elif self.is_selected(self.BLUE_COLOUR_BUTTON) and self.is_displayed(self.BLUE_COLOUR_ITEM):
            self.click_add_to_cart()
        elif self.is_selected(self.PURPLE_COLOUR_BUTTON) and self.is_displayed(self.PURPLE_COLOUR_ITEM):
            self.click_add_to_cart()
        else:
            self.change_colour()

    def is_confirmation_message_displayed(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CONFIRMATION_MESSAGE))
        return self.is_displayed(self.CONFIRMATION_MESSAGE)

    def check_confirmation_message(self, confirmation):
        return self.get_text(self.CONFIRMATION_MESSAGE) == confirmation

    def check_number_of_items(self):
        return self.get_text(self.ITEMS_IN_CART) == "1"

    def click_cart(self):
        self.click(self.ITEMS_IN_CART)

    def click_proceed_to_checkout(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PROCEED_TO_CHECKOUT))
        self.click(self.PROCEED_TO_CHECKOUT)

    def check_shipping_page(self):
        WebDriverWait(self.driver, 10).until(EC.url_matches(self.SHIPPING_URL))
        return self.actual_url() == self.SHIPPING_URL

    def click_new_address(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.NEW_ADDRESS_BUTTON))
        self.click(self.NEW_ADDRESS_BUTTON)

    def insert_shipping_info(self):
        self.send_text(self.STREET_BOX, 'via Spinelli 7')
        self.select_dropdown(self.COUNTRY_BOX, 'Italia')
        self.send_text(self.CITY_BOX, 'Forli')
        self.send_text(self.STATE_BOX, 'Bologna')
        self.send_text(self.ZIP_BOX, '123456')
        self.send_text(self.PHONE_BOX, '3887960981')

    def click_save_address(self):
        self.click_checkbox(self.CHECKBOX_BUTTON)

    def click_ship_here(self):
        self.click(self.SHIP_HERE_BUTTON)

    def click_next(self):
        self.click(self.NEXT_BUTTON)

    def check_payment_url(self):
        return self.actual_url() == self.PAYMENT_URL

    def click_same_address(self):
        self.click_checkbox(self.SAME_ADDRESSES)

    def click_place_order(self):
        self.click(self.PLACE_ORDER_BUTTON)

    def check_success_url(self):
        return self.actual_url() == self.SUCCESS_PURCHASE_URL #de facut metoda generala
