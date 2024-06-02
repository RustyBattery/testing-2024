from selenium.webdriver.common.by import By


class MainPageLocators(object):
    H1 = (By.TAG_NAME, 'h1')
    INPUT = (By.NAME, 'data')
    SUBMIT_BUTTON = (By.ID, 'submit-nums')


class ResultPageLocators(object):
    RESULT = (By.TAG_NAME, 'pre')
