"""
run

This module contains the primary function for QuickMerge. It assumes valid I/O.
While running, it logs performance metrics. All results are written to the 
output file.

Author: Rani Hinnawi
Date: 2023-08-22
"""
from typing import TextIO

def run(input_file: TextIO, output_file: TextIO):
    """
    Wrapper function for running Quicksort and Natural Merge Sort using input
    file data, then writing results and performance metrics to output file.

    Args:
        input_file (TextIO): text file with string items to sort
        output_file (TextIO): text file where results are written
        debug (bool): True if debug mode is toggled on, otherwise False
    """
    with open(input_file, "r", encoding="utf-8") as inputs, open(output_file, "w", encoding="utf-8") as out:
        for line in inputs:
            print(line.split())
            out.write(str(line.split()))
    print("OK")
