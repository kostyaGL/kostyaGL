from page_object_pattern.ui_tests.pages.base_page import BasePage


class NameOfPageWrapper(BasePage):
    def some_method_one(self):
        """
        self.driver is available, it's a good place for test logic
        :return:
        """
        self.driver.get('https://www.google.com.ua')

    def some_method_two(self):
        pass
