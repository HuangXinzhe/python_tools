import logging


# 设置打印日志的级别，level级别以上的日志会打印出
# level=logging.DEBUG 、INFO 、WARNING、ERROR、CRITICAL
def log_testing():

    
    """
     1. 此处进行Logging.basicConfig() 设置，后面设置无效

     2. filemode是设置保存日志的文件参数，不设的话默认为'a'，即追加模式；也可以设为'w'，那么每次写日志会覆盖之前的日志。

     3. 将level以上级别的日志输出，如不设置，默认为WARNING
    """
    logging.basicConfig(filename='log.txt',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s-%(funcName)s',
                        level=logging.ERROR)
    logging.debug('debug，用来打印一些调试信息，级别最低')
    logging.info('info，用来打印一些正常的操作信息')
    logging.warning('waring，用来用来打印警告信息')
    logging.error('error，一般用来打印一些错误信息')
    logging.critical('critical，用来打印一些致命的错误信息，等级最高')


if __name__ == '__main__':
    log_testing()
    """
    2023-09-04 22:28:32,981 - root - ERROR - error，一般用来打印一些错误信息-log_testing
    2023-09-04 22:28:32,981 - root - CRITICAL - critical，用来打印一些致命的错误信息，等级最高-log_testing
    
    
    日志结果中出现root，是因为没有设置logger的名字，所以默认使用root。
    """
