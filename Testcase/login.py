#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver
# from pyh2 import*
# import send_mail
import write_html
import json
import os
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

    step = u"打开cec党建云平台"
    main_info = u"通过域名访问党建云平台"
    browser = web_browser
    try:
        browser.get("http://10.2.57.30/front-djy-web/login")
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
        click_browser.find_element_by_xpath("//*[@id=\"userName\"]").send_keys("csdy")
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


def send_html_mail(file_name, test_case, fail_num, mail_list, browser):
    output_file = write_html.write_whole_html_file(file_name, test_case, fail_num, mail_list, browser)


def ui_test(browser):
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
    # return html_list
    scene = "登录"
    send_html_mail("test2", scene, test_num, html_list, browser)


if __name__ == "__main__":
    fire.Fire(ui_test)