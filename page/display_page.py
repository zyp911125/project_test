from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class DisplayPage(BaseAction):
    # 显示按钮
    display_button=By.XPATH,"//*[contains(@text,'显示')]"
    # 搜索按钮（点击放大镜）
    search_button=By.ID,"com.android.settings:id/search"
    # 搜索输入框
    input_text_viem=By.ID, "android:id/search_src_text"
    # 返回按钮
    back_button=By.CLASS_NAME,"android.widget.ImageButton"

    def __init__(self,driver):
        self.driver=driver
        BaseAction.__init__(self,driver) # 父类的初始化方法

    def click_display(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.find_element1(self.display_button).click()
        self.click(self.display_button)

    def click_search(self):
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.find_element1(self.search_button).click()
        self.click(self.search_button)

    def click_text(self,text):
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys(text)
        # self.find_element1(self.input_text_viem).send_keys(text)
        self.search_input(self.input_text_viem,text)

    def click_back(self):
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        # self.find_element1(self.back_button).click()
        self.click(self.back_button)



