from seleniumbase import Driver


class Driver:
    driver = Driver()
    driver.maximize_window()
    driver.implicitly_wait(1)

    def close_driver(self):
        self.driver.quit()
