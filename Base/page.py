from Page.loginpage import LoginPage


class Page:
    @classmethod
    def get_login(cls):
        """返回登录类"""
        return LoginPage()


