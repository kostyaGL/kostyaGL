# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import sqlite3
import sys

class RozetkaSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_rozetka_ua(self):

        driver = self.driver
        driver.implicitly_wait(10)
        driver.get("http://rozetka.com.ua/")
        self.assertIn('ROZETKA',driver.title)
        elem = driver.find_element_by_name("text")
        elem.send_keys("apple")
        assert "No results found." not in driver.page_source
        elem.send_keys(Keys.RETURN)

        links = driver.find_elements_by_xpath("//div[@class='search-result-goods']/*/div[@class='g-i-list-right-part']/div[@class='g-i-list-title']/a")
        #number = int(raw_input("Choose link : "))
        n = [l.get_attribute("href") for l in links][0]
        driver.get(n)

        prefer_link = driver.find_element_by_xpath("//ul[@class='m-tabs']//li[@name='characteristics']/a")
        driver.get(prefer_link.get_attribute("href"))

        characteristic_title = driver.find_element_by_xpath("//div[@class='detail-tab']/div/*")

        characteristic_title_i = driver.find_elements_by_xpath("//div[@class='detail-tab-characteristics']//div[@class='detail-tab-characteristics-i-title']")
        characteristics_i_field = driver.find_elements_by_xpath("//div[@class='detail-tab-characteristics']//div[@class='detail-tab-characteristics-i-field']")

        data = [i.text for i in characteristic_title_i]
        val =[j.text for j in characteristics_i_field]

        con = sqlite3.connect('learn.db')
        s = con.cursor()
        print len(data)
        with con:
            for i in range(len(data)):
                s.execute("INSERT INTO COMPANY(ID, Data, Val) VALUES ('%d', '%s', '%s')" % (i, data[i], val[i]))
        for i in s.execute('SELECT * FROM COMPANY'):
            print i
        s.close()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(RozetkaSearch)
    unittest.TextTestRunner().run(suite)