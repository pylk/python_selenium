import logging,os,time
from Config import GlobalConfig
log_path = GlobalConfig.log_path
class UserLog():
    """
    日志等级描述：(从低到高)
    debug：最详细的日志信息，典型应用场景是 问题诊断
    info:信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作
    warmming:当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的
    error:由于一个更严重的问题导致某些功能不能正常运行时记录的信息
    critical:当发生严重错误，导致应用程序不能继续运行时记录的信息
    """
    def __init__(self):
        #实例化logger
        self.logger = logging.getLogger(__name__)
        self.logger.handlers = []
        self.logger.removeHandler(self.logger.handlers)
        if not self.logger.handlers:
            #设置日志格级别水平,info 以上级别的日志才会输出
            self.logger.setLevel(logging.DEBUG)
            #定义格式
            fmt = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s > %(lineno)d > %(levelname)s：%(message)s")
            #设置日志文件的名称
            self.logfilename = os.path.join(log_path,"{0}.log".format(time.strftime("%Y-%m-%d")))

            #控制日志文件日志输出
            self.file_handle = logging.FileHandler(self.logfilename,encoding="utf-8")
            self.file_handle.setFormatter(fmt)
            self.file_handle.setLevel(logging.DEBUG)

            #logger添加handler
            self.logger.addHandler(self.file_handle)


    def get_log(self):
        return self.logger

    # def close_handle(self):
    #     self.logger.removeHandler(self.file_handle)
    #     self.file_handle.close()


if __name__ == '__main__':

    ll = UserLog(filelevel=logging.DEBUG)
    ll.get_log().info("你好k")
