import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait

from utilities.read_properties import ReadLabelsConfig
from utilities.read_properties import ReadLoginConfig
from utilities.read_properties import ReadUrl

from utilities import customLogger


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Login:

    login_config = ReadLoginConfig()
    label_config = ReadLabelsConfig()
    url_config = ReadUrl()

    logger = customLogger.get_logger("LoginPage")

    username_text = login_config.get_login_info('username_text')
    password_text = login_config.get_login_info('password_text')

    label_username_xpath = label_config.get_labels_info('label_username_xpath')
    label_password_xpath = label_config.get_labels_info('label_password_xpath')

    button_login_xpath = login_config.get_login_info('button_login_xpath')

    def __init__(self, driver):
        self.driver = driver

    def check_url(self, url):
        try:
            login_url = self.driver.current_url
            assert login_url == url
            print("url is: ", login_url)
        except Exception as e:
            self.logger.error("url is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def click_login_button(self):
        try:
            login_button = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.button_login_xpath)))
            assert login_button.text == "Login"
            self.logger.info("login_button is displayed")
            login_button.click()
        except Exception as e:
            self.logger.error("login_button is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def input_paragraph_username(self):
        label_username_xpath = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.label_username_xpath)))
        assert label_username_xpath.is_displayed()

        credentials_username_xpath = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.credentials_username_xpath)))
        assert credentials_username_xpath.is_displayed()

        credentials_username = self.driver.find_element(By.XPATH, self.credentials_username_xpath).text
        credentials_username_text = credentials_username.replace('Username : ', '')
        assert credentials_username_text == self.username_text

        input_username = self.driver.find_element(
            locate_with(By.TAG_NAME, "input").below(label_username_xpath))
        assert input_username.is_displayed()

        input_username.send_keys(credentials_username_text)

        try:
            assert credentials_username_text == self.username_text
            self.logger.info("credentials_username_text pass")
        except Exception as e:
            self.logger.error("credentials_username_text failed " + credentials_username_text, exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def input_paragraph_password(self):
        label_password_xpath = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.label_password_xpath)))
        assert label_password_xpath.is_displayed()

        credentials_password_xpath = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.credentials_password_xpath)))
        assert credentials_password_xpath.is_displayed()
        credentials_password = self.driver.find_element(By.XPATH, self.credentials_password_xpath).text
        credentials_password_text = credentials_password.replace('Password : ', '')
        assert credentials_password_text == self.password_text

        input_password = self.driver.find_element(
            locate_with(By.TAG_NAME, "input").below(label_password_xpath))
        assert input_password.is_displayed()

        input_password.send_keys(credentials_password_text)

        try:
            assert credentials_password_text == self.password_text
            self.logger.info("credentials_password_text pass")
        except Exception as e:
            self.logger.error("credentials_password_text failed " + credentials_password_text, exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def input_username(self, username):
        try:
            label_username_xpath = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.label_username_xpath)))
            assert label_username_xpath.is_displayed()
            self.logger.info("label_username_xpath is displayed")
        except Exception as e:
            self.logger.error("input_username failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            input_username = self.driver.find_element(
                locate_with(By.TAG_NAME, "input").below(label_username_xpath))
            self.logger.info("input_username is displayed")
        except Exception as e:
            self.logger.error("input_username is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        input_username.send_keys(username)

    def input_password(self, password):
        try:
            label_password_xpath = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.label_password_xpath)))
            assert label_password_xpath.is_displayed()
            self.logger.info("label_password_xpath is displayed")
        except Exception as e:
            self.logger.error("label_password_xpath failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            input_password = self.driver.find_element(
                locate_with(By.TAG_NAME, "input").below(label_password_xpath))
            self.logger.info("input_password is displayed")
        except Exception as e:
            self.logger.error("input_password is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        input_password.send_keys(password)
