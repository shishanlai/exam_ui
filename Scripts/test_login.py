from Base.driver import Driver
from Base.page import Page
from Base.data import Data
import pytest,time


def login_data1():
    # 空列表
    login_list = []
    for i in Data.get_json_data('login.json'):
        login_list.append((i.get("用户名"), i.get("密码"), i.get("验证码"), i.get("is_suc")))

    return login_list


class Test01:
    def teardown_class(self):
        Driver.quit_mis_driver()

    @pytest.mark.parametrize("name, pwd, code,is_suc", login_data1())
    def test_login(self, name, pwd, code, is_suc):
        Page.get_login().login(name, pwd, code)
        time.sleep(3)
        if is_suc:
            assert Page.get_login().page_exits_text("系统后台")
            # 点击退出
            Page.get_login().close_tp()
            time.sleep(10)
        else:
            assert Page.get_login().page_exits_text("账号密码不正确")
