import pytest
from selenium import webdriver

from page_object_pattern.ui_tests import config

browsers = {'browserstack': 'browserstack', "localhost": "firefox"}


class DriverManager(object):
    def __init__(self):
        self._instance = None

    def start(self, browser_type='browserstack', browserstack_type=None):

        """
        Webdriver instantiation method

        :param browser_type: of selected browser via commandline,
            in case of None pass browser will be runned all browsers from browsers dictionary
        :return: webdriver instance

        """

        if browser_type == 'firefox':
            self._instance = webdriver.Firefox()
        elif browser_type == 'browserstack':
            if not (config.USERNAME and config.BROWSERSTACK_KEY):
                raise Exception("Please provide your BrowserStack username and access key")
            else:
                self._instance = \
                    webdriver.Remote(
                        command_executor=config.COMMAND_EXECUTOR,
                        desired_capabilities=config.desired_cap.get(browserstack_type,
                                                                    config.desired_cap.get("firefox_OS10")))
        return self._instance.maximize_window()

    @property
    def instance(self):
        if not self._instance:
            self.start()
        return self._instance

    def stop(self):
        self._instance.quit()


def pytest_addoption(parser):
    """

    Register commandline options
      :param parser - commandline arg(e.g 'py.test --browser')

    """
    parser.addoption("--browser", default='',
                     type='choice', choices=sorted(browsers),
                     help="runs tests only for given browser")
    parser.addoption("--url", default='',
                     help="runs tests with specific url address")
    parser.addoption("--browserstack_type", default='',
                     help="specify browserstack OS and browser type")
    parser.addoption("--login", default='',
                     help="specify login name")
    parser.addoption("--password", default='',
                     help="specify password ")


@pytest.yield_fixture(scope="module", params=browsers.keys())
def browser(request):
    """

    :scope module - the scope for which this fixture is shared,
        one of 'function' (default). Has been selected module because of 'DriverManager' class instantiate
        and commandline args option pass via 'start' method
    :param request: an optional list of parameters
    :return: str of selected option(e.g py.test --browser=ff, will return 'firefox'),
        after this option pass in 'start()' method of 'DriverManager' class via BaseTest

    """
    selected = request.config.getoption('browser')
    if selected and selected != request.param:
        pytest.skip('browser {} selected in the command line'.format(selected))
    driver = browsers[request.param]
    yield driver


@pytest.yield_fixture(scope="module")
def url(request):
    """
    url as param can pass via tests

    """

    yield request.config.getoption("url")


@pytest.yield_fixture(scope="module")
def browserstack_type(request):
    """
    specify browser and OS to run on browserstack

    """
    yield request.config.getoption("browserstack_type")


@pytest.yield_fixture(scope="module")
def login(request):
    """
    Login field

    """

    yield request.config.getoption("login")


@pytest.yield_fixture(scope="module")
def password(request):
    """
    Password field

    """
    yield request.config.getoption("password")


@pytest.fixture(scope="module")
def driver():
    """
    DriverManager instantiation function

    :return: Instance of DriverManager

    PS: driver is visible across module
    """
    return DriverManager()
