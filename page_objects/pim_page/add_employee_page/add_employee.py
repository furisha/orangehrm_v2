import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.relative_locator import locate_with

from selenium.webdriver import ActionChains
from selenium.webdriver import Keys

from utilities import customLogger
from utilities.read_properties import ReadLoginConfig
from utilities.read_properties import ReadMainMenuElements
from utilities.read_properties import ReadTopBarConfig
from utilities.read_properties import ReadLabelsConfig
from utilities.read_properties import ReadPimElements


class PIMAddEmployee:

    logger = customLogger.get_logger("LoginPage")
    login_config = ReadLoginConfig()
    main_menu_elements = ReadMainMenuElements()
    pim_elements = ReadPimElements()
    label_config = ReadLabelsConfig()
    topbar_config = ReadTopBarConfig()

    base_url = login_config.get_login_info('base_url')
    username_text = login_config.get_login_info('username_text')
    password_text = login_config.get_login_info('password_text')
    login_title_class_name = login_config.get_login_info('login_title_class_name')

    search_pim = main_menu_elements.get_main_menu_info('txt_main_menu_pim')

    button_add_xpath = pim_elements.get_pim_info('button_add_xpath')
    button_cancel_xpath = pim_elements.get_pim_info('button_cancel_xpath')
    button_save_xpath = pim_elements.get_pim_info('button_save_xpath')

    password_hint_xpath = pim_elements.get_pim_info('password_hint_xpath')

    input_first_name_xpath = pim_elements.get_pim_info('input_first_name_xpath')
    input_middle_name_xpath = pim_elements.get_pim_info('input_middle_name_xpath')
    input_lastname_xpath = pim_elements.get_pim_info('input_lastname_xpath')
    input_employee_id_xpath = pim_elements.get_pim_info('input_employee_id_xpath')

    label_employee_id_xpath = label_config.get_labels_info('label_employee_id_xpath')
    label_username_xpath = label_config.get_labels_info('label_username_xpath')
    label_password_xpath = label_config.get_labels_info('label_password_xpath')
    label_confirm_password_xpath = label_config.get_labels_info('label_confirm_password_xpath')
    label_status_xpath = label_config.get_labels_info('label_status_xpath')
    label_enabled_xpath = label_config.get_labels_info('label_enabled_xpath')
    label_disabled_xpath = label_config.get_labels_info('label_disabled_xpath')

    topbar_title_header = topbar_config.get_topbar_info('topbar_title_header_xpath')
    topbar_user_dropdown_xpath = topbar_config.get_topbar_info('topbar_user_dropdown_xpath')
    topbar_user_dropdown_menu_xpath = topbar_config.get_topbar_info('topbar_user_dropdown_menu_xpath')
    topbar_menu_item_xpath = topbar_config.get_topbar_info('topbar_menu_item_xpath')
    topbar_menu_item_name_xpath = topbar_config.get_topbar_info('topbar_menu_item_name_xpath')

    def __init__(self, driver):
        self.driver = driver

    def click_add_button(self):
        button_add = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, self.button_add_xpath)))
        assert button_add.is_displayed()
        button_add.click()
        time.sleep(1)

    def click_save_button(self):
        try:
            save_button = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.button_save_xpath)))
            assert save_button.text == "Save"
            self.logger.info("save_button is displayed")
            save_button.click()
            time.sleep(1)
        except Exception as e:
            self.logger.error("save_button is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def click_cancel_button(self):
        try:
            cancel_button = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.button_cancel_xpath)))
            assert cancel_button.text == "Cancel"
            self.logger.info("cancel_button is displayed")
            cancel_button.click()
            time.sleep(1)
        except Exception as e:
            self.logger.error("cancel_button is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def checkbox_create_login_details_on(self):
        checkbox_create_login_details = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.CLASS_NAME, "oxd-switch-input--active")))
        assert checkbox_create_login_details.is_displayed()
        self.logger.info("checkbox_create_login_details is displayed")

        try:
            if checkbox_create_login_details.is_displayed():
                checkbox_create_login_details.click()
                print("CLICK")
                time.sleep(1)
        except Exception as e:
            self.logger.error("checkbox is not displayed")
            raise Exception("Message: {}".format(str(e)))

    def input_first_name(self, first_name):
        try:
            input_first_name = WebDriverWait(self.driver, 5).until(
                ec.visibility_of_element_located((By.XPATH, self.input_first_name_xpath)))
            assert input_first_name.is_displayed()
            input_first_name.send_keys(first_name)
            self.logger.info("first_name is displayed")
        except Exception as e:
            self.logger.error("first_name is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def input_middle_name(self, middle_name):
        try:
            input_middle_name = WebDriverWait(self.driver, 5).until(
                ec.visibility_of_element_located((By.XPATH, self.input_middle_name_xpath)))
            assert input_middle_name.is_displayed()
            input_middle_name.send_keys(middle_name)
            self.logger.info("input_middle_name is displayed")
        except Exception as e:
            self.logger.error("first_name is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def input_last_name(self, last_name):
        try:
            input_last_name = WebDriverWait(self.driver, 5).until(
                ec.visibility_of_element_located((By.XPATH, self.input_lastname_xpath)))
            assert input_last_name.is_displayed()
            input_last_name.send_keys(last_name)
            self.logger.info("input_last_name is displayed")
        except Exception as e:
            self.logger.error("first_name is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

    def input_employee_id(self, input_employee_id):
        try:
            label_employee_id_xpath = self.driver.find_element(By.XPATH, self.label_employee_id_xpath)
            employee_id_active = self.driver.find_element(
                locate_with(By.XPATH, "//input[@class='oxd-input oxd-input--active']").below(label_employee_id_xpath))
            employee_id_active.click()
            act = ActionChains(self.driver)
            act.double_click(employee_id_active).perform()
            act.key_down(Keys.DELETE)
            act.perform()
            employee_id_active.send_keys(input_employee_id)
            self.logger.info("employee_id_active is displayed")
        except Exception as e:
            self.logger.error("employee_id_active is not displayed", exc_info=True)
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

    def input_password_confirm(self, password_confirmed):
        try:
            label_confirm_password_xpath = WebDriverWait(self.driver, 20).until(
                ec.visibility_of_element_located((By.XPATH, self.label_confirm_password_xpath)))
            assert label_confirm_password_xpath.is_displayed()
            self.logger.info("label_confirm_password_xpath is displayed")
        except Exception as e:
            self.logger.error("label_confirm_password_xpath failed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        try:
            input_password_confirm = self.driver.find_element(
                locate_with(By.TAG_NAME, "input").below(label_confirm_password_xpath))
            self.logger.info("input_password_confirm is displayed")
        except Exception as e:
            self.logger.error("input_password_confirm is not displayed", exc_info=True)
            raise Exception("Message: {}".format(str(e)))

        input_password_confirm.send_keys(password_confirmed)
