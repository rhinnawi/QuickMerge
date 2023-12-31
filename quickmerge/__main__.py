"""
__main__

This is the entry point for the QuickMerge package. It runs when explicity 
called and not by default when the package is imported. It can be called by the
command: 
python -m quickmerge input_file output_file [...optional arguments]

The primary functionality lies in the package modules, and not directly in the
main module here.

Author: Rani Hinnawi
Date: 2023-08-22
"""
from sys import stderr
from pathlib import Path
import argparse
from support.is_valid_io import is_valid_io
from quickmerge.run import run

DEFAULT_FREQUENCY_TABLE_PATH = "hencoding/DefaultFreqTable.txt"

# Set up command line argument parsing
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input_file", type=str, help="Input file pathname")
arg_parser.add_argument("output_file", type=str, help="Output file pathname")
arg_parser.add_argument("--debug", action="store_true",
                        help="Toggles debug mode to log errors to stderr")
args = arg_parser.parse_args()

# Convert file names into paths
in_file = Path(args.input_file)
out_file = Path(args.output_file)

# Validate file paths then run main program
try:
    is_valid_io(in_file, out_file)
    run(in_file, out_file)
except FileNotFoundError as fnfe:
    error_message = fnfe.args[0]
    if args.debug:
        print(error_message, file=stderr)
