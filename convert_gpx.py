"""
Python file to convert GPX and plot distributions
"""
import os
import logging
import argparse
from gpx_csv_converter import Converter

logger = logging.getLogger(__name__)
logger.setLevel(10)

INPUT_FILE = "input1.gpx"
OUTPUT_FILE = "output1.csv"

if __name__ == '__main__':
    logger.debug("running gpx analysis")
    parser = argparse.ArgumentParser()
    options = parser.parse_args()
    Converter(input_file=INPUT_FILE, output_file=OUTPUT_FILE)
