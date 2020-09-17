from Base.base import Base
from Page.pageElements import PageElements


class LoginPage(Base):
    """登录类"""

    def __init__(self):
        super().__init__()  # 初始化方法

    def login(self, name, pwd, code):
        """登录方法"""
        # 输入用户名
        self.send_ele(PageElements.tp_login_name, name)
        # 输入密码
        self.send_ele(PageElements.tp_login_passward, pwd)
        # 输入验证码
        self.send_ele(PageElements.tp_login_code, code)
        # 点击登录
        self.click_ele(PageElements.tp_login_enter)

    def close_tp(self):
        """关闭页面"""
        self.click_ele(PageElements.tp_close)
