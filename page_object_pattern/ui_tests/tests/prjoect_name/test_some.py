from page_object_pattern.ui_tests import config
from page_object_pattern.ui_tests.pages.page_factory import Pages
from page_object_pattern.ui_tests.tests.base_test import BaseTest


class TestSome(BaseTest):
    """
        Test Step:
        ---------------
        Test summary

        1) Test steps

        Test Environment:
        ----------------
        - Selenium
        - pytest(pip install pytest)
        - pytest-html(pip install pytest-html)
        - Firefox
        - Windows 10
        - Browser stack

        How to run:
        -----------------
        py.test --browser=localhost --url=https://www.google.com/
        Expected Result:
        ----------------
        Some text :)

        [FAIL]
         -  some text as well :)
    """

    @staticmethod
    def get_home_page(driver):
        """
        Create instance of page
        :param driver: web-driver
        :return: instance
        """
        pages = Pages(driver)
        return pages.navigate_to.home_page()

    def test_get_url(self, driver, url):
        home_page = self.get_home_page(driver)
        get_test_panel_url = home_page.navigate_to_url(url)
        assert get_test_panel_url == url if url else config.TEST_URL, 'Incorrect url-address'
