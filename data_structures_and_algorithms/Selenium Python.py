# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: Selenium Python.py
@time: 2023/3/13 19:02
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.kujiale.com")
driver.ex
driver.add_cookie()
# assert "Python" in driver.title
# elem = driver.
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
