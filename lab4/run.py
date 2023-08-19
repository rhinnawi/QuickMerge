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
from support.output_formatters import write_to_output, format_sorted_results, \
    format_original_records
from support.format_performance_report import format_performance_report
from support.performance import Performance


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
    records, error = parse_all_records(input_file)

    out.append("-------Quicksort and Natural Merge Sort Results-------\n")
    out.extend(format_original_records(records, error))

    if error:
        # Output results
        write_to_output(output_file, out)

        if debug:
            print('ERROR CAUGHT. SEE OUTPUT FILE.', file=stderr)

        return

    line_counter = 1
    # TODO: implement way to create full list by reading all lines and
    # concatenating records into one large list
    # TODO: set up loop to re-run sort multiple times but only print
    # sorted output the first time, performance multiple times
    size = len(records)

    # Set up error handling and performance metrics
    result = []
    performance.set_size(size).start()

    try:
        result = records
    except ValueError as ve:
        result = ve.args[0].split()
        error = True

        if debug:
            error_message = f"Records: {records[:80]}"
            error_message += f"\n\tError Message: {result}"
            print(error_message, file=stderr)
    finally:
        performance.stop()

        if error:
            performance.log_error()
        else:
            performance.log_success()

        out.append(format_sorted_results(
            line_counter, result, str(performance.get_runtime()), error))

        line_counter += 1

    # Output performance report
    out.append(format_performance_report(performance))

    # Output results
    write_to_output(output_file, out)

    if debug:
        print('OK', file=stderr)
