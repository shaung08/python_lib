import logging

class logger:
    def __init__(self, handler, type_) -> None:
        self.logger = logging.getLogger("django_log")
        self.level = self.logging_type(type_)
        self.set_log_level()
        self.set_handler(handler)
    def logging_type(self, type_):
        if type_ == "debug":
            return logging.DEBUG
        elif type_ == "info":
            return logging.INFO
        elif type_ == "warning":
            return logging.WARNING
        elif type_ == "error":
            return logging.ERROR
    def set_handler(self, handler):
        if handler=="stream":
            ch = logging.StreamHandler()
            ch.setLevel(self.level)
        else:
            # from datetime import datetime
            # ch = logging.FileHandler("log_"+str(datetime.now().strftime("%H:%M:%S")))
            ch = logging.FileHandler("django_log")
            ch.setLevel(self.level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
    def set_log_level(self):
        self.logger.setLevel(self.level)
    def log_msg(self, type_, msg):
        self.logger.log(self.logging_type(type_), msg)
