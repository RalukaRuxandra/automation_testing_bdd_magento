from selenium.webdriver.support.select import Select

from driver import Driver


class BasePage(Driver):
    URL = "https://magento.softwaretestingboard.com/"
    SIGN_IN_URL = "https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/"
    ADDRESS_URL = "https://magento.softwaretestingboard.com/customer/address/index/"

    def get_page(self, link):
        self.driver.get(link)

    def find_elem(self, locator):
        return self.driver.find_element(*locator)

    def click_elem(self, locator):
        self.find_elem(locator).click()

    def get_text(self, locator):
        return self.find_elem(locator).text

    def send_text(self, locator, text):
        self.find_elem(locator).send_keys(text)

    def is_displayed(self, locator):
        return self.find_elem(locator).is_displayed()

    def is_selected(self, locator):
        return self.find_elem(locator).is_selected()

    def actual_url(self):
        return self.driver.current_url

    def select_dropdown(self, locator, country):
        country_elem = self.find_elem(locator)
        select = Select(country_elem)
        select.select_by_visible_text(country)

    def click_checkbox(self, locator):
        checkbox_element = self.find_elem(locator)
        if not checkbox_element.is_selected():
            self.click_elem(locator)
