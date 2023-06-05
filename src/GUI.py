import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
# import pandas as pd
from logic_processing import union
from logic_processing import inter
from logic_processing import occurence
from csv_manipulate import load_csv
# from csv_manipulate import sauv_csv


def import_csv(file_number):
    # Ouvre une boîte de dialogue pour sélectionner un fichier CSV
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    # Vérifie si un fichier a été sélectionné
    if file_path:
        # Stocke le chemin du fichier
        if file_number == 1:
            file_path_1.set(file_path)
        elif file_number == 2:
            file_path_2.set(file_path)


def insert_data(data, dictio):
    for valeur, compte in dictio.items():
        texte = f"{valeur} : {compte} occurrence(s)"
        data.insert(0, texte)


def inter_csv():
    # Obtient les chemins des fichiers sélectionnés
    path_1 = file_path_1.get()
    path_2 = file_path_2.get()

    # Obtient le séparateur choisi
    separator = separator_var.get()

    # Obtient le numéro de colonne saisi
    # Convertit en entier et ajuste pour l'index de la colonne
    column = int(column_entry.get()) - 1

    # Lit les fichiers CSV et traite les données selon nos paramètres
    BN_ID_csv_1 = load_csv(path_1, separator, column)

    BN_ID_csv_2 = load_csv(path_2, separator, column)

    # Vérifie si les fichiers et les paramètres ont été sélectionnés
    if path_1 and path_2 and separator is not None:
        # Crée un canevas pour afficher les résultats
        inter_2_csv = tk.Tk()
        inter_2_csv.title("Intersection des BN_ID des deux CSV")
        inter_2_csv.geometry("300x400+650+300")

        # Création d'un widget Frame pour contenir la liste des résultats
        frame = ttk.Frame(inter_2_csv)
        frame.pack(fill=tk.BOTH,
                   expand=True)

        # Création d'un widget Scrollbar
        scrollbar = ttk.Scrollbar(frame,
                                  orient=tk.VERTICAL)

        # Création d'un widget Listbox pour afficher les résultats
        BN_ID_inter = tk.Listbox(frame,
                                 yscrollcommand=scrollbar.set)
        BN_ID_inter.pack(side=tk.LEFT,
                         fill=tk.BOTH,
                         expand=True)

        # Configuration de la Scrollbar pour se déplacer avec la Listbox
        scrollbar.config(command=BN_ID_inter.yview)
        scrollbar.pack(side=tk.RIGHT,
                       fill=tk.Y)

        # Appel de la fonction pour remplir les résultats
        insert_data(BN_ID_inter, (occurence(inter(BN_ID_csv_1, BN_ID_csv_2))))


def union_csv():
    # Obtient les chemins des fichiers sélectionnés
    path_1 = file_path_1.get()
    path_2 = file_path_2.get()

    # Obtient le séparateur choisi
    separator = separator_var.get()

    # Obtient le numéro de colonne saisi
    # Convertit en entier et ajuste pour l'index de la colonne
    column = int(column_entry.get()) - 1

    # Lit les fichiers CSV et traite les données selon nos paramètres
    BN_ID_csv_1 = load_csv(path_1, separator, column)

    BN_ID_csv_2 = load_csv(path_1, separator, column)

    # Vérifie si les fichiers et les paramètres ont été sélectionnés
    if path_1 and path_2 and separator and column is not None:
        # Crée un canevas pour afficher les résultats
        union_2_csv = tk.Tk()
        union_2_csv.title("Union des BN_ID des deux CSV")
        union_2_csv.geometry("300x400+650+300")

        # Création d'un widget Frame pour contenir la liste des résultats
        frame = ttk.Frame(union_2_csv)
        frame.pack(fill=tk.BOTH,
                   expand=True)

        # Création d'un widget Scrollbar
        scrollbar = ttk.Scrollbar(frame,
                                  orient=tk.VERTICAL)

        # Création d'un widget Listbox pour afficher les résultats
        BN_ID_union = tk.Listbox(frame,
                                 yscrollcommand=scrollbar.set)
        BN_ID_union.pack(side=tk.LEFT,
                         fill=tk.BOTH, expand=True)

        # Configuration de la Scrollbar pour se déplacer avec la Listbox
        scrollbar.config(command=BN_ID_union.yview)
        scrollbar.pack(side=tk.RIGHT,
                       fill=tk.Y)

        # Appel de la fonction pour remplir les résultats
        insert_data(BN_ID_union, (occurence(union(BN_ID_csv_1, BN_ID_csv_2))))


