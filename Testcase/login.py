#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
import sys
import fire
import logging
sys.path.append('Testcase')
reload(sys)
sys.setdefaultencoding("UTF-8")


# 判断是否成功，成功为0，失败为1
def judge_fail_num(number):
    if number == 0:
        return True


# 测试用例中的测试步骤
def open_web_ui_test(statistics_list, web_browser):

    step = u"打开dm党建云平台"
    main_info = u"通过ip访问党建云平台"
    browser = web_browser
    try:
        browser.get("http://192.168.1.106/front-djy-web/login")
        time.sleep(3)
        browser.find_element_by_xpath("//*[@id=\"userName\"]")
        failnum = 0
    except Exception as e:
        browser.get_screenshot_as_file(main_info+".png")
        logging.exception(e)
        failnum = 1

    statistics_list.append((step, main_info, failnum))
    return failnum


# 测试用例中的测试步骤
def click_register_ui_test(statistics_list, web_browser):
    step = u"登录账户"
    main_info = u"登录测试账号"
    click_browser = web_browser
    try:
        click_browser.find_element_by_xpath("//*[@id=\"userName\"]").send_keys("guojun")
        click_browser.find_element_by_xpath("//*[@id=\"password\"]").send_keys("css12345")
        time.sleep(2)
        click_browser.find_element_by_xpath("//*[@id=\"loginEle\"]").click()
        time.sleep(6)
        click_browser.find_element_by_xpath("//*[@id=\"tab-mainPage\"]")
        register_failnum = 0
    except Exception as e:
        click_browser.get_screenshot_as_file(main_info + ".png")
        logging.exception(e)
        register_failnum = 1

    statistics_list.append((step, main_info, register_failnum))
    return register_failnum


def ui_test(browser):
    scene = "登录"
    html_list = []
    if browser == "chrome":
        test_browser = webdriver.Chrome()
    elif browser == "firefox":
        test_browser = webdriver.Firefox()
    elif browser == "ie":
        test_browser = webdriver.ie()
    test_case1_list = [open_web_ui_test, click_register_ui_test]
    num = 0
    while num < len(test_case1_list):
        test_num = test_case1_list[num](html_list, test_browser)

        if judge_fail_num(test_num):
            print "continue"
        else:
            break
        num = num + 1
    return scene, html_list


if __name__ == "__main__":
    fire.Fire(ui_test)
