#!/usr/bin/python3

import logging

def main():

    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler("example.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    logger.addHandler(fh)

    logger.info("Program started")
    logger.info("Done!")

if __name__ == "__main__":
    main()