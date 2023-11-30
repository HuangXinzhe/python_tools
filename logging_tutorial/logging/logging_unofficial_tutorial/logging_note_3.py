import logging


def log_testing():
    selflogger = logging.getLogger('THIS-LOGGING')  # 定义一个日志器，定义不同的日志器，方便区分不同的日志信息
    logging.basicConfig(filename='log.txt',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s-%(funcName)s',
                        level=logging.ERROR)
    selflogger.warning('waring，用来用来打印警告信息')
    selflogger.error('error，一般用来打印一些错误信息')
    selflogger.critical('critical，用来打印一些致命的错误信息，等级最高')


if __name__ == '__main__':
    log_testing()
