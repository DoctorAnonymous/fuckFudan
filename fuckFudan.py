from selenium import webdriver
import time
import ddddocr
from PIL import Image, ImageEnhance
import requests


def fuckFudan(username, password):
    try:

        browser = webdriver.Chrome()
        browser.get('https://zlapp.fudan.edu.cn/site/ncov/fudanIndex')
        if 'undefined' in browser.page_source:
            return('Error')
        time.sleep(2)
        # 登录
        browser.find_element_by_id('username').send_keys(username)
        browser.find_element_by_id('password').send_keys(password)
        browser.find_element_by_id('idcheckloginbtn').click()
    except:
        pass
    try:
        time.sleep(5)
        browser.find_element_by_css_selector('.tab.tab_wrap').click()
        time.sleep(5)
        browser.find_element_by_css_selector('.wapat-btn.wapat-btn-ok').click()
    except:
        browser.close()
        time.sleep(600)
        return(username)
        # 是否在校
    try:
        time.sleep(2)
        browser.find_element_by_name('sfzx').find_elements_by_tag_name('em')[2].click()
        time.sleep(2)
        browser.find_element_by_css_selector('.wapcf-btn.wapcf-btn-ok').click()
        time.sleep(2)
        browser.find_element_by_name('fxyy').send_keys('无')
    except:
        pass
        # 定位
    try:
        time.sleep(2)
        browser.find_element_by_name('area').click()
        time.sleep(2)
        browser.find_element_by_partial_link_text('提交').click()
        time.sleep(2)
        browser.find_element_by_css_selector('.wapcf-btn.wapcf-btn-ok').click()
        # 验证码
        time.sleep(2)
        browser.save_screenshot('test.png')
        Image.open("test.png").crop((397, 363, 512, 400)).save('test.png')
        with open('test.png', 'rb') as inputFile:
            code = ddddocr.DdddOcr().classification(inputFile.read())
        browser.find_element_by_class_name('wapat-title-input').find_element_by_tag_name('input').send_keys(code)
        browser.find_element_by_css_selector('.wapat-btn.wapat-btn-ok').click()
        time.sleep(3)
    except Exception as e:
        pass
    browser.close()
    time.sleep(0)
    return(fuckFudan(username, password))

