from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import selenium.common
import logging
import sys

from page_object_pattern.ui_tests.config import UI_MAX_RESPONSE_TIME, TEST_URL

logging.basicConfig(level=logging.INFO)


class BasePage(object):
    """

    Base class to initialize the base page that will be called from all pages

    """

    def __init__(self, driver):
        self.driver = driver.instance
        self.wait = WebDriverWait(
            self.driver,
            UI_MAX_RESPONSE_TIME,
            ignored_exceptions=selenium.common.exceptions.WebDriverException
        )

    @property
    def log(self):
        logger = logging.getLogger(self.__class__.__name__ + "." + sys._getframe(1).f_code.co_name)
        return logger

    def navigate_to_url(self, url):
        """

        @param url: passing url via tests if it's none take default link form config
        @return: current url of load page
        """
        if url:
            self.log.info("Have been taken url from commandline: {}".format(url))
            self.driver.get(url)
        else:
            self.log.info("Have been taken 'url' from config file: {}".format(TEST_URL))
            self.driver.get(TEST_URL)
        return self.driver.current_url

    def switch_to_default_content(self):
        return self.driver.switch_to.default_content()

    def window_handler(self, handler):
        """
            Browser windows switcher

        @param handler: last available window web element
        @return: browser tab to be switched
        """
        windows_now = self.driver.window_handles
        if windows_now == 1:
            return windows_now[-1]
        window_to_switch = set(windows_now) - set(handler)
        needed_window = list(window_to_switch)
        self.driver.switch_to.window(needed_window[-1])
        if self.body_page:
            return self.driver.current_url

    def switch_to_admin_toolbar(self):
        """
            'i'frame' locator should be once used for one browser instance

        @return: bool
        """
        if self.body_page:
            return self.wait.until(ec.frame_to_be_available_and_switch_to_it((By.TAG_NAME, 'iframe')),
                                   "Unable to locate iframe")

    def wait_for_elements_by_xpath(self, element, message):
        """
            wait until web element/elements appears in DOM with delay of 0,5 second,
            in case if elements/element is visible returns web element/elements else throws exception
        @param element: XPATH
        @param message: Assertion message
        @return: web element/elements
        """
        return self.wait.until(
            ec.presence_of_all_elements_located((By.XPATH, element)), message)

    def wait_for_elements_by_class_name(self, element, message):
        """
            wait until web element/elements appears in DOM with delay of 0,5 second,
            in case if elements/element is visible returns web element/elements else throws exception
        @param element: CLASS NAME
        @param message: Assertion message
        @return: web element/elements
        """
        return self.wait.until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, element)), message)

    def wait_for_elements_by_tag_name(self, element, message):
        """
            wait until web element/elements appears in DOM with delay of 0,5 second,
            in case if elements/element is visible returns web element/elements else throws exception
            @param element: TAG NAME
            @param message: Assertion message
            @return: web element/elements
        """
        return self.wait.until(
            ec.presence_of_all_elements_located((By.TAG_NAME, element)), message)

    def wait_for_elements_by_id(self, element, message):
        """
            wait until web element/elements appears in DOM with delay of 0,5 second,
            in case if elements/element is visible returns web element/elements else throws exception
            @param element: ID
            @param message: Assertion message
            @return: web element/elements
        """
        return self.wait.until(
            ec.presence_of_all_elements_located((By.ID, element)), message)

    def wait_until_element_visible_by_xpath(self, element, message):
        """
            wait until web element/elements is visible
            @param element: XPATH
            @param message: Assertion message
            @return: web element/elements else False
        """
        return self.wait.until(
            ec.visibility_of_element_located((By.XPATH, element)), message)

    def wait_until_element_visible_by_id(self, element, message):
        """
            wait until web element/elements if visible with delay 0,5 second by default
            @param element: ID
            @param message: Assertion message
            @return: web element/elements else False
        """
        return self.wait.until(
            ec.visibility_of_element_located((By.ID, element)), message)

    def wait_until_element_visible_by_tag(self, element, message):
        """
            wait until web element/elements if visible with delay 0,5 second by default
            @param element: TAG_NAME
            @param message: Assertion message
            @return: web element/elements else False
        """
        return self.wait.until(
            ec.visibility_of_element_located((By.TAG_NAME, element)), message)

    def wait_until_element_visible_by_class_name(self, element, message):
        """
            wait until web element/elements if visible with delay 0,5 second by default
            @param element: CLASS_NAME
            @param message: Assertion message
            @return: web element/elements else False
        """
        return self.wait.until(
            ec.visibility_of_element_located((By.CLASS_NAME, element)), message)

    def wait_until_not_visible_element_by_xpath(self, element, message):
        """
            wait until web element/elements if invisible with delay 0,5 second by default
            @param element: XPATH
            @param message: Assertion message
            @return: web element/elements else False
        """
        return self.wait.until(
            ec.invisibility_of_element_located((By.XPATH, element)), message)

    def is_alert_visible(self):
        """
            Verifies firing alerts

        @return: bool
        """
        try:
            alert = self.wait.until(ec.alert_is_present())
            alert.accept()
            return True
        except TimeoutException:
            return False

    @property
    def body_page(self):
        """
            Checks body-html loading

        @return: html body web element
        """
        return self.wait_for_elements_by_tag_name('body', "Unable to locate body")
