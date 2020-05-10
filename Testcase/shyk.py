#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
import sys
import logging
reload(sys)
sys.setdefaultencoding("UTF-8")


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
        # 添加会议标题
        click_browser.find_element_by_xpath("//*[@id=\"worktab_1\"]/div[3]/div/div/form/div[1]/div/div/input").send_keys("test_meeting")
        time.sleep(2)
        # 添加会议地点
        click_browser.find_element_by_xpath("//*[@id=\"worktab_1\"]/div[3]/div/div/form/div[10]/div/div/div/div[1]/div/div/input").send_keys("test_meeting")
        time.sleep(2)
        # 添加补充说明
        click_browser.find_element_by_xpath("//*[@id=\"worktab_1\"]/div[3]/div/div/form/div[11]/div/div/input").send_keys("test_meeting")
        # 添加会议内容
        click_browser.find_element_by_xpath("//*[@id=\"worktab_1\"]/div[3]/div/div/form/div[12]/div/div/div/div/div[2]/div[1]").send_keys("test_meeting")
        # 点击发布按钮
        click_browser.find_element_by_xpath("//*[@id=\"worktab_1\"]/div[3]/div/div/form/div[15]/div/div/button[3]/span").click()
        # 点击确认按钮
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