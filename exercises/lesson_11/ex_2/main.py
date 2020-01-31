# Requirement:
#
# Write a module that defines a function that takes two arguments: a path to a
# CSV file and a path to a JSON file.
# The function must read the CSV file and write to the JSON file.
# The JSON file must contain an array of JSON objects (one for each CSV row).
# Each object must have the name of the columns as keys and the row values as
# its corresponding values.
# Also, write a script that uses the created module.

# Implemented on Python 3.6.

import argparse, csv2json

parser = argparse.ArgumentParser(description='CSV to JSON converter.')

# Add CSV file argument.
parser.add_argument('csv', help='Path to CSV file')

# Add JSON file argument.
parser.add_argument('json', help='Path to JSON file')

# Parse command line arguments.
args = parser.parse_args()

csv2json.convert(args.csv, args.json)
