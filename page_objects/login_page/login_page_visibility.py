import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait

from utilities.read_properties import ReadLabelsConfig
from utilities.read_properties import ReadLoginConfig

from utilities import customLogger
logger = customLogger.get_logger("LoginPage")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class LoginPageVisibility:

    login_config = ReadLoginConfig()
    label_config = ReadLabelsConfig()

    logger = customLogger.get_logger("LoginPage")

    username_text = login_config.get_login_info('username_text')
    password_text = login_config.get_login_info('password_text')
    url_login_actual = login_config.get_login_info('url_login_actual')
    logo_top_xpath = login_config.get_login_info('logo_top_xpath')
    logo_right_xpath = login_config.get_login_info('logo_right_xpath')
    login_title_class_name = login_config.get_login_info('login_title_class_name')

    label_username_xpath = label_config.get_labels_info('label_username_xpath')
    label_password_xpath = label_config.get_labels_info('label_password_xpath')

    credentials_username_xpath = login_config.get_login_info('credentials_username_xpath')
    credentials_password_xpath = login_config.get_login_info('credentials_password_xpath')
    button_login_xpath = login_config.get_login_info('button_login_xpath')
    forgot_password_class_name = login_config.get_login_info('forgot_password_class_name')
    footer_class_name = login_config.get_login_info('footer_class_name')
    orangehrm_copyright_xpath_0 = login_config.get_login_info('orangehrm_copyright_xpath_0')
    orangehrm_copyright_xpath_1 = login_config.get_login_info('orangehrm_copyright_xpath_1')
    orangehrm_copyright_xpath_2 = login_config.get_login_info('orangehrm_copyright_xpath_2')
    social_network_icons_linkedin_xpath = login_config.get_login_info('social_network_icons_linkedin_xpath')
    social_network_icons_facebook_xpath = login_config.get_login_info('social_network_icons_facebook_xpath')
    social_network_icons_twitter_xpath = login_config.get_login_info('social_network_icons_twitter_xpath')
    social_network_icons_youtube_xpath = login_config.get_login_info('social_network_icons_youtube_xpath')

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

    def login_page_visibility(self):

        try:
            logo_top = WebDriverWait(self.driver, 5).until(
                ec.visibility_of_element_located((By.XPATH, self.logo_top_xpath)))
            assert logo_top.is_displayed()
            self.logger.info("logo_top is displayed")
        except Exception as e:
            self.logger.error("logo_top is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            logo_right = WebDriverWait(self.driver, 5).until(
                ec.visibility_of_element_located((By.XPATH, self.logo_right_xpath)))
            assert logo_right.is_displayed()
            self.logger.info("logo_right is displayed")
        except Exception as e:
            self.logger.error("logo_right is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            login_title = WebDriverWait(self.driver, 5).until(
                ec.visibility_of_element_located((By.CLASS_NAME, self.login_title_class_name)))
            assert login_title.is_displayed()
            self.logger.info("login_title is displayed")
        except Exception as e:
            self.logger.error("login_title is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            label_username_xpath = WebDriverWait(self.driver, 1).until(
                ec.visibility_of_element_located((By.XPATH, self.label_username_xpath)))
            assert label_username_xpath.is_displayed()
            self.logger.info("label_username_xpath is displayed")
        except Exception as e:
            self.logger.error("label_username_xpath is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            label_password_xpath = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.label_password_xpath)))
            assert label_password_xpath.is_displayed()
            self.logger.info("label_password_xpath is displayed")
        except Exception as e:
            self.logger.error("label_password_xpath is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            credentials_username_xpath = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.credentials_username_xpath)))
            assert credentials_username_xpath.is_displayed()
            credentials_username = self.driver.find_element(By.XPATH, self.credentials_username_xpath).text
            credentials_username_text = credentials_username.replace('Username : ', '')
            assert credentials_username_text == self.username_text
            self.logger.info("Username is: " + self.username_text)
        except Exception as e:
            self.logger.error("credentials_username_text is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            credentials_password_xpath = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.credentials_password_xpath)))
            assert credentials_password_xpath.is_displayed()
            credentials_password = self.driver.find_element(By.XPATH, self.credentials_password_xpath).text
            credentials_password_text = credentials_password.replace('Password : ', '')
            assert credentials_password_text == self.password_text
            self.logger.info("Password is:  " + self.password_text)
        except Exception as e:
            self.logger.error("credentials_password_text is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            input_username = self.driver.find_element(
                locate_with(By.TAG_NAME, "input").below(label_username_xpath))  # 1 input below label username
            assert input_username.is_displayed()
            self.logger.info("input_username is displayed")
        except Exception as e:
            self.logger.error("input_username is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            input_password = self.driver.find_element(
                locate_with(By.TAG_NAME, "input").below(label_password_xpath))  # 1 input below label password
            assert input_password.is_displayed()
            self.logger.info("input_password is displayed")
        except Exception as e:
            self.logger.error("input_password is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            button_login = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.button_login_xpath)))
            assert button_login.is_displayed()
            self.logger.info("button_login is displayed")
        except Exception as e:
            self.logger.error("button_login is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            forgot_password = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.CLASS_NAME, self.forgot_password_class_name)))
            assert forgot_password.is_displayed()
            self.logger.info("forgot_password is displayed")
        except Exception as e:
            self.logger.error("forgot_password not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            footer = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.CLASS_NAME, self.footer_class_name)))
            assert footer.is_displayed()
            self.logger.info("footer is displayed")
        except Exception as e:
            self.logger.error("footer is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            orangehrm_copyright = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.orangehrm_copyright_xpath_0)))
            assert orangehrm_copyright.is_displayed()
            self.logger.info("orangehrm_copyright is displayed")
        except Exception as e:
            self.logger.error("orangehrm_copyright is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            orangehrm_copyright_1 = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.orangehrm_copyright_xpath_1)))
            assert orangehrm_copyright_1.is_displayed()
            self.logger.info("orangehrm_copyright_1 is displayed")
        except Exception as e:
            self.logger.error("orangehrm_copyright_1 is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            orangehrm_copyright_2 = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.orangehrm_copyright_xpath_2)))
            assert orangehrm_copyright_2.is_displayed()
            self.logger.info("orangehrm_copyright_2 is displayed")
        except Exception as e:
            self.logger.error("orangehrm_copyright_2 is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            social_network_icons_linkedin = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.social_network_icons_linkedin_xpath)))
            assert social_network_icons_linkedin.is_displayed()
            self.logger.info("social_network_icons_linkedin is displayed")
        except Exception as e:
            self.logger.error("social_network_icons_linkedin is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            social_network_icons_facebook = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.social_network_icons_facebook_xpath)))
            assert social_network_icons_facebook.is_displayed()
            self.logger.info("social_network_icons_facebook is displayed")
        except Exception as e:
            self.logger.error("social_network_icons_facebook is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            social_network_icons_twitter = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.social_network_icons_twitter_xpath)))
            assert social_network_icons_twitter.is_displayed
            self.logger.info("social_network_icons_twitter is displayed")
        except Exception as e:
            self.logger.error("social_network_icons_twitter is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            social_network_icons_youtube = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.social_network_icons_youtube_xpath)))
            assert social_network_icons_youtube.is_displayed()
            self.logger.info("social_network_icons_youtube is displayed")
        except Exception as e:
            self.logger.error("social_network_icons_youtube is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))