import logging

# 输出格式和添加一些公共信息
logging.basicConfig(format="%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    level=logging.DEBUG)


name = "Tom"
age = 18
logging.debug(f"姓名{name}，年龄{age}")