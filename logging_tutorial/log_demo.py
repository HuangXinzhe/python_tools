import logging
from logging import getLogger, INFO
from concurrent_log_handler import ConcurrentRotatingFileHandler
import os

log = getLogger(__name__)
logfile = os.path.abspath("nhtai_service_embedding_bge.log")
formatter = logging.Formatter("%(asctime)s [nhtai_service_embedding_bge] %(levelname)-5s [%(trace_id)s] [%(threadName)s] [%(filename)s:%(lineno)d] %(message)s")
rotateHandler = ConcurrentRotatingFileHandler(logfile, "a", 50 * 1024 * 1024, 3)
rotateHandler.setFormatter(formatter)
log.addHandler(rotateHandler)
log.setLevel(INFO)

def log_something(mode, mes, trace_id="", extra=None):
    if extra is None:
        extra = {}
    extra["trace_id"] = trace_id

    if mode == "info":
        log.info(mes, extra=extra)
    elif mode == "error":
        log.error(mes, extra=extra)
    elif mode == "warning":
        log.warning(mes, extra=extra)
    elif mode == "debug":
        log.debug(mes, extra=extra)
    else:
        log.info(mes, extra=extra)
    

def log_info(msg, trace_id="", extra=None):
    log_something("info", msg, trace_id, extra)

def log_error(msg, trace_id="", extra=None):
    log_something("error", msg, trace_id, extra)
