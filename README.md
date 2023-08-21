# QuickMerge

This repo contains packages and modules that implements quicksort and natural
merge sort. Their performance is also compared using data from various file
sizes.

## Running QuickMerge

1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m lab4 -h`. This will print the help
   message.
4. Run the program as a module (with real inputs):
   `python -m lab4 <some_input_file> <some_output_file>`
   - Example: `python -m lab4 resources/input.txt resources/output.txt`
   - Optional - run the program as a module with errors outputted to stderr:
     `python -m lab4 <some_input_file> <some_output_file> --debug`

Output will be written to the specified output file after processing the input
file.

### QuickMerge Usage:

```commandline
usage: python -m lab4 [-h] in_file out_file [--debug]

positional arguments:
  in_file     Input File Pathname
  out_file    Output File Pathname

optional arguments:
  --debug             Toggles debug mode to log errors to stderr
  -h, --help          show this help message and exit
```

Usage statements reference

| Symbol        | Meaning                                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------ |
| [var]         | variable var is optional.                                                                                          |
| var           | variable var is required. All positional arguments are required.                                                   |
| -v, --version | This refers to a flag. One dash + one letter OR two dashes and a whole word. Some flags take one or more arguments |
| +             | This argument consumes 1 or more values                                                                            |
| \*            | This argument consumes 0 or more values                                                                            |

### Project Layout

- [QuickMerge/](.): The parent or "root" folder containing all of these
  files
  - [README.md](README.md):
    The guide you're reading.
  - [lab4](lab4):
    This is the _package_.
    - [`__init__.py`](lab4/__init__.py)
      This contains the functionality that is automatically run when importing
      the package
    - [`__main__.py`](lab4/__main__.py)
      This file is the entrypoint to the lab4 package when run as a program
    - `*.py`
      These are Python scripts that do the actual work
  - [support](support):
    This is a separate package for supporting modules not directly involved in
    sorting.
    - [`__init__.py`](support/__init__.py)
      This contains the functionality that is automatically run when importing
      the package
    - `*.py`
      These are the supporting Python modules
  - [Resources](resources)
    - `*.txt`
      These are the input files for testing code
    - `*_output.txt`
      These are the output files for metrics and data from input files with
      same name

### Python Version

3.10.x

### IDE / Editor

Visual Studio Code (WSL: Ubuntu)
