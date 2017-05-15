import logging


def error_log(message):     #将日志写入不同的文件
    file_1_1 = logging.FileHandler('error.log', 'a+', encoding='utf-8')     #定义文件
    fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
    file_1_1.setFormatter(fmt)
    logger1 = logging.Logger('error', level=logging.ERROR)      #创建日志对象
    logger1.addHandler(file_1_1)        #日志对象和文件对象创建关系
    logger1.log(logging.FATAL,message)

def run_log(message):
    file_1_1 = logging.FileHandler('run.log', 'a+', encoding='utf-8')
    fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
    file_1_1.setFormatter(fmt)
    # 创建日志对象
    logger1 = logging.Logger('run', level=logging.ERROR)
    # 日志对象和文件对象创建关系
    logger1.addHandler(file_1_1)
    logger1.log(logging.FATAL, message)