import logging
import logging.config

# 配置文件的方式来处理日志
logging.config.fileConfig('logging.conf')  # 读取配置文件
# 使用字典就能从任意格式文件进行配置，字典是一种接口格式
# logging.config.dictConfig({"loggers":"root,applog"})

rootLogger = logging.getLogger('root')  # 获取logger实例
rootLogger.debug("This is root Logger, debug")

logger = logging.getLogger('applog')
logger.info("This is applog Logger, info")


# 打印错误信息
a = "abc"
try:
    b = int(a)
except Exception as e:
    # logger.error(e)
    logger.exception(e)  # 打印错误信息

