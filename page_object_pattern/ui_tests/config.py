"""
   production url list of sites
   browser configuration

"""
TEST_URL = "http://google.com.ua"

# delay for wait until function
UI_MAX_RESPONSE_TIME = 25.0

# Browserstack credentials:
# USERNAME = 'xxxx', BROWSERSTACK_KEY = 'xxxxx'
USERNAME = 'USERNAME_browser-stack'
BROWSERSTACK_KEY = 'PASSWD_browser-stack'
COMMAND_EXECUTOR = 'browser-stack_command_executor'

# Browserstack parameters:
desired_cap = {'firefox_OS10': {'browser': 'Firefox',
                                'browser_version': '46.0',
                                'os': 'WINDOWS',
                                'os_version': '10',
                                'resolution': '2048x1536',
                                'browserstack.local': 'true',
                                'browserstack.selenium_version': "2.53.0",
                                'project': 'Test Panel Account Functional Tests'}
               }
