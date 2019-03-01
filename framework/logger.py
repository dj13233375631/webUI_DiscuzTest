import logging
import os.path
import time

class Logger(object):
    def __init__(self,logger):

        self.logger = logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)

        rq = time.strftime("%Y%m%d%H%M" , time.localtime(time.time()))
        lj = os.path.dirname(os.path.abspath(".")) + "/logs/"
        name = lj + rq + ".log"

        fh = logging.FileHandler(name)
        fh.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def getlog(self):
        return self.logger




