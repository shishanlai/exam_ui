from selenium.webdriver.common.by import By


class PageElements:
    """页面元素类"""
    # 用户名
    tp_login_name = (By.NAME, 'username')
    # 密码
    tp_login_passward = (By.NAME, 'password')
    # 验证码
    tp_login_code = (By.NAME, 'vertify')
    # 登录
    tp_login_enter = (By.XPATH, '//input[@value="登录"]')

    #退出
    tp_close = (By.CLASS_NAME,"login-out")