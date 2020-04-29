#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from pyh2 import*
import send_mail
import write_html
import time
import sys
reload(sys)
sys.setdefaultencoding("UTF-8")
'''
__author__ == junguo
__time__ == 2019/6/25 20:24
__detail__ == 处理ui的文件
'''


# 转换时间 将s转换成ms
def trans_time(origin_time):
    _time = ('%.2f' % (origin_time*1000))
    response_time = str(_time)+"ms"
    return response_time


def judge_fail_num(number):
    if number == 0:
        return True


def open_web_ui_test(statistics_list, web_browser):
    step = u"打开平台"
    main_info = u"通过域名访问aiui平台"
    browser = web_browser
    browser.get("http://aiui.xfyun.cn")
    # 打点计开始时间
    time_start = time.time()
    my_use = browser.find_element_by_link_text(u"我的应用")
    # 判断是否存在我的应用
    if my_use:
        # 结束时间
        time_end = time.time()
        open_web_time = time_end - time_start
        # 算响应时间
        open_response_time = trans_time(open_web_time)
        failnum = 0
    else:
        failnum = 1
        open_response_time = "Step Failed "

    statistics_list.append((step, main_info, failnum, open_response_time))
    return failnum


def click_register_ui_test(statistics_list, web_browser):
    step = u"注册账户"
    main_info = u"点击注册按钮"
    click_browser = web_browser
    click_browser.find_element_by_xpath("//*[@id='__layout']/div/div[1]/div/div[3]/div/a[2]/div").click()
    # 打点计开始时间
    register_time_start = time.time()
    iflyos_icon = click_browser.find_elements_by_link_text("iFLYOS")
    if iflyos_icon:
        # 结束时间
        register_time_end = time.time()
        register_time = register_time_end - register_time_start
        # 算响应时间
        register_response_time = trans_time(register_time)
        register_failnum = 0
    else:
        register_failnum = 1
        register_response_time = "Step Failed "
    statistics_list.append((step, main_info, register_failnum, register_response_time))
    return register_failnum


if __name__ == "__main__":
    html_file = PyH('iflyOS web report')
    html_table = html_file << table(border="2", cellpadding="2", cellspacing="0")
    html_list = []

    test_browser = webdriver.Chrome()
    Testcase = u"打开aiui平台"
    open_num = open_web_ui_test(html_list, test_browser)
    if judge_fail_num(open_num):
        register_num = click_register_ui_test(html_list, test_browser)
        if judge_fail_num(register_num):
            num = 0
            page, new_table = write_html.write_title(Testcase, num, html_file, html_table)
            for item in html_list:
                html_table = write_html.write_table_title(html_table)
                html_table = write_html.write_html(item[0], item[1], item[2], item[3], html_table)
        else:
            num = 1
            print "llll"
            page, new_table = write_html.write_title(Testcase, num, html_file, html_table)
            for item in html_list:
                html_table = write_html.write_table_title(html_table)
                html_table = write_html.write_html(item[0], item[1], item[2], item[3], html_table)

    else:
        num = 1
        page, new_table = write_html.write_title(Testcase, num, html_file, html_table)
        for item in html_list:
            html_table = write_html.write_table_title(html_table)
            html_table = write_html.write_html(item[0], item[1], item[2], item[3], html_table)

    output_file = "junguo.html"
    page.printOut(output_file)
    # send_mail.send_mail_to_group(output_file)
