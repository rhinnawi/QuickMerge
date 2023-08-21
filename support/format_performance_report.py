"""
format_performance_report

This module contains helper functions called to format strings intended to be
outputted to a text file. It specifically holds a function for formatting the
performance report.

Author: Rani Hinnawi
Date: 2023-08-22
"""
from support.performance import Performance


def format_performance_report(metrics: 'Performance', micro_sec=False) -> str:
    """
    Function that formats the size and runtime data logged for each success and
    failure into a report. Runtimes are outputted by size in order from 
    smallest to largest.

    Args:
        metrics (Performance): Performance object with logged metrics data
        micro_sec (bool): True if saving runtime in microseconds, otherwise
            False

    Returns:
        str: logged successes and failures, formatted to suit a text file

    TODO: Update to have write be a List that is joined by \n
    """
    write = ["\n-------Performance Report-------\n"]

    # Note total number of successes and successes per size
    write.append(f"Total number of successes: {metrics.get_num_successes()}")

    successes = metrics.get_successes()
    for size in sorted(successes.keys()):
        runtimes = sorted(successes[size])

        if micro_sec:
            # If measurements are in micro-seconds, convert runtimes
            for i, time in enumerate(runtimes):
                time /= 1000
                runtimes[i] = int(time)

        write.append(str(runtimes))

    write.append("-")

    # Note total number of errors and errors per size
    write.append(f"Total number of errors: {metrics.get_num_errors()}")

    errors = metrics.get_errors()
    for size in sorted(errors.keys()):
        runtime = sorted(errors[size])

        if micro_sec:
            # If measurements are in micro-seconds, convert runtimes
            for i, time in enumerate(runtimes):
                time /= 1000
                runtimes[i] = int(time)

        write.append(str(runtime))

    write.append("\nFormat:\n\t[runtime1, ..., runtimeN]")
    footer = "\tNOTE: Runtimes measured in"

    if micro_sec:
        footer += " microseconds (μs)"
    else:
        footer += " nanoseconds (ns)"

    write.append(footer)

    return '\n'.join(write)
