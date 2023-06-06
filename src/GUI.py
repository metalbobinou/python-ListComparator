import tkinter as tk
from tkinter import ttk
# import pandas as pd
from logic_processing import union
from logic_processing import inter
from logic_processing import occurence
from csv_manipulate import load_csv
from csv_manipulate import save_csv
from csv_manipulate import import_csv

gui_windows = [None, None, None, None]
gui_liste = [None, None, None]


def insert_data(data, dictio):
    for valeur, compte in dictio.items():
        texte = f"{valeur} : {compte} occurrence(s)"
        data.insert(0, texte)


def win_generator():
    canevas = tk.Tk()

    charge_button = tk.Button(canevas,
                              text="Charger",
                              state=tk.DISABLED)
                              # command=charger)
    charge_button.pack()

    save_button = tk.Button(canevas,
                            text="Sauvegarder",
                            state=tk.DISABLED)
                            # command=sauvegarder)
    save_button.pack()

    return canevas


def inter_csv():
    global gui_windows, gui_liste

    if gui_windows[3] is not None:
        gui_windows[3].withdraw()
        del gui_windows[3]
        gui_windows.append(None)

    # Crée un canevas pour afficher les résultats
    gui_windows[3] = win_generator()
    gui_windows[3].title("Intersection des BN_ID des deux CSV")
    gui_windows[3].geometry("300x400+650+300")

    # Création d'un widget Frame pour contenir la liste des résultats
    frame = ttk.Frame(gui_windows[3])
    frame.pack(fill=tk.BOTH,
               expand=True)

    # Création d'un widget Scrollbar
    scrollbar = ttk.Scrollbar(frame,
                              orient=tk.VERTICAL)

    # Création d'un widget Listbox pour afficher les résultats
    BN_ID_inter = tk.Listbox(frame,
                             yscrollcommand=scrollbar.set)
    BN_ID_inter.pack(side=tk.LEFT,
                     fill=tk.BOTH, expand=True)

    # Configuration de la Scrollbar pour se déplacer avec la Listbox
    scrollbar.config(command=BN_ID_inter.yview)
    scrollbar.pack(side=tk.RIGHT,
                   fill=tk.Y)

    # Appel de la fonction pour remplir les résultats
    insert_data(BN_ID_inter, (occurence(inter(gui_liste[0],
                                              gui_liste[1]))))


def union_csv():
    global gui_windows, gui_liste

    if gui_windows[3] is not None:
        gui_windows[3].withdraw()
        del gui_windows[3]
        gui_windows.append(None)

    # Crée un canevas pour afficher les résultats
    gui_windows[3] = win_generator()
    gui_windows[3].title("Union des BN_ID des deux CSV")
    gui_windows[3].geometry("300x400+650+300")

    # Création d'un widget Frame pour contenir la liste des résultats
    frame = ttk.Frame(gui_windows[3])
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
    insert_data(BN_ID_union, (occurence(union(gui_liste[0],
                                              gui_liste[1]))))


# def save_dictionary_as_csv(dictionary):
    # Créer la fenêtre principale
    canevas_save = tk.Tk()
    canevas_save.title("Sauvegarder le dictionnaire en CSV")

    # Définir la fonction pour sauvegarder le dictionnaire en CSV
    def command_save(dictionary, separator):
        save_csv(dictionary, separator)

    # Définir la fonction pour choisir le séparateur

    def choose_separator():
        separator = separator_entry.get()
        save_csv(separator)

    # Créer le canevas
    canvas = tk.Canvas(canevas_save, width=300, height=200)
    canvas.pack()

    # Ajouter un champ de saisie pour le séparateur
    separator_label = tk.Label(canevas_save, text="Séparateur:")
    separator_label.pack()
    separator_entry = tk.Entry(canevas_save)
    separator_entry.pack()

    # Ajouter un bouton pour choisir le séparateur
    separator_button = tk.Button(canevas_save, text="Choisir séparateur",
                                 command=choose_separator)
    separator_button.pack()

    separator_button = tk.Button(canevas_save, text="Sauvegarder",
                                 command=command_save)
    separator_button.pack()


def process_csv():
    global gui_windows, gui_liste

    # Crée un nouveau canevas pour les différentes actions
    gui_windows[0].withdraw()
    gui_windows[0] = tk.Tk()
    gui_windows[0].title("Action possible")
    gui_windows[0].geometry("300x100+650+50")

    process_button = tk.Button(gui_windows[0],
                               text="Intersection des 2 csv",
                               command=inter_csv)
    process_button.pack()

    process_button = tk.Button(gui_windows[0],
                               text="Union des 2 csv",
                               command=union_csv)
    process_button.pack()

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
        # Crée un nouveau canevas pour chaque fichier CSV
        gui_windows[1] = win_generator()
        gui_windows[1].title("BN_ID du premier csv")
        gui_windows[1].geometry("300x400+200+150")

        gui_windows[2] = win_generator()
        gui_windows[2].title("BN_ID du deuxième csv")
        gui_windows[2].geometry("300x400+1100+150")

        # Lit les fichiers CSV et traite les données selon nos paramètres
        BN_ID_csv_1 = load_csv(path_1, separator, column)
        gui_liste[0] = BN_ID_csv_1

        BN_ID_csv_2 = load_csv(path_2, separator, column)
        gui_liste[1] = BN_ID_csv_2

        # Création d'un widget Frame pour contenir la liste des résultats
        frame_1 = ttk.Frame(gui_windows[1])
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
        frame_2 = ttk.Frame(gui_windows[2])
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
                     command=lambda: import_csv(1, file_path_1, file_path_2))
button_1.pack()

button_2 = tk.Button(window,
                     text="Importer CSV 2",
                     command=lambda: import_csv(2, file_path_1, file_path_2))
button_2.pack()

# Liste des séparateurs
separator_options = [",", ";", ":"]

# Menu déroulant pour sélectionner le séparateur du csv 1
separator_var = tk.StringVar(window)
separator_var.set(separator_options[1])  # Séparateur par défaut

separator_label = tk.Label(window,
                           text="Séparateur :")
separator_label.pack()

separator_menu = tk.OptionMenu(window,
                               separator_var,
                               *separator_options)
separator_menu.pack()

# Saisie du numéro de colonne du csv 1
column_label = tk.Label(window,
                        text="Numéro de colonne csv 1 :")
column_label.pack()

column_entry = tk.Entry(window)
column_entry.pack()

gui_windows[0] = window

# Menu déroulant pour sélectionner le séparateur du csv 2
separator_var = tk.StringVar(window)
separator_var.set(separator_options[1])  # Séparateur par défaut

separator_label = tk.Label(window,
                           text="Séparateur :")
separator_label.pack()

separator_menu = tk.OptionMenu(window,
                               separator_var,
                               *separator_options)
separator_menu.pack()

# Saisie du numéro de colonne du csv 2
column_label = tk.Label(window,
                        text="Numéro de colonne csv 2 :")
column_label.pack()

column_entry = tk.Entry(window)
column_entry.pack()

gui_windows[0] = window

# Bouton pour traiter les fichiers CSV
process_button = tk.Button(window,
                           text="Traiter",
                           command=process_csv)
process_button.pack()

# Lance la boucle principale Tkinter
window.mainloop()
