import pandas as pd


def load_csv(path):
    csv_reader_1 = pd.read_csv(path_1,
                               sep=separator,
                               header=None,
                               usecols=[column])
    BN_ID_csv_1 = csv_reader_1[column].tolist()