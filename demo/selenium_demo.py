'''
@File : selenium_demo.py
@Author : liruichuan
@Date: 2019/11/20
@Desc: selenium demo 模拟点击和滑动的动作
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def _seleep(int):
    time.sleep(int)

#谷歌浏览器
browser = webdriver.Firefox()
#访问百度
browser.get('https://www.baidu.com/')
print("已经打开百度，现在将浏览器设置为最大化")
browser.maximize_window()

btn_name = browser.find_element_by_id('su').get_attribute("value")
print("按钮名称：",btn_name)

#字符前面加u 保持utf-8编码不变
#设置搜索关键字 并提交
browser.find_element_by_id('kw').send_keys(u'python')
browser.find_element_by_id('su').submit()

print(browser.find_element_by_id('kw').get_attribute('type'))
print(browser.find_element_by_id('kw').size) #打印输入框的大小
time.sleep(3)

print('现在我将设置浏览器为宽480，高800显示')
browser.set_window_size(480,800)
browser.get('http://m.mail.10086.cn')
time.sleep(3)

print("返回上一个页面")
browser.forward()
time.sleep(5)

print("现在我们打开淘宝")
browser.get("https://www.taobao.com/")
browser.find_element_by_xpath(".//*[@id='q']").send_keys(u'裤子')
browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[1]/div[2]/form/div[1]/button").click()
time.sleep(5)
# 将滚动条移动到页面的底部
js = "var q=document.documentElement.scrollTop=100000"
browser.execute_script(js)
time.sleep(3)
# 将滚动条移动到页面的顶部
js = "var q=document.documentElement.scrollTop=0"
browser.execute_script(js)
time.sleep(3)
browser.quit()