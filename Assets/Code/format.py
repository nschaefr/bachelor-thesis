def format(self, record):
    log_fmt = self.FORMATS.get(record.levelno)
    if "TEST COMPILATION SUCCESSFUL" in record.getMessage():
        log_fmt = SUCCESS + "%(asctime)s - %(message)s" + RESET
    formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
    return formatter.format(record)