def process_csv():
    # Obtient les chemins des fichiers sélectionnés
    path_1 = file_path_1.get()
    path_2 = file_path_2.get()

    # Obtient le séparateur choisi
    separator = separator_var.get()

    # Obtient le numéro de colonne saisi
    # Convertit en entier et ajuste pour l'index de la colonne
    column = int(column_entry.get()) - 1

    # Vérifie si les fichiers et les paramètres ont été sélectionnés
    if path_1 and path_2 and separator and column is not None:
        # On fait disparaître le canva ouverture
        window.withdraw()

        # Crée un nouveau canevas pour chaque fichier CSV
        canvas_1 = tk.Tk()
        canvas_1.title("BN_ID du premier csv")
        canvas_1.geometry("300x400+200+200")

        canvas_2 = tk.Tk()
        canvas_2.title("BN_ID du deuxième csv")
        canvas_2.geometry("300x400+1100+200")

        # Crée un nouveau canevas pour les différentes actions
        canvas_3 = tk.Tk()
        canvas_3.title("Action possible")
        canvas_3.geometry("300x100+650+50")

        # Lit les fichiers CSV et traite les données selon nos paramètres
        BN_ID_csv_1 = load_csv(path_1, separator, column)

        BN_ID_csv_2 = load_csv(path_2, separator, column)

        # Création d'un widget Frame pour contenir la liste des résultats
        frame_1 = ttk.Frame(canvas_1)
        frame_1.pack(fill=tk.BOTH,
                     expand=True)

        # Création d'un widget Scrollbar
        scrollbar = ttk.Scrollbar(frame_1,
                                  orient=tk.VERTICAL)

        # Création d'un widget Listbox pour afficher les résultats
        BN_ID_1 = tk.Listbox(frame_1,
                             yscrollcommand=scrollbar.set)
        BN_ID_1.pack(side=tk.LEFT,
                     fill=tk.BOTH,
                     expand=True)

        # Configuration de la Scrollbar pour se déplacer avec la Listbox
        scrollbar.config(command=BN_ID_1.yview)
        scrollbar.pack(side=tk.RIGHT,
                       fill=tk.Y)

        # Appel de la fonction pour remplir les résultats
        insert_data(BN_ID_1, occurence(BN_ID_csv_1))

        # Création d'un widget Frame pour contenir la liste des résultats
        frame_2 = ttk.Frame(canvas_2)
        frame_2.pack(fill=tk.BOTH,
                     expand=True)

        # Création d'un widget Scrollbar
        scrollbar = ttk.Scrollbar(frame_2,
                                  orient=tk.VERTICAL)

        # Création d'un widget Listbox pour afficher les résultats
        BN_ID_2 = tk.Listbox(frame_2,
                             yscrollcommand=scrollbar.set)
        BN_ID_2.pack(side=tk.LEFT,
                     fill=tk.BOTH, expand=True)

        # Configuration de la Scrollbar pour se déplacer avec la Listbox
        scrollbar.config(command=BN_ID_2.yview)
        scrollbar.pack(side=tk.RIGHT,
                       fill=tk.Y)

        insert_data(BN_ID_2, occurence(BN_ID_csv_2))

        process_button = tk.Button(canvas_3,
                                   text="Intersection des 2 csv",
                                   command=inter_csv)
        process_button.pack()

        process_button = tk.Button(canvas_3,
                                   text="Union des 2 csv",
                                   command=union_csv)
        process_button.pack()

    else:
        print("Sélectionnez tous les fichiers et paramètres souhaités.")

# Crée une fenêtre Tkinter


window = tk.Tk()
window.title("Importer CSV")
window.geometry("500x300+500+300")

# Variables pour stocker les chemins des fichiers
file_path_1 = tk.StringVar()
file_path_2 = tk.StringVar()

# Étiquettes pour afficher les chemins des fichiers
label_1 = tk.Label(window, textvariable=file_path_1)
label_1.pack()

label_2 = tk.Label(window, textvariable=file_path_2)
label_2.pack()

# Boutons pour importer les fichiers
button_1 = tk.Button(window,
                     text="Importer CSV 1",
                     command=lambda: import_csv(1))
button_1.pack()

button_2 = tk.Button(window,
                     text="Importer CSV 2",
                     command=lambda: import_csv(2))
button_2.pack()

# Liste des séparateurs
separator_options = [",", ";", ":"]

# Menu déroulant pour sélectionner le séparateur
separator_var = tk.StringVar(window)
separator_var.set(separator_options[1])  # Séparateur par défaut

separator_label = tk.Label(window,
                           text="Séparateur :")
separator_label.pack()

separator_menu = tk.OptionMenu(window,
                               separator_var,
                               *separator_options)
separator_menu.pack()

# Saisie du numéro de colonne
column_label = tk.Label(window,
                        text="Numéro de colonne :")
column_label.pack()

column_entry = tk.Entry(window)
column_entry.pack()

# Bouton pour traiter les fichiers CSV
process_button = tk.Button(window,
                           text="Traiter",
                           command=process_csv)
process_button.pack()

# Lance la boucle principale Tkinter
window.mainloop()
