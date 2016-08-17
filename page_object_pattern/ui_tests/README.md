This is an opinionated automation framework for use Pytest and WebDriver libraries.

Pre-requirements:
1. Python v2.7 (just google python :)).
If was installed python lower then v2.7.9 likely enough need to install pip manual
2. pytest == 2.8.7 or higher(pip install pytest==2.8.7)
3. pytest-html for generating html reports(pip install pytest-html). It's not mandatory.
4. selenium==2.53.3 (pip install selenium==2.53.3)
5. Download Firefox browser(for selenium v2.53.3 nice to use Firefox v46.0 or lower,
                            if you going to use some other firefox version need to familiarize with selenium
                            docs which indicates applicable browser version)
6. Download BrowserStackLocal.exe(win)/.bin(unix). Needed for running scripts remotely
    - https://www.browserstack.com/browserstack-local/BrowserStackLocal-linux-x64.zip(unix64)
    - https://www.browserstack.com/browserstack-local/BrowserStackLocal-win32.zip(Win x32 but it works normally even on x64)

How to understand what commandline args are available:
1. See conftest.py(located: test_panel_ui_tests -->> tests -->> conftest.py):
    - pytest_addoption method which reside all avalaible commandlines arguments

How to run:
1. Go to test_panel directory into tests:
    1.1 Run on localhost:
       - py.test --browser=localhost --url=http://google.com/
