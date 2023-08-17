"""
run

This module contains the primary function for QuickMerge. It assumes valid I/O.
While running, it logs performance metrics. All results are written to the 
output file.

Author: Rani Hinnawi
Date: 2023-08-22
"""
from sys import stderr
from typing import TextIO
from support.output_formatters import write_to_output
from support.performance import Performance


def run(input_file: TextIO, output_file: TextIO, debug=False):
    """
    Wrapper function for running Quicksort and Natural Merge Sort using input
    file data, then writing results and performance metrics to output file.

    Args:
        input_file (TextIO): text file with string items to sort
        output_file (TextIO): text file where results are written
        debug (bool): True if debug mode is toggled on, otherwise False
    """
    # Set up Performance object and output strings used by runner functions
    performance = Performance()
    out = []

    with open(input_file, 'r', encoding="utf-8") as inputs:
        out.append("\n\n-------Sorting Results-------\n")
        line_counter = 1
        # TODO: replace for-loop with cleaner way to read individual records
        for line in inputs:
            expression = line.strip()
            size = len(expression)

            if size == 0:
                # Case: empty line. Ignore.
                continue

            # Set up error handling and performance metrics
            error = False
            result = ""
            performance.set_size(size).start()

            try:
                result = print(expression)
            except ValueError as ve:
                result = ve.args[0]
                error = True

                if debug:
                    error_message = f"Expression: {expression}"
                    error_message += f"\n\tError Message: {result}"
                    print(error_message, file=stderr)
            finally:
                performance.stop()

                if error:
                    performance.log_error()
                else:
                    performance.log_success()

                line_counter += 1

    # Display conversion values
    out.append("\nSorted values: ")

    # Output results
    write_to_output(output_file, out)

    if debug:
        print('OK', file=stderr)
