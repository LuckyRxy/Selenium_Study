# todo: selenium框架学习
#
# @Time: 2024/12/16 20:21:06
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

class TestBaseCase(unittest.TestCase):
    
    def setUp(self):
        """
        @todo: 设置驱动路径，加快selenium的启动速度
        @return: 
        """
        self.service = ChromeService(executable_path=r"D:\drivers\browers_drivers\chromedriver-win64\chromedriver.exe")
        pass


    @unittest.skip("暂时跳过")
    def test_chrome_driver(self):
        """
        @todo: selenium测试chrome浏览器
        @return: 
        """
        browser = webdriver.Chrome(service=self.service)
        browser.get("https://www.baidu.com")
        print("当前页面的标题是：", browser.title)
        print("当前相应的url：", browser.current_url)
        print("当前相应的page_source:", browser.page_source)
        print("当前浏览器的驱动名称：",browser.name)

        time.sleep(10)
        browser.close()
        
        pass
    
    @unittest.skip("暂时跳过")
    def test_attr_methods(self):
        """
        @todo: 测试selenium中的属性和方法
        @return: 
        """
        browser = webdriver.Chrome(service=self.service)
        
        # 获取浏览器名称
        print(browser.name)

        # 访问百度首页，暂时不使用https
        browser.get("http://www.baidu.com")
        # 获取响应对应的url
        print(browser.current_url)
        # 获取当前页标题
        print(browser.title)
        # 获取当前网页的源码长度
        print(len(browser.page_source))

        # 休息2秒，跳转到豆瓣首页,这里的两秒是等当前页面加载完毕，也就是浏览器转完圈后等待的两秒
        time.sleep(2)
        browser.get("https://www.douban.com")

        # 等待2秒钟返回百度
        time.sleep(2)
        browser.back()

        # 等待2秒钟再返回豆瓣
        time.sleep(2)
        browser.forward()

        # 等待2秒钟再刷新页面
        time.sleep(2)
        browser.refresh()

        # 保存当前页面截屏快照
        browser.save_screenshot('./images/screenshot.png')

        # 关闭当前标签页
        browser.close()

        # 关闭浏览器，释放进程
        browser.quit()
        pass
    
    @unittest.skip("暂时跳过")
    def test_element_id(self):
        """
        @todo: 通过id定位元素，测试输入框的输入和点击
        @return: 
        """
        # 实例化浏览器对象
        browser = webdriver.Chrome(service=self.service)
        # 打开百度首页
        browser.get("https://ww.baidu.com")
        # 输入关键字内容sora，并赋值给标签的id属性名来定位，这是新的写法
        browser.find_element(by=By.ID, value='kw').send_keys('sora')
        # 点击搜索按钮
        browser.find_element(by=By.ID,value='su').click()
        # 获取搜索结果
        # 关闭浏览器
        time.sleep(2)
        browser.quit()
        pass
    
    @unittest.skip("暂时跳过")
    def test_element_class_name(self):
        """
        @todo: 通过class_name定位元素，测试输入框的输入和点击 
        @return: 
        """
        browser = webdriver.Chrome(service=self.service)
        browser.get("https://www.baidu.com")
        #使用class_name定位输入框，并把输入框的内容设置为sora
        browser.find_element(by=By.CLASS_NAME,value="s_ipt").send_keys("sora")
        browser.find_element(by=By.CLASS_NAME,value='s_btn').click()
        time.sleep(5)
        browser.quit()
        pass
    
    @unittest.skip("暂时跳过")
    def test_element_xpath (self):
        """
        @todo: 通过xpath定位元素，测试输入框的输入和点击
        @return: 
        """
        # 实例化浏览器对象
        browser = webdriver.Chrome(service=self.service)
        browser.get("https://www.baidu.com")
        # 使用xpath定位输入框，并把输入框中的内容设置为sora
        browser.find_element(by=By.XPATH,value='//*[@id="kw"]').send_keys('sora')
        # 点击搜索按钮
        browser.find_element(by=By.XPATH,value='//*[@id="su"]').click()

        #关闭浏览器
        time.sleep(5)
        browser.quit()
        pass


    def test_element_css_selector(self):
        """
        @todo: 通过css选择器定位元素，测试输入框的输入与点击
        @return: 
        """

        # 实例化浏览器对象
        browser = webdriver.Chrome(service=self.service)
        browser.get("https://www.baidu.com")
        # 使用css选择器定位输入框，先进行清空文本框，并把输入框的内容设置为sora
        browser.find_element(by=By.CSS_SELECTOR, value="#kw").clear()
        browser.find_element(by=By.CSS_SELECTOR, value="#kw").send_keys('sora')
        browser.find_element(by=By.CSS_SELECTOR, value="#su").click()

        #关闭浏览器
        time.sleep(4)
        browser.quit()

        pass

    @unittest.skip("暂时跳过")
    def test_element_xpath(self):
        """
        @todo: 通过xpath定位元素列表，测试获取列表的数据
        @return: 
        """
        browser = webdriver.Chrome(service=self.service)
        browser.get("https://fund.eastmoney.com/data/fundranking.html#tall")
        # 使用xpath定位列表
        elements = browser.find_elements(by=By.XPATH,value='//table[@id="dbtable"]/tbody/tr/td[3]/a')

        for elem in elements:
            print(elem.text)

        # 页面加载完成后，再等待2秒，自动关闭浏览器，这里没有使用quit()方法，也能自动释放
        time.sleep(2)
        browser.quit()
        pass
    
    @unittest.skip("暂时跳过")
    def test_op_element(self):
        """
        @todo: 测试获取元素的文本内容
        @return: 
        """
        # 实例化浏览器对象
        browser = webdriver.Chrome(service=self.service)
        # 天天基金网，查看所有基金，这只是测试，不作为正式的爬虫
        browser.get('https://fund.eastmoney.com/data/fundranking.html#tall')

        # 使用xpath定位元素列表,基金代码
        elems = browser.find_elements(by=By.XPATH, value='//table[@id="dbtable"]/tbody/tr/td[3]/a')
        for elem in elems:
            print(elem.text)
            print(elem.get_attribute('href'))

        time.sleep(5)
        browser.quit()
        pass
    
    @unittest.skip("暂时跳过")
    def test_element_css_selector(self):
        """
        @todo: 通过css选择器定位元素，测试输入框的输入和点击
        @return:
        """
        # 实例化浏览器对象,打开百度首页
        browser = webdriver.Chrome(service=self.service)
        browser.get('https://www.baidu.com')
        # 使用css选择器定位输入框,先进行清空文本框，并把输入框的内容设置为sora
        browser.find_element(by=By.CSS_SELECTOR, value="#kw").clear()
        browser.find_element(by=By.CSS_SELECTOR, value="#kw").send_keys('sora')
        browser.find_element(by=By.CSS_SELECTOR, value="#su").click()
        # 关闭浏览器
        time.sleep(2)
        browser.quit()
        pass


    def test_headless_driver(self):
        """
        @todo: 测试chrome无头浏览器
        @return: 
        """
        # 配置信息
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        browser = webdriver.Chrome(service=self.service,options=chrome_options)
        browser.get('https://www.baidu.com')
        # 查看当前页面url
        print(browser.current_url)
        # 获取页面标题
        print("页面标题：", browser.title)
        # 获取渲染后的页面源码
        print("页面源码-长度：", len(browser.page_source))
        # 获取页面cookie
        print("cookie-data", browser.get_cookies())

        # 关闭页面的标签页
        browser.close()

        time.sleep(5)

        # 关闭浏览器
        browser.quit()

        pass


if __name__ == "__main__":
    unittest.main()