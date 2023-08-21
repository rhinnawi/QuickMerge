"""
run_sort

This module contains the wrapper function for running a sorting algorithm. 
While running, it logs performance metrics. It also accounts for possible 
errors and incorporates them into output text. Output text is returned.

Author: Rani Hinnawi
Date: 2023-08-22
"""
from sys import stderr
from typing import List, Tuple
from support.output_formatters import format_sorted_results
from support.performance import Performance


def run_quicksort(line_number: int, records: List[int],
                  performance: "Performance", print_results=False, debug=False)\
        -> Tuple[bool, str]:
    """
    Runner function for passed-in sort type using inputted records list.
    Returns string fromatted for output.

    Args:
        line_number (int): number for labelling lines in the output
        records (List[int]): list of integer records to be sorted
        performance (Performance): Performance object for storing metrics
        print_sorted (bool): True if printing sorted results, otherwise False
        debug (bool): True if debug mode is toggled on, otherwise False

    Returns:
        bool: True if error returned, otherwise False
        str: output string
    """
    # Set up
    result = []
    error = False

    # Set up error handling and performance metrics
    performance.set_size(len(records)).start()

    try:
        result = records
    except ValueError as ve:
        # Ensure error message gets printed to output file
        result = ve.args[0].split()
        error = True
        print_results = True

        if debug:
            error_message = f"Records: {records[:80]}"
            error_message += f"\n\tError Message: {result}"
            print(error_message, file=stderr)
    finally:
        # Stop timer. Account for errors
        performance.stop()

        if error:
            performance.log_error()
        else:
            performance.log_success()

        if not print_results:
            result = []

    # Return formatted results
    return error, format_sorted_results(
        line_number, result, str(performance.get_runtime_micro_sec()), error)
