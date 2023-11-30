import logging.config
import logging

def getLogging(confName="applog"):
    logging.config.fileConfig("logging.conf")
    return logging.getLogger(confName)
