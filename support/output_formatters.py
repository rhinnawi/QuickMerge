"""
output_formatters

This module contains helper functions called to format strings intended to be
outputted to a text file.

Author: Rani Hinnawi
Date: 2023-08-08
"""
from typing import TextIO, List, Tuple, Union


def write_to_output(output_file: TextIO, output_text: List[str]) -> None:
    """
    Helper function for writing to an output file the text from a list of
    result and formatting strings.

    Args:
        output_file (TextIO): file to which the results are written
        output_text (List[str]): list of results
    """
    with open(output_file, 'w', encoding="utf-8") as output:
        output.write('\n'.join(output_text))
        output.write("\nDone.")

    return


def break_string(expression: List[Union[str, int]], chars_per_line: int) \
        -> str:
    """
    Helper function for outputting a long string within user-defined length
    restrictions.

    Args:
        expression (str): string being broken into multiple lines
        chars_per_line (str): max length of substring per line

    Returns:
        str: formatted string
    """
    # Begin on new line with indentation
    lines = ["\t\t"]
    current_line = ""

    # Build up lines without cutting off terms
    for term in expression:
        term = str(term)
        if len(current_line) + len(term) + 1 <= chars_per_line:
            current_line += term + " "
        else:
            lines.append(current_line)
            current_line = term + " "

    # Add last line
    if current_line:
        lines.append(current_line)

    return "\n\t\t".join(lines)


def format_original_records(records: List[int], error=False, chars_per_line=80)\
        -> List[str]:
    """
    Function that formats the list of all inputted records

    Args:
    records (List[str]): original file records before being sorted
    error (bool): indicator of whether result is an error message
    chars_per_line (int): max width of lines in output file

    Returns:
        List[str]: conditionally formatted results
    """
    # Format header line with original expression
    prefix = "Original: "

    if error:
        # Indicate if records is actually an error
        prefix += "\n\tERROR - "

    # Format for output file and return
    expression = break_string(records, chars_per_line - len(prefix))
    write = [prefix + expression]
    write.append(f"Size: {len(records)} Records\n")
    return write


def format_sorted_results(line_number: int, result: List[Union[str, int]],
                          runtime: str, error=False, chars_per_line=80) -> str:
    """
    Function that formats the inputted expression and the output given from a
    sorting process.

    Args:
        line_number (int): number for labelling lines in the output
        result (List[str]): sorted records OR error message
        runtime (str): current process's runtime in μs
        error (bool): indicator of whether result is an error message
        chars_per_line (int): max width of lines in output file

    Returns:
        str: conditionally formatted results
    """
    # Format and append result with error  handling
    output_text = f"\n{line_number}. "

    if len(result) > 0:
        # Add to output text if results are being added to the output
        output_text += "\tError - " if error else "\tSorted: "
        output_text += break_string(result, chars_per_line - len(output_text))
        output_text += '\n'

    # Add metrics and return
    output_text += f"Runtime: {runtime}μs"
    return output_text


def format_logs(comparisons: List[Tuple[int, int]],
                exchanges: List[Tuple[int, int]], num_comparisons: int,
                num_exchanges: int, chars_per_line=80) -> str:
    """
    Function that formats the comparisons and exchanges logged

    Args:
        comparisons (List[Tuple[int, int]]): tuples of comparisons logged
        exchanges (List[Tuple[int, int]]): tuples of exchanges logged
        num_comparisons (int): number of comparisons logged
        num_exchanges (int): number of exchanges logged
        chars_per_line (int): max width of lines in output file

    Returns:
        str: conditionally formatted results
    """
    # Format and append result with error  handling
    output_text = [f"\nComparisons: {num_comparisons}",
                   f"Exchanges: {num_exchanges}"]

    if len(comparisons) > 0:
        # Add to output text if comparisons are being added to the output
        prefix = "All Comparisons:"
        output_text.append(prefix + break_string(comparisons,
                                                 chars_per_line - len(prefix)))
        output_text.append('\n')

    if len(exchanges) > 0:
        # Add to output text if comparisons are being added to the output
        prefix = "\nAll Exchanges:"
        output_text.append(prefix + break_string(exchanges,
                                                 chars_per_line - len(prefix)))

    return '\n'.join(output_text)
