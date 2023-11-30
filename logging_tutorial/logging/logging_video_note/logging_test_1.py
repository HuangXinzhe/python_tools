import logging

# 默认的日志输出级别是warning
# 使用baseConfig()方法可以设置日志输出级别

logging.basicConfig(filename='demo.log', filemode='w', level=logging.DEBUG)

logging.debug("this is a debug log")
logging.info("this is a info log")
logging.warning("this is a warning log")
logging.error("this is a error log")
logging.critical("this is a critical log")
