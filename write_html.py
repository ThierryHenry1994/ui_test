# encoding: utf-8
import sys
import arrow
import os
import shutil
from pyh2 import*
reload(sys)
sys.setdefaultencoding("utf-8")
# 灰色背景色调
gray_background_color = "#AAAAAA"
# 白色背景色调
white_background_color = "#F7F7F7"


# 写表头
def write_title(test_case, fail_num, html_page, table):

    if fail_num == 0:
        failture = "是 "
    else:
        failture = "否"
    page = html_page
    html_table = table
    headtr = html_table << tr(id='headline')
    headtr << th('&nbsp;&nbsp;djy WEB UI TEST&nbsp;&nbsp;', colspan="7", align='center', bgColor=gray_background_color,
                 style="color:#000;font-family:Microsoft Yahei;")
    tr1 = html_table << tr()
    tr1 << td(u"项目名称", colspan="2", align='center', bgColor=gray_background_color,
              style="color:#000;font-family:Microsoft Yahei;font-weight:normal")
    tr1 << td(u"用例模块", colspan="2", align='center', bgColor=gray_background_color,
              style="color:#000;font-family:Microsoft Yahei;font-weight:normal")
    tr1 << td(u"执行时间", colspan="2", align='center', bgColor=gray_background_color,
              style="color:#000;font-family:Microsoft Yahei;font-weight:normal")
    tr1 << td(u"是否通过", colspan="2", align='center', bgColor=gray_background_color,
              style="color:#000;font-family:Microsoft Yahei;font-weight:normal")
    tr2 = html_table << tr()
    now_time = arrow.now().format("YYYY-MM-DD HH:mm:ss ZZ")
    tr2 << td(u'党建云测试', colspan="2", align='center', bgColor=white_background_color,
              style="color:#000;font-family:Microsoft Yahei;font-weight:normal")
    tr2 << td(test_case, colspan="2", align='center', bgColor=white_background_color,
              style="color:#000;font-family:Microsoft Yahei;font-weight:normal")
    tr2 << td(now_time, colspan="2", align='center', bgColor=white_background_color,
              style="color:#000;font-family:Microsoft Yahei;font-weight:normal")
    tr2 << td(failture, colspan="2", align='center', bgColor=white_background_color,
              style="color:#000;font-family:Microsoft Yahei;font-weight:normal")

    tr3 = html_table << tr()
    tr3 << td(u"具体测试步骤执行情况", colspan="8", align='center', bgColor=gray_background_color,
              style="color:#000;font-family:Microsoft Yahei;font-weight:normal")

    # print page

    return page, table


# 测试用例的表头
def write_table_title(title_table):
    _tr = title_table << tr()
    _tr << td(u'测试用例', colspan="2", align='center', bgColor=gray_background_color,
              style="color:#000;font-family:Microsoft Yahei;font-weight:normal")
    _tr << td(u'主要操作', colspan="3", align='center', bgColor=gray_background_color,
              style="color:#000;font-family:Microsoft Yahei;font-weight:normal")
    _tr << td(u'是否通过', colspan="2", align='center', bgColor=gray_background_color,
              style="color:#000;font-family:Microsoft Yahei;font-weight:normal")
    return title_table


# 基于测试步骤的结果写表格的内容
def write_html(step, main_info, failnum, content_table):
    if failnum == 0:
        failture = "是"
    else:
        failture = "否"
    _tr = content_table << tr()
    _tr << td(step, colspan="2", align='center', bgColor=white_background_color,
              style="color:#000;font-family:Microsoft Yahei;font-weight:normal")
    _tr << td(main_info, colspan="3", align='center', bgColor=white_background_color,
              style="color:#000;font-family:Microsoft Yahei;font-weight:normal")
    _tr << td(failture, colspan="2", align='center', bgColor=white_background_color,
              style="color:#000;font-family:Microsoft Yahei;font-weight:normal")
    return content_table


def judge_file_path_exist(path):
    if os.path.exists(path):
        pass
    else:
        os.mkdir("html_file")


# 写整个html文件
def write_whole_html_file(Testcase, fail_num, result_list):
    html_file = PyH('TEST webUI report')
    html_table = html_file << table(border="2", cellpadding="2", cellspacing="0")
    write_title(Testcase, fail_num, html_file, html_table)
    for result in result_list:
        write_table_title(html_table)
        write_html(result[0], result[1], result[2], html_table)
    # 判断是否存在存放html的文件夹
    # judge_file_path_exist("html_file")
    nowtime = arrow.utcnow().timestamp
    output_file = "ui_test.html"
    if os.path.exists(output_file):
        os.remove(output_file)
    html_file.printOut(output_file)
    # shutil.move(output_file, "html_file")
    # new_file = os.path.join("html_file", output_file)
    return html_file




