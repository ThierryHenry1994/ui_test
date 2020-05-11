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
import imp
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


# 读取本次需要执行的场景
def get_scene_from_json(scenes):
    scene_list = []
    scenes = scenes.replace("\"", "")
    scene = scenes.split(",")
    for i in scene:
        scene_list.append(i.split("(")[0]+".py")

    print scene_list
    return scene_list


def test(scene, test_browser):
    scene_list = get_scene_from_json(scene)
    write_dict = {}
    for num in scene_list:
        model_name = "Testcase."+num.split(".")[0]
        model_path = "Testcase/"+num

        test_obj = imp.load_source(model_name, model_path)

        scene_name, html_list = test_obj.ui_test(test_browser)

        write_dict[scene_name] = html_list
    print write_dict
    write_html.write_whole_html_file(write_dict, test_browser)


if __name__ == "__main__":
    # test_list = [open_web_ui_test, click_register_ui_test, get_into_lesson, add_meeting]
    # ui_test(browser=test_browser, test_case=test_list, scene=scene)
    # fire.Fire(test)
    test("\"shyk(三会一课),login(登录)\"", "chrome")





