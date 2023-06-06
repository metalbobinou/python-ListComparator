from tkinter import filedialog
import pandas as pd


def load_csv(path, separator, column):
    csv_list = pd.read_csv(path,
                           sep=separator,
                           header=None,
                           usecols=[column])
    csv_list = csv_list[column].tolist()
    return csv_list


def save_csv(dictio, separator):
    # Demander à l'utilisateur de choisir l'emplacement de sauvegarde
    file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("Fichier CSV",
                                                         "*.csv")])
    if file_path:
        # Convertir le dictionnaire en DataFrame
        df = pd.DataFrame.from_dict(dictio, orient='index')

        # Sauvegarder le DataFrame en tant que fichier CSV
        df.to_csv(file_path, sep=separator, header=False, index=False)
