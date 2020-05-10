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





# 读取本次需要执行的场景
def get_scene_from_json(scenes):
    scene_list = []
    scene = scenes.split(",")
    with open("testcase.txt", "rb") as f:
        scene_dict = json.load(f)
        for i in scene:
            if i in scene_dict.keys():
                scene_list.append(scene_dict[i.decode("utf-8")])
    # print scene_list
    return scene_list






# 发送邮件
def send_html_mail(test_case, fail_num, mail_list, browser):
    output_file = write_html.write_whole_html_file(test_case, fail_num, mail_list, browser)
    # send_mail.send_mail_to_group(output_file)


# 执行汇总
def ui_test(browser, test_case, scene):
    html_list = []
    if browser == "chrome":
        test_browser = webdriver.Chrome()
    elif browser == "firefox":
        test_browser = webdriver.Firefox()
    elif browser == "ie":
        test_browser = webdriver.ie()
    test_case1_list = test_case
    # test_case1_list = [open_web_ui_test, click_register_ui_test, get_into_lesson, add_meeting]
    num = 0
    while num < len(test_case1_list):
        test_num = test_case1_list[num](html_list, test_browser)

        if judge_fail_num(test_num):
            print "continue"
        else:
            break
        num = num + 1

    send_html_mail(scene, test_num, html_list, browser)


def test(scene, test_browser):
    scene_list = get_scene_from_json(scene)
    for num in scene_list:
        os.system("python Testcase/"+num+" "+test_browser)
        print num


if __name__ == "__main__":
    # test_list = [open_web_ui_test, click_register_ui_test, get_into_lesson, add_meeting]
    scene = "三会一课,登录"
    # scene_list = get_scene_from_json(scene)

    test_browser = "firefox"
    test(scene, test_browser)
    # ui_test(browser=test_browser, test_case=test_list, scene=scene)
    # fire.Fire(ui_test)





