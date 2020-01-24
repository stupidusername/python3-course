# Requirement:
#
# Write a program that reads a CSV file and builds a list of dict objects with
# the content of each row. The dictionary must use the column names as its
# keys. It is assumend that the first line of the CSV contains the column
# names.
#
# The program must take a positional argument that specifies the path of the
# CSV file to be processed.
# An optional argument (-d or --delimiter) can be used to specify which
# delimitir will be used to process the CSV (it must default to ",").

# Implemented on Python 3.

import argparse


# Exception raised when a processed file is not a well-formed CSV.
class MalformedCSV(Exception):
    pass


parser = argparse.ArgumentParser(description='CSV parser.')

# Add CSV file argument.
parser.add_argument(
    'csv',
    help='Path to CSV file',
    type=argparse.FileType('r')
)

# Add delimiter argument.
parser.add_argument(
    '-d',
    '--delimiter',
    dest='delimiter',
    default=',',
    help='CSV delimiter (defaults to ",")'
)

# Parse command line arguments.
args = parser.parse_args()

# List of processed rows.
rows = []

# Build the column names.
cols = args.csv.readline().strip().split(args.delimiter)

# If the file is empty raise an exception.
if not cols:
    raise MalformedCSV('The CSV file does not have any line.')

if not all(cols):
    # A columnt is empty, raise an exception.
    raise MalformedCSV('The CSV contains an empty column name.')

# Process rows.
for row_number, line in enumerate(args.csv):
    row_cols = line.strip().split(args.delimiter)
    if len(row_cols) != len(cols):
        # The columns of this row do not match the columns defined in the first
        # line.
        raise MalformedCSV(
            f'Line {row_number + 2} has an invalid column count.'
        )
    # Add a dictionary (built from this row) to the rows list.
    rows.append(dict(zip(cols, row_cols)))

# Prit the processed rows.
for row in rows:
    print(row)

# Close file.
args.csv.close()
