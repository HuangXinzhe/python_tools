import logging

# 编程的方式来写一下高级的写法
# 记录器
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)  # 设置日志级别，低于此级别的日志不会被记录

# 处理器handler
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

# 没有给handler指定日志级别，将使用logger的级别
fileHandler = logging.FileHandler(filename='my.log', mode='w', encoding='utf-8')
fileHandler.setLevel(logging.INFO)

# formatter格式，可以设置多个格式（%()8s，表示占位8个字符，若有‘-’号则为左对齐）
formatter = logging.Formatter('%(asctime)s|%(levelname)8s|%(filename)20s:%(lineno)4s|%(message)s')

# 给处理器设置格式
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# 将处理器添加到记录器
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

# 定义一个过滤器
filter = logging.Filter('mylogger')  # 过滤记录器名称为mylogger的日志
# 给记录器添加过滤器
logger.addFilter(filter)

# 打印日志的代码
logger.debug("this is a debug log")
logger.info("this is a info log")
logger.warning("this is a warning log")
logger.error("this is a error log")
logger.critical("this is a critical log")
