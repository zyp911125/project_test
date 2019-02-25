import os, sys
import pytest
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.display_page import DisplayPage


class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.display_page = DisplayPage(self.driver)

    def teardown(self):
        self.driver.quit()



    def test_mobile_display_input(self):
        # 点击显示
        self.display_page.click_display()
        # 点击放大镜
        self.display_page.click_search()
        # 输入文字
        self.display_page.click_text("hello")
        # 点击返回
        self.display_page.click_back()


