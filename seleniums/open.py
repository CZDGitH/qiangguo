# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/7/11 15:06
# @Author : chenzhida
# @Email : zhida.chen@huafeng-cn.com
# @File : open.py
# @Software: PyCharm

import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        time.sleep(60) # 改为60s
        is_login = chrome.find_element_by_xpath('//*[@id="root"]/div/div/section/div/div/div/div/div[4]/section/div[4]')
        print(is_login)
        if is_login:
            is_login.click()
            # 阅读文章
            time.sleep(10)
            # 跳转页面
            windows = chrome.window_handles
            chrome.switch_to.window(windows[-1])

            read_article = chrome.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[2]/div')
            read_article.click()
            # 跳转页面
            windows = chrome.window_handles
            chrome.switch_to.window(windows[-1])
            # 打开文章目录
            open_list = chrome.find_element_by_xpath('//*[@id="25fa"]/div/div/div/div/div/div/div[1]/span/div')
            open_list.click()
            # 跳转页面
            windows = chrome.window_handles
            chrome.switch_to.window(windows[-1])
            time.sleep(3)
            for i in range(18):
                article = chrome.find_element_by_xpath('//*[@id="root"]/div/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div[3]/section/div/div/div/div/div/section/div/div/div[1]/div/div['+str(i+1)+']/div/div/div[2]/span')
                article.click()
                time.sleep(3)
                # 跳转页面
                windows = chrome.window_handles
                chrome.switch_to.window(windows[-1])
                # 视听学习
                listen_and_read = chrome.find_element_by_xpath('//*[@id="root"]/div/section/div/div/div/div/div[2]/section/div/div/div/div/div/div/div[3]/div[1]/div[1]/audio')
                # listen_and_read.click()
                listen_and_read.send_keys(Keys.SPACE)
                for temp in range(5, 3, -1):
                    height = 'window.scrollTo(0,document.body.scrollHeight/' + str(temp) + ')'
                    chrome.execute_script(height)
                    time.sleep(60)
                # chrome.close()
                windows = chrome.window_handles
                chrome.switch_to.window(windows[3])
        #     视频
            movie_1 = chrome.find_element_by_xpath('//*[@id="root"]/div/header/div[2]/div[1]/div[2]/a[2]')
            movie_1.click()
            time.sleep(3)
            # 跳转页面
            windows = chrome.window_handles
            chrome.switch_to.window(windows[-1])
            movie_2 = chrome.find_element_by_xpath('//*[@id="00c8"]/div/div/div/div/div/div/div[2]/img')
            movie_2.click()
            time.sleep(3)
            # 跳转页面
            windows = chrome.window_handles
            chrome.switch_to.window(windows[-1])
            for i in range(4):
                for j in range(4):
                    movie_3 = chrome.find_element_by_xpath('//*[@id="1novbsbi47k-5"]/div/div/div/div/div/div/section/div[3]/section/div/div/div[1]/div['+str(i+1)+']/div['+str(j+1)+']/section/div/div/div/div/div[1]/div/div/span/div')
                    movie_3.click()
                    time.sleep(3)
                    # 跳转页面
                    windows = chrome.window_handles
                    chrome.switch_to.window(windows[-1])
                    for temp in range(5,0,-1):
                        height = 'window.scrollTo(0,document.body.scrollHeight/'+str(temp)+')'
                        chrome.execute_script(height)
                        time.sleep(3)
                    windows = chrome.window_handles
                    chrome.switch_to.window(windows[-2-j-i*4])
            news = chrome.find_element_by_xpath('//*[@id="0454"]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[5]/div/div')
            news.click()
            time.sleep(5)
            news_1 = chrome.find_element_by_xpath('//*[@id="17th9fq5c7l-5"]/div/div/div/div/div/div/section/div[3]/section/div/div/div[1]/div[1]/div[1]/section/div/div/div/div/div[1]/div/div/span/div')
            news_1.click()
            # 跳转页面
            windows = chrome.window_handles
            chrome.switch_to.window(windows[-1])
            for temp in range(5, 3, -1):
                height = 'window.scrollTo(0,document.body.scrollHeight/' + str(temp) + ')'
                chrome.execute_script(height)
                time.sleep(3)
        time.sleep(60*3*6)
        chrome.quit()  # 退出

if __name__ == '__main__':
    open()
