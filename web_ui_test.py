#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from pyh2 import*
import send_mail
import write_html
import time
import sys
import fire
import logging
reload(sys)
sys.setdefaultencoding("UTF-8")
'''
__author__ == junguo
__time__ == 2019/6/25 20:24
__detail__ == 处理ui的文件
'''
gray_background_color = "#AAAAAA"
white_background_color = "#F7F7F7"


# 转换时间 将s转换成ms
def trans_time(origin_time):
    _time = ('%.2f' % (origin_time*1000))
    response_time = str(_time)+"ms"
    return response_time


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
        my_use = browser.find_element_by_xpath("//*[@id=\"userName\"]")
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


def get_into_lesson(statistics_list, web_browser):
    step = u"点击三会一课"
    main_info = u"进入三会一课详情列表"
    click_browser = web_browser
    try:
        click_browser.find_element_by_xpath("//*[@id=\"menuWrapper\"]/span[2]/span/span").click()
        time.sleep(4)
        click_browser.find_element_by_xpath("//dd[contains(text(),\"三会一课\")]").click()
        time.sleep(3)
        click_browser.find_element_by_xpath("//*[@id=\"worktab_1\"]/div[3]/div/div/div[1]/div[1]/button/span")
        register_failnum = 0
    except Exception as e:
        click_browser.get_screenshot_as_file(main_info + ".png")
        logging.exception(e)
        register_failnum = 1
    statistics_list.append((step, main_info, register_failnum))
    return register_failnum


def add_meeting(statistics_list, web_browser):
    step = u"新增三会一课"
    main_info = u"创建三会一课并补充相关内容"
    click_browser = web_browser
    try:
        click_browser.find_element_by_xpath("//*[@id=\"worktab_1\"]/div[3]/div/div/div[1]/div[1]/button/span").click()
        time.sleep(2)
        click_browser.find_element_by_xpath("//*[@id=\"worktab_1\"]/div[3]/div/div/form/div[1]/div/div/input").send_keys("test_meeting")
        time.sleep(2)
        click_browser.find_element_by_xpath("//*[@id=\"worktab_1\"]/div[3]/div/div/form/div[11]/div/div/div/div/div[2]/div[1]").send_keys("test_meeting")
        time.sleep(2)

        click_browser.find_element_by_xpath("//*[@id=\"worktab_1\"]/div[3]/div/div/form/div[14]/div/div/button[3]/span").click()
        click_browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/button[2]/span").click()
        time.sleep(6)
        click_browser.find_element_by_xpath("//span[contains(text(),\"test_meeting\")]")
        register_failnum = 0
    except Exception as e:
        click_browser.get_screenshot_as_file(main_info + ".png")
        logging.exception(e)
        register_failnum = 1
    statistics_list.append((step, main_info, register_failnum))
    return register_failnum


# 发送邮件
def send_html_mail(test_case, fail_num, mail_list):
    output_file = write_html.write_whole_html_file(test_case, fail_num, mail_list)
    # send_mail.send_mail_to_group(output_file)


# 执行汇总
def ui_test():
    html_list = []
    test_browser = webdriver.Chrome()
    # 大用例名称
    Testcase1 = u"打开党建云平台"
    # test_case1_list = [open_web_ui_test, click_register_ui_test]
    test_case1_list = [open_web_ui_test, click_register_ui_test, get_into_lesson, add_meeting]
    num = 0
    while num < len(test_case1_list):
        test_num = test_case1_list[num](html_list, test_browser)

        if judge_fail_num(test_num):
            print "continue"
        else:
            break
        num = num + 1

    send_html_mail(Testcase1, test_num, html_list)


if __name__ == "__main__":
    fire.Fire(ui_test)





