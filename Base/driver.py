from appium import webdriver as app
from selenium import webdriver as web


class Driver:
    # 后台
    tp_login_driver = None
    @classmethod
    def get_mis_driver(cls):
        """声明自媒体驱动"""
        if cls.tp_login_driver is None:
            # chrome浏览器
            cls.tp_login_driver = web.Chrome()
            # 最大化
            cls.tp_login_driver.maximize_window()
            # 访问自媒体首页
            cls.tp_login_driver.get("http://tpshop-test.itheima.net/Admin/Admin/login")
        return cls.tp_login_driver

    @classmethod
    def quit_mis_driver(cls):
        """退出自媒体driver"""
        if cls.tp_login_driver:
            # 退出
            cls.tp_login_driver.quit()
            # 置为None
            cls.tp_login_driver = None
