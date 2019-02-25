from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self,driver):
        self.driver=driver

    def click(self,clo):
        self.find_element(clo).click()

    def search_input(self, clo,text):
        self.find_element(clo).send_keys(text)

    # 自定义一个 find_element方法
    def find_element(self, clo):
        by=clo[0]
        value=clo[1]
        if by==By.XPATH: # 是xpath，调用封装好的代码
            self.make_xpath_feature(value)
        # 增加显示等待
        return  WebDriverWait(self.driver,5,1).until(lambda x:x.find_element(by,value))

    # 自己封装的方法
    def find_elements(self, clo):
        by=clo[0]
        value=clo[1]
        if by==By.XPATH:
            self.make_xpath_feature(value)
        # 增加显示等待
        return  WebDriverWait(self.driver,5,1).until(lambda x:x.find_elements(by,value))

    # 对xpath 部分进行封装
    def make_xpath_midle_feature(loc):
        # 拼接xpath中间的部分
        args = loc.split(",")
        feature = " "
        index0 = 0  # 为了代码规范，而定义的活变量
        index1 = 1
        index2 = 2
        if len(args) == 2:
            feature = "contains(@" + args[index0] + ",'" + args[index1] + "')" + "and"
        elif len(args) == 3:
            if args[index2] == "1":
                feature = "@" + args[index0] + "='" + args[index1] + "'" + "and"
            elif args[index2] == "0":
                feature = "contains(@" + args[index0] + ",'" + args[index1] + "')" + "and"
        return feature

    def make_xpath_feature(self,loc):
        feature_start = "//*["
        feature_end = "]"
        feature = " "

        if isinstance(loc, str):  # loc 是字符串
            # 如果是正常的xpath
            if loc.startswith("//"):
                return loc
            feature = self.make_xpath_midle_feature(loc)
        else:
            # loc 是列表
            for i in loc:
                feature += self.make_xpath_midle_feature(i)
        feature = feature.rstrip("and")  # 去掉尾部的and
        loc = feature_start + feature + feature_end
        return loc
