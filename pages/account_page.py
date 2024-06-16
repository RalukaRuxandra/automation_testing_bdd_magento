
import unittest

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
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
    SIZE_XS_BUTTON = (By.XPATH, '//div[@id="option-label-size-143-item-166"]')
    SIZE_S_BUTTON = (By.XPATH, '//div[@id="option-label-size-143-item-167"]')
    SIZE_M_BUTTON = (By.XPATH, '//div[@id="option-label-size-143-item-168"]')
    SIZE_L_BUTTON = (By.XPATH, '//div[@id="option-label-size-143-item-169"]')
    SIZE_XL_BUTTON = (By.XPATH, '//div[@id="option-label-size-143-item-170"]')
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
    FIRST_NAME_BOX = (By.XPATH, '//input[@id="firstname"]')
    LAST_NAME_BOX = (By.XPATH, '//input[@id="lastname"]')
    STREET_BOX = (By.XPATH, '//input[@id="street_1"]')
    CITY_BOX = (By.XPATH, '//input[@name="city"]')
    STATE_BOX = (By.XPATH, '//input[@id="region"]')
    ZIP_BOX = (By.XPATH, '//input[@id="zip"]')
    COUNTRY_BOX = (By.ID, 'country')
    PHONE_BOX = (By.XPATH, '//input[@id="telephone"]')
    CHECKBOX_BUTTON = (By.ID, 'shipping-save-in-address-book')
    NEXT_BUTTON = (By.XPATH, '//button[@class="button action continue primary"]')
    PAYMENT_URL = 'https://magento.softwaretestingboard.com/checkout/#payment'
    SAME_ADDRESSES = (By.XPATH, '//input[@type="checkbox"]')
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[@class="action action-apply"]')
    SUCCESS_PURCHASE_URL = 'https://magento.softwaretestingboard.com/checkout/onepage/success/'
    CUSTOMER_MENU_BUTTON = (By.XPATH, '//div[@class="panel header"]//button[@type="button"]')
    MY_ACCOUNT_BUTTON = (By.XPATH, '//div[@aria-hidden="false"]//a[normalize-space()="My Account"]')
    CHANGE_BILLING_ADDRESS_BUTTON = (By.XPATH, '//div[@class="box box-billing-address"]//span[contains(text(),"Edit Address")]')
    CHANGE_SHIPPING_ADDRESS_BUTTON = (By.XPATH, '//div[@class="box box-shipping-address"]//span[contains(text(),"Edit Address")]')
    SAVE_ADDRESS_BUTTON = (By.XPATH, '//button[@class="action save primary"]')

    fake = Faker(locale='it')

    def select_product(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_elem(self.WOMEN_BUTTON)).perform()
        actions.move_to_element(self.find_elem(self.TOPS_BUTTON)).perform()
        self.find_elem(self.JACKETS_BUTTON).click()

    def click_first_item(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FIRST_ITEM))
        self.click_elem(self.FIRST_ITEM)

    def check_item_url(self):
        assert self.actual_url() == self.FIRST_ITEM_URL

    def click_add_to_cart(self):
        self.click_elem(self.ADD_TO_CART_BUTTON)

    def are_error_messages_displayed(self, err_msgs):
        assert self.is_displayed(self.SIZE_ERROR_MESSAGE) and self.is_displayed(self.COLOUR_ERROR_MESSAGE) and self.get_text(self.SIZE_ERROR_MESSAGE) == err_msgs and self.get_text(self.COLOUR_ERROR_MESSAGE) == err_msgs

    def click_size(self, size):
        if size == 'XS':
            self.click_elem(self.SIZE_XS_BUTTON)
        elif size == 'S':
            self.click_elem(self.SIZE_S_BUTTON)
        elif size == 'M':
            self.click_elem(self.SIZE_M_BUTTON)
        elif size == 'L':
            self.click_elem(self.SIZE_L_BUTTON)
        else:
            self.click_elem(self.SIZE_XL_BUTTON)

    def change_colour(self):
        if self.is_displayed(self.BLACK_COLOUR_ITEM):
            self.click_elem(self.BLUE_COLOUR_BUTTON)
        elif self.is_displayed(self.BLUE_COLOUR_ITEM):
            self.click_elem(self.PURPLE_COLOUR_BUTTON)
        else:
            self.click_elem(self.BLACK_COLOUR_BUTTON)

    def is_confirmation_message_displayed(self, confirmation_msg):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CONFIRMATION_MESSAGE))
        assert self.is_displayed(self.CONFIRMATION_MESSAGE) and self.get_text(self.CONFIRMATION_MESSAGE) == confirmation_msg

    def click_cart(self):
        self.click_elem(self.ITEMS_IN_CART)

    def click_proceed_to_checkout(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PROCEED_TO_CHECKOUT))
        self.click_elem(self.PROCEED_TO_CHECKOUT)

    def check_shipping_page(self):
        WebDriverWait(self.driver, 10).until(EC.url_matches(self.SHIPPING_URL))
        return self.actual_url() == self.SHIPPING_URL

    def click_customer_menu_arrow(self):
        self.click_elem(self.CUSTOMER_MENU_BUTTON)

    def click_my_account(self):
        self.click_elem(self.MY_ACCOUNT_BUTTON)

    def click_change_shipping_address(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CHANGE_SHIPPING_ADDRESS_BUTTON))
        self.click_elem(self.CHANGE_SHIPPING_ADDRESS_BUTTON)

    def insert_billing_or_shipping_info(self):
        first_name = self.fake.first_name()
        self.find_elem(self.FIRST_NAME_BOX).clear()
        self.send_text(self.FIRST_NAME_BOX, first_name)
        last_name = self.fake.last_name()
        self.find_elem(self.LAST_NAME_BOX).clear()
        self.send_text(self.LAST_NAME_BOX, last_name)
        self.select_dropdown(self.COUNTRY_BOX, 'Italy')
        city = self.fake.city()
        self.find_elem(self.CITY_BOX).clear()
        self.send_text(self.CITY_BOX, city)
        state = self.fake.state()
        self.find_elem(self.STATE_BOX).clear()
        self.send_text(self.STATE_BOX, state)
        cap = self.fake.postcode()
        self.find_elem(self.ZIP_BOX).clear()
        self.send_text(self.ZIP_BOX, cap)
        phone_number = self.fake.phone_number()
        self.find_elem(self.PHONE_BOX).clear()
        self.send_text(self.PHONE_BOX, phone_number)
        street = self.fake.address()
        self.find_elem(self.STREET_BOX).clear()
        self.send_text(self.STREET_BOX, street)

    def click_save_address(self):
        self.click_elem(self.SAVE_ADDRESS_BUTTON)

    def check_address_url(self):
        assert self.ADDRESS_URL == self.actual_url()

    def click_next(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.NEXT_BUTTON))
        self.click_elem(self.NEXT_BUTTON)

    def check_payment_url(self):
        WebDriverWait(self.driver, 10).until(EC.url_matches(self.PAYMENT_URL))
        assert self.actual_url() == self.PAYMENT_URL

    def click_same_address(self):
        self.click_checkbox(self.SAME_ADDRESSES)

    def click_place_order(self):
        self.click_elem(self.PLACE_ORDER_BUTTON)

    def check_success_url(self):
        assert self.actual_url() == self.SUCCESS_PURCHASE_URL

    def check_sign_in_url(self):
        assert self.actual_url() == self.SIGN_IN_URL
