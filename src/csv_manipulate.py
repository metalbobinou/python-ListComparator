import pandas as pd
import os
import csv
from tkinter import filedialog


def load_csv(path, separator, column):
    csv_list = pd.read_csv(path,
                           sep=separator,
                           header=None,
                           usecols=[column])
    csv_list = csv_list[column].tolist()
    return csv_list


def save_csv_to_file(dictio, separator, file_path):
    # Convertir le dictionnaire en DataFrame
    df = pd.DataFrame.from_dict(dictio, orient='index')

    # Supprime le fichier csv si il existe déjà
    if os.path.exists(file_path):
        os.remove(file_path)

    # Sauvegarder le DataFrame en tant que fichier CSV
    df.to_csv(file_path, sep=separator, header=False, index=True)


def print_out_csv(dictio, separator):
    for key, value in dictio.items():
        print(f"{key}{separator}{value}")


def save_csv(dictio, separator, file_path):
    if (file_path == "-"):
        print_out_csv(dictio, separator)
    else:
        save_csv_to_file(dictio, separator, file_path)
