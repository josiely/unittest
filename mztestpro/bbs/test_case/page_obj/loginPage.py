#date:2018/1/4
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from mztestpro.bbs.test_case.page_obj.base import Page
from time import sleep

class login(Page):
    """
    用户登录界面
    """
    url = '/'

    # Action
    bbs_login_user_loc = (By.XPATH, "//div[@id='mzcust']/div/img")
    bbs_login_button_loc = (By.ID, 'mzLogin')

    def bbs_login(self):
        self.find_element(*self.bbs_login_user_loc).click()
        sleep(1)
        self.find_element(*self.bbs_login_button_loc).click()

    login_username_loc = (By.ID, "account")
    login_password_loc = (By.ID, "password")
    login_button_loc = (By.ID, "login")

    # 登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    # 登录密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_password_loc).click()

    # 定义统一登录入口
    def user_login(self, username="uname", password="111"):
        """
        获取的用户名密码登录
        :param username:
        :param password:
        :return:
        """
        self.open()
        self.bbs_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    user_err_hint_loc = (By.XPATH, "//span[@for='account']")
    pwd_err_hint_loc = (By.XPATH, "//span[@for='password']")
    user_login_success_loc = (By.ID, "mzCustName")

    # 用户名错误提示
    def user_err_hint(self):
        return self.find_element(*self.user_err_hint_loc).text

    # 密码错误提示
    def pwd_err_hint(self):
        return self.find_element(*self.pwd_err_hint_loc).text

    # 登录成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text

