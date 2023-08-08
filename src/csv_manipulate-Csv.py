import os

# csv module for CSV parsing
import csv as csv


def load_csv(file_path, separator, column):
    # Open file
    with open(file_path, newline='') as  csv_file:
        # Prepare a reader on the opened file
        csv_reader = csv.reader(csv_file,
                                delimiter=separator)
        # Read each line and get the desired column
        csv_list = []
        for line in csv_reader:
            csv_list.append(str(line[column]))
    return csv_list


def save_csv_to_file(dictio, file_path, separator):
    # Delete the CSV file if it already exists
    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, 'w') as csv_file:
        writer = csv.writer(csv_file,
                            delimiter=separator,
                            quoting=csv.QUOTE_NONNUMERIC,
                            escapechar='')
        for key, value in dictio.items():
            writer.writerow([key, value])

### Quoting :
# csv.QUOTE_ALL         : quotes every field
# csv.QUOTE_MINIMAL     : quotes only fields with special characters
# csv.QUOTE_NONNUMERIC  : quotes only non-numeric fields
# csv.QUOTE_NONE        : no quoting [requires an 'escapechar']


def print_out_csv(dictio, separator):
    for key, value in dictio.items():
        print(f"{key}{separator}{value}")


def save_csv(dictio, separator, file_path):
    if (file_path == "-"):
        print_out_csv(dictio, separator)
    else:
        save_csv_to_file(dictio, file_path, separator)
