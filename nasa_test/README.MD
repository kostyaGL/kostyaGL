SHORT INTRODUCTION:
   nasa_test ->
            tests -> nasa_api       -> test
                     base_test/py
                     conftest.py
             wrappers -> nasa_wrapper -> wrapper.py
                         base_page.py

conftest file - it's need for configuration test infrastructure based on py.test(argrparse, collection of tests and so on)

base_test.py - contains BaseTest class for describing all common things for all tests

base_page.py - same story as base_test only for wrappers


Need to perform:
1. pip install -r requirements.txt
2. python -m pytest tests
