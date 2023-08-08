import os

# Pandas module for CSV parsing
import pandas as pd

# csv for Pandas options
import csv


def load_csv(file_path, separator, column):
    csv_reader = pd.read_csv(file_path,
                             sep=separator,
                             header=None,
                             usecols=[column])
    csv_list = csv_reader[column].tolist()
    return csv_list


def save_csv_to_file(dictio, file_path, separator):
    # Convert the dictionnary into a DataFrame
    df = pd.DataFrame.from_dict(dictio,
                                orient='index')

    # Delete the CSV file if it already exists
    if os.path.exists(file_path):
        os.remove(file_path)

    # Save the DataFrame as a CSV file
    df.to_csv(file_path,
              sep=separator,
              header=False,
              index=True,
              quoting=csv.QUOTE_NONNUMERIC)

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
