from selenium.webdriver.support.select import Select

from driver import Driver


class BasePage(Driver):
    URL = "https://magento.softwaretestingboard.com/"

    def get_page(self, link):
        self.driver.get(link)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find_element(locator).click()

    def get_text(self, locator):
        return self.find_element(locator).text

    def send_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def is_selected(self, locator):
        return self.find_element(locator).is_selected()

    def actual_url(self):
        return self.driver.current_url

    def select_dropdown(self, locator, country):
        country_elem = self.find_element(locator)
        select = Select(country_elem)
        select.select_by_visible_text(country)

    def click_checkbox(self, locator):
        checkbox_element = self.find_element(locator)
        if not checkbox_element.is_selected():
            self.click(locator)
