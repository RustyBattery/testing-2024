from .locators import MainPageLocators, ResultPageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def fill_data(self, data):
        element = self.driver.find_element(*MainPageLocators.INPUT)
        element.send_keys(data)

    def click_send_btn(self):
        element = self.driver.find_element(*MainPageLocators.SUBMIT_BUTTON)
        element.click()


class ResultPage(BasePage):
    def get_result(self):
        result = self.driver.find_element(*ResultPageLocators.RESULT)
        return result.text


class ErrorPage(BasePage):
    def is_title_matches(self, title):
        return title == self.driver.title
