import logging

# 向日志输出变量
logging.basicConfig(level=logging.DEBUG)


name = "Tom"
age = 18
logging.debug(f"姓名{name}，年龄{age}")

"""
输出结果：
DEBUG:root:姓名Tom，年龄18

DEBUG表示日志级别
root表示日志器的名称
"""