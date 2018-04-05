#date:2018/1/4
from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from mztestpro.bbs.test_case.models import myunit, function
from mztestpro.bbs.test_case.page_obj.loginPage import login

class loginTest(myunit.MyTest):
    """  社区登录测试 """
    # 测试用户登录
    def user_login_verify(self, username="", password=""):
        login(self.driver).user_login(username, password)

    def test_login1(self):
        """ 用户名、密码为空登录 """
        self.user_login_verify()
        po = login(self.driver)
        self.assertEqual(po.user_err_hint(), "账号不能为空")
        self.assertEqual(po.pwd_err_hint(), "密码不能为空")
        function.insert_img(self.driver, "user_pwd_empty.png")

    def test_loin2(self):
        """ 用户名正确，密码为空 """
        self.user_login_verify(username="pytest")
        po = login(self.driver)
        self.assertEqual(po.pwd_err_hint(), "密码不能为空")
        function.insert_img(self.driver, "pwd_empty.png")

    def test_login3(self):
        """ 用户名为空，密码正确 """
        self.user_login_verify(password="abc123456")
        po = login(self.driver)
        self.assertEqual(po.user_err_hint(), "用户名不能为空")
        function.insert_img(self.driver, "user_empty.png")

    def test_login4(self):
        """ 用户名与密码不匹配 """
        character = random.choice("fjeoirip3[irnciaughdu")
        username = "zhangsan" + character
        self.user_login_verify(username=username, password="1234")
        po = login(self.driver)
        self.assertEqual(po.pwd_err_hint(),"密码与账号不匹配")
        function.insert_img(self.driver, "user_pwd_err.png")

    def test_login5(self):
        """ 用户名、密码正确 """
        self.user_login_verify(username="zhangsan", password="1234")
        sleep(2)
        po = login(self.driver)
        self.assertEqual(po.user_login_success(), "张三")
        function.insert_img(self.driver, "user_pwd_true.png")

if __name__ == "__main__":
    unittest.main()
