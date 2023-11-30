from get_logging import getLogging

logger = getLogging()

# 打印错误信息
a = "abc"
try:
    b = int(a)
except Exception as e:
    # logger.error(e)
    logger.exception(e)  # 打印错误信息
