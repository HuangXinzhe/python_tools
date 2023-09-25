import logging
"""
    在消息中显示日期/时间
"""
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p')
logging.warning('is when this event was logged.')

"""
2023/09/20 06:37:15 PM is when this event was logged.
"""