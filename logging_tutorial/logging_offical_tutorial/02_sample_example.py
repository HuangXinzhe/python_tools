import logging

"""
默认级别为warning，所以只有warning和高于warning级别的日志会被打印出来
"""
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
