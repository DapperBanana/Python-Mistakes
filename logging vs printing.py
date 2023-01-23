import logging

def print_errors():
    print("debug info")
    print("random info")
    print("this is a bad error")

#----------------------------------------

def log_errors():
    logging.debug("debug info")
    logging.info("just some info")
    logging.error("this is a bad error")

def main():
    level = logging.DEBUG
    fmt = '[%(levelname)s] %(asctime)s = %(message)s'
    logging.basicConfig(level=level, format=fmt)

#instead of printing out everything, we can use a more robust logging method in order to accurately track all of the info we're needing to. This also allows us to filter based on a type of message