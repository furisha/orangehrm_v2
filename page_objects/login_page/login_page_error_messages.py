import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait

from utilities.read_properties import ReadLabelsConfig
from utilities.read_properties import ReadLoginConfig

from utilities import customLogger


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class LoginPageErrorMessages:

    login_config = ReadLoginConfig()
    label_config = ReadLabelsConfig()

    logger = customLogger.get_logger("LoginPage")

    username_text = login_config.get_login_info('username_text')
    password_text = login_config.get_login_info('password_text')
    url_login_actual = login_config.get_login_info('url_login_actual')

    label_username_xpath = label_config.get_labels_info('label_username_xpath')
    label_password_xpath = label_config.get_labels_info('label_password_xpath')

    error_message_username_xpath = login_config.get_login_info('error_message_username_xpath')
    error_message_password_xpath = login_config.get_login_info('error_message_password_xpath')
    error_message_invalid_credentials_xpath = login_config.get_login_info('error_message_invalid_credentials_xpath')
    message_invalid_text = login_config.get_login_info('message_invalid_text')

    # Create Constructor
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

    def input_random_username(self):

        random_input_username = random_generator()

        label_username_xpath = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.label_username_xpath)))
        input_username = self.driver.find_element(
            locate_with(By.TAG_NAME, "input").below(label_username_xpath))

        input_username.send_keys(random_input_username)

        self.logger.info("Input random username:" + random_input_username)

    def input_random_password(self):

        random_input_password = random_generator()

        label_password_xpath = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.label_password_xpath)))
        input_password = self.driver.find_element(
            locate_with(By.TAG_NAME, "input").below(label_password_xpath))

        input_password.send_keys(random_input_password)

        self.logger.info("Input random password :" + random_input_password)

    def message_invalid_required_username(self):
        try:
            error_message_username = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.error_message_username_xpath)))
            assert error_message_username.text == self.message_invalid_text
            self.logger.info("message_invalid_required_username pass")
        except Exception as e:
            self.logger.error("message_invalid_required_username failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def message_invalid_required_password(self):
        try:
            error_message_password = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.error_message_password_xpath)))
            assert error_message_password.text == self.message_invalid_text
            self.logger.info("message_invalid_required_password pass")
        except Exception as e:
            self.logger.error("message_invalid_required_password failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def message_invalid_credentials(self):
        try:
            error_message_invalid_credentials = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.error_message_invalid_credentials_xpath)))
            assert error_message_invalid_credentials.is_displayed()
            self.logger.info("error_message_invalid_credentials is displayed")
        except Exception as e:
            self.logger.error("error_message_invalid_credentials is not displayed", exc_info=True)
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

    # def forgot_password(self):

    # def logout_user(self):

    # ...
