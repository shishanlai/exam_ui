from Base.page import Page
Page.get_login().login("admin","123456",8888)
assert Page.get_login().page_exits_text("系统后台")