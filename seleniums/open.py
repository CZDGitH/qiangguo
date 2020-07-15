# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/7/11 15:06
# @Author : chenzhida
# @Email : zhida.chen@huafeng-cn.com
# @File : open.py
# @Software: PyCharm
from selenium import webdriver
import time


def open():
    try:
        chrome_options = webdriver.ChromeOptions()
        # 代理IP,由快代理提供
        # proxy = '60.17.254.157:21222'
        # 设置代理
        # chrome_options.add_argument('--proxy-server=%s' % proxy)
        # chrome_options.add_argument('disable-infobars')
        # 注意options的参数用之前定义的chrome_options
        chrome_options.add_argument('--no-proxy-server')
        chrome = webdriver.Chrome(options=chrome_options)
        chrome.get('https://pc.xuexi.cn/points/login.html?ref=https%3A%2F%2Fwww.xuexi.cn%2F')
        time.sleep(3)
        chrome.switch_to.frame(chrome.find_element_by_xpath("// iframe[contains( @ id, 'ddlogin-iframe')]"))
        app = chrome.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div[1]/img')
        app_src = app.get_attribute('src')
        print(app_src)
        time.sleep(10)
        return app_src
    finally:
        # 判断是否登入
        time.sleep(10) # 改为60s
        is_login = chrome.find_element_by_xpath('//*[@id="root"]/div/div/section/div/div/div/div/div[4]/section/div[4]')
        print(is_login)
        if is_login:
            is_login.click()
            # 阅读文章
            time.sleep(10)
            # 跳转页面
            windows = chrome.window_handles
            chrome.switch_to.window(windows[-1])
            read_article = chrome.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div')
            read_article.click()
            # 跳转页面
            windows = chrome.window_handles
            chrome.switch_to.window(windows[-1])
            # 打开文章目录
            open_list = chrome.find_element_by_xpath('//*[@id="d6df"]/div/div/div/div/div/section/div/div/div/div/div[1]/div/div/span')
            open_list.click()
            # 跳转页面
            windows = chrome.window_handles
            chrome.switch_to.window(windows[-1])
            for i in range(7):
                article = chrome.find_element_by_xpath('//*[@id="root"]/div/div/section/div/div/div/div/div/section/div/div/div/div[1]/div/section/div/div/div/div/div/section/div/div/div/div/div[3]/section/div/div/div/div/div/section/div/div/div[1]/div/div['+str(i+1)+']/div/div/div[1]/span')
                article.click()
                time.sleep(3)
                # 跳转页面
                windows = chrome.window_handles
                chrome.switch_to.window(windows[-1])
                chrome.execute_script("window.scrollTo(0,document.body.scrollHeight/2)")
                time.sleep(3)
                chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(3)
                chrome.close()
                windows = chrome.window_handles
                chrome.switch_to.window(windows[-1])
            time.sleep(10)
        chrome.quit()  # 退出

if __name__ == '__main__':
    # test
    open()
