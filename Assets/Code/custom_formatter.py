class CustomFormatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: RESET + "%(asctime)s - %(message)s" + RESET,
        logging.INFO: "%(asctime)s - %(message)s" + RESET,
        logging.WARNING: BOLD + "%(asctime)s - %(message)s" + RESET,
        logging.ERROR: FAIL + "%(asctime)s - %(message)s" + RESET,
        logging.CRITICAL: BOLD + FAIL + "%(asctime)s - %(message)s" + RESET,
    }
