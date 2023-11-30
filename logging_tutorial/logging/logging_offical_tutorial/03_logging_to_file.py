import argparse
import logging

"""
方式一
"""
# level默认是warning，若没有设置level
# logging.basicConfig(filename='example.log',level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')

"""
方式二
"""
# 可以在命令行中通过（--log=级别）来设置日志级别
# logging.basicConfig(filename='example.log')
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')


"""
方式三
"""
# # 创建解析器
# parser = argparse.ArgumentParser()
# # 添加 --log 参数
# parser.add_argument("--log", type=str, help="日志级别")
# # 解析命令行参数
# args = parser.parse_args()
# # 获取 --log 参数的值
# loglevel = args.log
# numeric_level = getattr(logging, loglevel.upper(), None)
# if not isinstance(numeric_level, int):
#     raise ValueError('Invalid log level: %s' % loglevel)
# logging.basicConfig(filename='example.log',level=numeric_level)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')


"""
多次运行
设置filemode='w'，会覆盖之前的日志
设置filemode='a'，会追加日志
"""
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)