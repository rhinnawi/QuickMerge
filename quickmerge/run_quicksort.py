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
from quickmerge.quicksort import Quicksort
from support.output_formatters import format_sorted_results, format_logs
from support.performance import Performance


def run_quicksort(line_number: int, records: List[int],
                  insertion_threshold: int, performance: "Performance",
                  print_results=False, pivot_option="first", debug=False)\
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
    comparisons = []
    exchanges = []
    error = False
    quicksort = Quicksort(records, pivot_option, insertion_threshold)
    MAX_LOG_LENGTH = 100

    # Set up error handling and performance metrics
    performance.set_size(len(records)).start()

    try:
        result = quicksort.q_sort()
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

            # Convert back to regular Python list for output
            if not print_results:
                result = []
            else:
                comparisons = quicksort.get_comparisons()
                exchanges = quicksort.get_exchanges()

    # Cap comparison and exchange lists for readability
    if len(comparisons) > MAX_LOG_LENGTH:
        comparisons = comparisons[:MAX_LOG_LENGTH]
        comparisons.append("...")

    if len(exchanges) > MAX_LOG_LENGTH:
        exchanges = exchanges[:MAX_LOG_LENGTH]
        exchanges.append("...")

    # Set up and return output text
    output_text = format_sorted_results(
        line_number, result, str(performance.get_runtime_micro_sec()), error)

    output_text += f"\nPivot type: {pivot_option}"
    output_text += f"\nInsertion Sort Threshold: {insertion_threshold}"
    output_text += format_logs(comparisons, exchanges,
                               quicksort.get_num_comparisons(),
                               quicksort.get_num_exchanges())

    # Return formatted results
    return error, output_text
