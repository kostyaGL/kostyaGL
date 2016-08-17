import pytest
import logging
import sys
logging.basicConfig(level=logging.INFO)


class BaseTest(object):
    """
        Base class to initialize the base test class and driver

    """
    @pytest.fixture(scope="class", autouse=True)
    def manage_driver(self, request, driver, browser, browserstack_type):
        """
        Instantiate pre requirements and driver instance

        @param request: request object has TearUp/TearDown methods and so on things common for Unittest module
        @param driver: driver instance(Firefox ...)
        @param browser: type of browser selected via commandline "localhost' == 'firefox'(native selenium driver)
        @param browser-stack_type: type of browser and OS for browser-stack(e.g Firefox 46.0 and OS10). See config file.
        """
        driver.start(browser, browserstack_type)
        request.addfinalizer(driver.stop)

    @property
    def log(self):
        logger = logging.getLogger(self.__class__.__name__ + "." + sys._getframe(1).f_code.co_name)
        return logger
