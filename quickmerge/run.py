"""
run

This module contains the primary function for QuickMerge. It assumes valid I/O.
While running, it logs performance metrics. All results are written to the 
output file.

Author: Rani Hinnawi
Date: 2023-08-22
"""
from sys import stderr
from typing import TextIO, List, Union
from support.output_formatters import write_to_output, format_original_records
from support.format_performance_report import format_performance_report
from support.performance import Performance
from quickmerge.run_quicksort import run_quicksort
from quickmerge.run_n_merge_sort import run_n_merge_sort


def parse_all_records(input_file: TextIO) -> Union[List[int], bool]:
    """
    Helper function for retrieving all records from a data input file. This
    assumes multiple records spread across multiple lines. 

    Args:
        input_file (TextIO): text file with string items to sort

    Returns:
        List[int]: list of all records
        bool: True if ValueError raised else False

    Raises:
        ValueError: if a non-integer record is found
    """
    all_integers = []

    # Read each line in input file. Add records to output list
    with open(input_file, 'r', encoding="utf-8") as records:
        for line in records:
            line = line.strip()
            if line:
                # If empty line, skip to the next. Ensure records are integers
                try:
                    integers = [int(num) for num in line.split()]
                    all_integers.extend(integers)
                except ValueError as ve:
                    # If record cannot be cast as an int, it is invalid
                    error_message = [ve.args[0]]
                    return error_message, True

    return all_integers, False


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
    RUNS_PER_SORT = 5
    records, error = parse_all_records(input_file)
    print_results = len(records) <= 50

    out.append("-------Quicksort and Natural Merge Sort Results-------")
    if print_results:
        out.extend(format_original_records(records, error))
    else:
        out.append(f"Size: {len(records)} Records\n")

    if error:
        # Output results
        write_to_output(output_file, out)

        if debug:
            print('ERROR CAUGHT. SEE OUTPUT FILE.', file=stderr)

        return

    # Run Quicksort using specified settings
    out.append("\n-----Quicksort:")
    qs_settings = {
        "pivot": ["first", "first", "first", "median_of_three"],
        "insertion_threshold": [2, 100, 50, 2]}

    for line_number in range(1, RUNS_PER_SORT):
        i = line_number - 1
        error, result_text = run_quicksort(
            line_number, records, qs_settings["insertion_threshold"][i],
            performance, print_results, qs_settings["pivot"][i], debug)
        print_results = False

        out.append(result_text)
        if error:
            break

    # Run Natural Merge Sort
    out.append("\n-----Natural Merge Sort:")
    print_results = len(records) <= 50
    for line_number in range(1, RUNS_PER_SORT + 1):
        error, result_text = run_n_merge_sort(
            line_number, records, performance, print_results, debug)
        print_results = False

        out.append(result_text)
        if error:
            break

    # Output performance report
    out.append(format_performance_report(performance, micro_sec=True))

    # Output results
    write_to_output(output_file, out)

    if debug:
        print('OK', file=stderr)
