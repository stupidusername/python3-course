import csv, json

def convert(csv_path, json_path):
    # Open CSV file for reading.
    with open(csv_path, newline='') as csv_file:
        # Create CSV reader.
        csv_reader = csv.DictReader(csv_file)
        # Open JSON file for writing.
        with open(json_path, 'w') as json_file:
            # Start JSON array.
            json_file.write('[\n')
            # Write each row converted to a JSON object.
            for row in csv_reader:
                json_file.write(f'\t{json.dumps(row)}')
                pos = json_file.tell()  # Position before inserting last ",".
                json_file.write(',\n')
            # End JSON array.
            json_file.seek(pos)  # Go back to the last ",".
            json_file.write('\n]\n')
