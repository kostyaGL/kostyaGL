from page_object_pattern.ui_tests.pages.base_page import BasePage
from page_object_pattern.ui_tests.pages.some_page.page_wrapper import NameOfPageWrapper


class Pages(BasePage):
    """
    Initialization of page wrappers

    """

    def __init__(self, driver):
        super(Pages, self).__init__(driver)
        self.driver = driver

    @property
    def navigate_to(self):
        return PageWrappers(self.driver)


class PageWrappers(Pages):
    def __init__(self, driver):
        super(PageWrappers, self).__init__(driver)

    def home_page(self):
        return NameOfPageWrapper(self.driver)
