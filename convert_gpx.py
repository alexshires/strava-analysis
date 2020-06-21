"""
Python file to convert GPX and plot distributions
"""
import os
import pathlib
import logging
import argparse
from gpx_csv_converter import Converter

logger = logging.getLogger(__name__)
logger.setLevel(10)

INPUT_FILE = "data/strava/input1.gpx"
OUTPUT_FILE = ".output1.csv"

if __name__ == '__main__':
    logger.debug("running gpx analysis")
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, default=None)
    parser.add_argument("-o", "--output", type=str, default=None)
    options = parser.parse_args()
    data_dir = pathlib.Path.home() / "Documents" / "data" / "strava"
    input_file_path = data_dir / options.input
    output_file_path = data_dir / options.output
    logger.debug("converting %s to %s", input_file_path, output_file_path)
    Converter(input_file=input_file_path, output_file=output_file_path)
