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
    scenes = scenes.replace("\"", "")
    scene = scenes.split(",")

    with open("testcase.txt", "rb") as f:
        scene_dict = json.load(f)
        print scene_dict
        for i in scene:
            for _key in scene_dict.keys():
                if i == _key:
                    scene_list.append(scene_dict[i.decode("utf-8")])
    print scene_list
    return scene_list


def test(scene, test_browser):
    scene_list = get_scene_from_json(scene)
    for num in scene_list:
        os.system("python Testcase/"+num+" "+test_browser)
        print num


if __name__ == "__main__":
    # test_list = [open_web_ui_test, click_register_ui_test, get_into_lesson, add_meeting]
    # ui_test(browser=test_browser, test_case=test_list, scene=scene)
    fire.Fire(test)





