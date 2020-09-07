import unittest
from selenium import webdriver
import time
 
# 创建测试类——继承unittest.TestCase
class TestSpace(unittest.TestCase):
 
    # 方法类别的处理器
    # 每个测试用例方法执行前执行
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(r'https://i.qq.com/')
 
    # 每个测试用例方法执行后执行
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
 
    # 创建测试用例（测试方法）
    # 方法名必须是test开头
    # 成功
    def test_login_success(self):
        self.driver.switch_to.frame('login_frame')
        self.driver.find_element_by_link_text('帐号密码登录').click()
        #账号：******
        self.driver.find_element_by_id('u').send_keys('******')
        #密码：******
        self.driver.find_element_by_id('p').send_keys('******')
        self.driver.find_element_by_id('login_button').click()
        text = self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/div[1]/a[1]/span').text
        #用户名：******
        username = '*******'
        self.assertIn(username,text)
 
    # 失败
    def test_login_fail(self):
        self.driver.switch_to.frame('login_frame')
        self.driver.find_element_by_link_text('帐号密码登录').click()
        #账号：******
        self.driver.find_element_by_id('u').send_keys('******')
        #密码：******
        self.driver.find_element_by_id('p').send_keys('******')
        self.driver.find_element_by_id('login_button').click()
        text = self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/div[1]/a[1]/span').text
        #用户名：******11
        username = '******11'
        self.assertIn(username,text)
 
    def test_lll(self):
        self.driver.switch_to.frame('login_frame')
        print('111')
