# todo: selenium模拟浏览器高级操作
#
# @Time: 2024/12/17 14:14:33
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com
import time
import unittest
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from utils.tools import Tools


class TestAdvancedCase(unittest.TestCase):
    def setUp(self):
        """
        @todo: 前置操作
        @return: 
        """
        # windows下的chromedriver路径
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
        # 验证 selenium网站是否有效
        self.url = 'https://bot.sannysoft.com/'
        # linux/macos环境
        # self.service = ChromService(executable_path="/usr/local/bin/chromedriver")
        # windows环境
        self.service = ChromeService(executable_path=r"D:\drivers\browers_drivers\chromedriver-win64\chromedriver.exe")

        pass
    
    @unittest.skip("暂时跳过")
    def test_selenium_valid(self):
        """
        @todo: 验证selenium是否被反爬
        @return: 
        """
        # 实例化配置项
        chrome_options = webdriver.ChromeOptions()
        # 设置无头模式
        chrome_options.add_argument("--headless")
        # 设置无显卡
        chrome_options.add_argument("--disable-gpu")
        # 实例化浏览器对象
        driver = webdriver.Chrome(service=self.service, options=chrome_options)

        # 发送请求,截图
        driver.get(self.url)
        driver.save_screenshot('./images/sannysoft_valid.png')
        print("截屏成功！")
        # 关闭浏览器
        driver.quit()
        pass

    @unittest.skip("暂时跳过")
    def test_stealth(self):
        """
        @todo: 主要为了隐藏 selenium 的指纹，不被网站给识别出来是机器人(即不被反爬)
        @return: 
        """
        # 配置实例化配置项
        chrome_options = webdriver.ChromeOptions()
        # 设置无头模式
        chrome_options.add_argument('--headless')
        # 设置无显卡
        chrome_options.add_argument('--disable-gpu')
        # 实例化浏览器对象
        driver = webdriver.Chrome(service=self.service, options=chrome_options)

        # 执行'stealth.min.js'文件进行隐藏浏览器指纹
        with open("stealth.min.js","r") as f:
            js = f.read()
        
        # 执行js代码
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source":js})
        # 发送请求
        driver.get(self.url)
        # 截图
        driver.save_screenshot("./images/sannysoft.png")
        print("消除指纹成功！")
        # 关闭浏览器
        driver.quit()
        pass

    @unittest.skip("暂时跳过")
    def test_label_switch(self):
        """
        @todo: 使用句柄切换标签页，同时隐藏指纹
        @todo: 句柄相当于是智能指针，来标识资源；而隐藏指纹是为了防止被反爬
        @return: 
        """

        # 声明浏览器驱动实例
        driver = webdriver.Chrome(service=self.service)
        # 执行反爬js代码，隐藏浏览器指纹
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": Tools.open_stealth_js()})

         # 进入58同城首页
        driver.get("https://hz.58.com/")

        # todo 获取当前所有的标签页的句柄构成的列表，这不能提前申明为变量，随着新便签页的打开，这是动态变化的
        # current_windows = driver.window_handles

        # 获取当前页
        print(driver.current_url)
        print(driver.window_handles)

        # 点击整租的链接，打开租房页面
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/span[2]/a").click()
        # todo 根据标签页句柄,将句柄切换到最新新打开的标签页，这一定要有，不然句柄不会变化，那么下一页内容取不到
        # driver.switch_to.window(driver.window_handles[-1])
        print(driver.current_url)
        print(driver.window_handles)


        elem_list = driver.find_elements(by=By.XPATH, value="/html/body/div[6]/div[2]/ul/li/div[2]/h2/a")
        # 统计租房列表的个数
        print(len(elem_list))

        time.sleep(5)
        driver.quit()
        pass

    @unittest.skip("暂时跳过")    
    def test_no_switchto_frame(self):
        # 声明浏览器驱动实例
        driver = webdriver.Chrome(service=self.service)
        # 打开 qzone 登录页
        driver.get("https://qzone.qq.com/")

        # 默认进来是采用扫码，我们这里需要切换成账号密码登录
        driver.find_element(by=By.ID, value="switcher_plogin").click()
        # 填写账号
        driver.find_element(by=By.ID, value="u").send_keys("1430183056@qq.com")
        # 并不是真实的密码
        driver.find_element(by=By.ID, value="p").send_keys("123456")
        # 点击登录按钮
        driver.find_element(by=By.XPATH, value='//*[@id="login_button"]').click()

        time.sleep(5)
        driver.quit()
        pass
    
    @unittest.skip("暂时跳过")    
    def test_switchto_frame(self):
        driver = webdriver.Chrome(service=self.service)
        driver.get("https://qzone.qq.com/")

        # 切入iframe
        driver.switch_to.frame("login_frame")

        driver.find_element(by=By.ID, value="switcher_plogin").click()
        driver.find_element(by=By.ID, value="u").send_keys("531881823.qq.com")
        driver.find_element(by=By.ID, value="p").send_keys("123456")
        driver.find_element(by=By.XPATH, value='//*[@id="login_button"]').click()

        time.sleep(5)
        driver.quit()
        pass
    
    
    def test_cookie(self):
        """
        @tode: 获取cookie
        @return:
        """
        driver = webdriver.Chrome(service=self.service)
        driver.get("https://baidu.com/")

        # 获取cookie的值
        cookie_info = {data["name"]: data["value"] for data in driver.get_cookies()}
        pprint(cookie_info)

        time.sleep(2)
        driver.quit()
        pass


    def test_page_wait(self):
        """
        @todo 隐式等待
        @return:
        """
        # 打开浏览器，进到百度首页
        driver = webdriver.Chrome(service=self.service)
        driver.get("https://www.baidu.com/")

        # 隐式等待，最大等待10秒
        driver.implicitly_wait(10)

        # 点击百度的logo图标的src 属性
        elem = driver.find_element(by=By.XPATH, value='//img[@id="s_lg_img_new"]')
        print(elem.get_attribute("src"))

        # 强制等待2秒
        time.sleep(2)
        driver.quit()
        pass

    
if __name__ == "__main__":

    unittest.main()
    