import logging


class logger():
    def __init__(self):
        pass

    def setup_logger(self, logger_name, log_file, level=logging.INFO):
        self.l = logging.getLogger(logger_name)
        self.formatter = logging.Formatter('%(asctime)s %(message)s')
        self.fileHandler = logging.FileHandler(log_file, mode='a')
        self.fileHandler.setFormatter(self.formatter)
        self.streamHandler = logging.StreamHandler()
        self.streamHandler.setFormatter(self.formatter)
        self.l.setLevel(level)
        self.l.addHandler(self.fileHandler)
        self.l.addHandler(self.streamHandler)

    def logger(self,name,filename):
        self.setup_logger(name,filename)
        logger = logging.getLogger(name)
        return logger