import logging


# 设置打印日志的级别，level级别以上的日志会打印出
# level=logging.DEBUG 、INFO 、WARNING、ERROR、CRITICAL
def log_testing():
    # 此处进行Logging.basicConfig() 设置，后面设置无效
    logging.basicConfig(level=logging.ERROR)  # 将level以上级别的日志输出，如不设置，默认为WARNING
    logging.debug('debug，用来打印一些调试信息，级别最低')
    logging.info('info，用来打印一些正常的操作信息')
    logging.warning('waring，用来用来打印警告信息')
    logging.error('error，一般用来打印一些错误信息')
    logging.critical('critical，用来打印一些致命的错误信息，等级最高')


if __name__ == '__main__':
    log_testing()
