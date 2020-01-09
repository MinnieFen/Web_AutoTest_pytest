# coding:utf-8
from Base.DriverBase import DriverBase
import unittest
class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = DriverBase().open_broswer()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()