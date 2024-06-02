import page_object.page as page
from page_object.locators import MainPageLocators


class TestUI:
    def test_app_main_page_has_h1_valid(self, browser):
        main_page = page.MainPage(browser)
        assert main_page.driver.find_element(*MainPageLocators.H1).text == 'Max product'

    def test_app_main_page_has_input(self, browser):
        main_page = page.MainPage(browser)
        assert main_page.driver.find_element(*MainPageLocators.INPUT)

    def test_app_main_page_has_submit_btn(self, browser):
        main_page = page.MainPage(browser)
        assert main_page.driver.find_element(*MainPageLocators.SUBMIT_BUTTON)

    def test_app_isset_result_with_valid_data(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_data('1 2 3 1 1 1 0 1')
        main_page.click_send_btn()
        result_page = page.ResultPage(browser)
        assert result_page.get_result()

    def test_app_correct_result_with_valid_data(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_data('1 2 3 1 1 1 0 1')
        main_page.click_send_btn()
        result_page = page.ResultPage(browser)
        assert result_page.get_result() == '{\n  "res": 6\n}'

    def test_app_error_if_invalid_data_type(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_data('cat say meow 3 times')
        main_page.click_send_btn()
        error_page = page.ErrorPage(browser)
        assert error_page.is_title_matches('400 Bad Request')

    def test_app_error_if_empty_data(self, browser):
        main_page = page.MainPage(browser)
        main_page.click_send_btn()
        error_page = page.ErrorPage(browser)
        assert error_page.is_title_matches('400 Bad Request')

    def test_app_error_if_data_out_of_range(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_data('1 2 3 0 15 100')
        main_page.click_send_btn()
        error_page = page.ErrorPage(browser)
        assert error_page.is_title_matches('400 Bad Request')
