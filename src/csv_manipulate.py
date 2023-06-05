import pandas as pd


def load_csv(path, separator, column):
    csv_list = pd.read_csv(path,
                           sep=separator,
                           header=None,
                           usecols=[column])
    csv_list = csv_list[column].tolist()
    return csv_list


def sauv_csv(data, separator):
    rslt_csv = pd.DataFrame(data)
    rslt_csv.to_csv('csv_rslt.csv',
                    sep=separator)
