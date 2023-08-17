"""
output_formatters

This module contains helper functions called to format strings intended to be
outputted to a text file.

Author: Rani Hinnawi
Date: 2023-08-08
"""
from typing import TextIO, List, Union


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


def format_sorted_results(line_number: int, records: List[str],
                          result: List[Union[str, int]], metrics: str,
                          error=False, chars_per_line=80) -> str:
    """
    Function that formats the inputted expression and the output given from a
    sorting process.

    Args:
        line_number (int): number for labelling lines in the output
        expression (List[str]): original file records before being sorted
        result (List[str]): sorted records OR error message
        metrics (str): string representation of Performance values (size, runtime)
        error (bool): indicator of whether result is an error message

    Returns:
        str: conditionally formatted results
    """
    # Format header line with original expression
    prefix = f"{line_number}. Original: "
    expression = break_string(records, chars_per_line - len(prefix))
    write = [prefix + expression]

    # Format and append result with error  handling
    prefix = "\tError - " if error else "\tSorted: "
    result = break_string(result, chars_per_line - len(prefix))
    write.append(prefix + result)

    # Add metrics and return
    write.append(f"{metrics}\n")

    return '\n'.join(write)
