import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from GuiClasses import WindowList
from GuiClasses import WindowActions
from logic_processing import occurence
from csv_manipulate import load_csv
from csv_manipulate import save_csv

# gui_windows : Opening 2 files, Input List 1, Input List 2, Output List
from GuiClasses import GlobalWindows
#gui_windows = [None, None, None, None]

# gui_liste : Input List 1, Input List 2, Output List
import GlobalLists
#gui_liste = [None, None, None]


def insert_data(data, dictio):
    for valeur, compte in dictio.items():
        texte = f"{valeur} : {compte} occurrence(s)"
        data.insert(0, texte)


def import_csv(file_path):
    # Ouvre une boîte de dialogue pour sélectionner un fichier CSV
    file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    # Vérifie si un fichier a été sélectionné
    if file:
        # Stocke le chemin du fichier
        file_path.set(file)


def save_path():
    # Demander à l'utilisateur de choisir l'emplacement de sauvegarde
    file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("Fichier CSV",
                                                         "*.csv")])
    return file_path


def process_csv():
    global gui_windows, gui_liste

    # Vérifie si les fichiers et les paramètres ont été sélectionnés
    if (file_path_1.get() == "") or (file_path_2.get() == "")           \
       or (separator_var1.get() == "") or (separator_var2.get() == "") \
       or (column_entry1.get() == "") or (column_entry2.get() == ""):

        label = tk.Label(gui_windows[0], text="Sélectionner tous les fichiers et paramètres souhaités")
        label.pack()
    else:
        # Hide main window selecting files
        GlobalWindows.gui_windows[0].withdraw()

        ### !!! WARNING : HIDDEN WINDOW IS LOST IN MEMORY !!!

        # Show a new window with the possible actions
        GlobalWindows.gui_windows[0] = WindowActions.WindowActions("300x200+650+50")
        GlobalWindows.gui_windows[0].SetTitle("Action possible")
        
        # Obtient les chemins des fichiers sélectionnés
        path_1 = file_path_1.get()
        path_2 = file_path_2.get()
    
        # Obtient le séparateur choisi
        separator1 = separator_var1.get()
        separator2 = separator_var2.get()
        
        # Obtient le numéro de colonne saisi
        # Convertit en entier et ajuste pour l'index de la colonne
        column1 = int(column_entry1.get()) - 1
        column2 = int(column_entry2.get()) - 1

        # Vérifie si les fichiers et les paramètres ont été sélectionnés
        if (path_1 is not None) and (path_2 is not None) and          \
           (separator1 is not None) and (separator2 is not None) and  \
           (column1 is not None) and (column2 is not None) :
            # Crée un nouveau canevas pour chaque fichier CSV
            GlobalWindows.gui_windows[1] = WindowList.WindowList("300x400+200+150")
            GlobalWindows.gui_windows[1].SetTitle("BN_ID du premier csv")
            GlobalWindows.gui_windows[1].SpecializedAsInputList()
            
            GlobalWindows.gui_windows[2] = WindowList.WindowList("300x400+1100+150")
            GlobalWindows.gui_windows[2].SetTitle("BN_ID du deuxième csv")
            GlobalWindows.gui_windows[2].SpecializedAsInputList()

            # Lit les fichiers CSV et traite les données selon nos paramètres
            BN_ID_csv_1 = load_csv(path_1, separator1, column2)

            GlobalLists.gui_liste[0] = BN_ID_csv_1
            insert_data(GlobalWindows.gui_windows[1].ListBox, occurence(GlobalLists.gui_liste[0]))

            BN_ID_csv_2 = load_csv(path_2, separator1, column2)
            GlobalLists.gui_liste[1] = BN_ID_csv_2
            insert_data(GlobalWindows.gui_windows[2].ListBox, occurence(GlobalLists.gui_liste[1]))
        else:
            print("Sélectionnez tous les fichiers et paramètres souhaités.")

# Crée une fenêtre Tkinter
window = tk.Tk()
window.title("Importer CSV")
window.geometry("500x350+500+300")

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
                     command=lambda: import_csv(file_path_1))
button_1.pack()

button_2 = tk.Button(window,
                     text="Importer CSV 2",
                     command=lambda: import_csv(file_path_2))
button_2.pack()

# Liste des séparateurs
separator_options = [",", ";", ":"]

# Menu déroulant pour sélectionner le séparateur du csv 1
separator_var1 = tk.StringVar(window)
separator_var1.set(separator_options[1])  # Séparateur par défaut

separator_label1 = tk.Label(window,
                            text="Séparateur csv 1 :")
separator_label1.pack()

separator_menu1 = tk.OptionMenu(window,
                                separator_var1,
                                *separator_options)
separator_menu1.pack()

# Saisie du numéro de colonne du csv 1
column_label1 = tk.Label(window,
                         text="Numéro de colonne csv 1 :")
column_label1.pack()

column_entry1 = tk.Entry(window)
column_entry1.insert(0, "6")
column_entry1.pack()

GlobalWindows.gui_windows[0] = window

# Menu déroulant pour sélectionner le séparateur du csv 2
separator_var2 = tk.StringVar(window)
separator_var2.set(separator_options[1])  # Séparateur par défaut

separator_label2 = tk.Label(window,
                            text="Séparateur csv 2 :")
separator_label2.pack()

separator_menu2 = tk.OptionMenu(window,
                                separator_var2,
                                *separator_options)
separator_menu2.pack()

# Saisie du numéro de colonne du csv 2
column_label2 = tk.Label(window,
                         text="Numéro de colonne csv 2 :")
column_label2.pack()

column_entry2 = tk.Entry(window)
column_entry2.insert(0, "6")
column_entry2.pack()

GlobalWindows.gui_windows[0] = window

# Bouton pour traiter les fichiers CSV
process_button = tk.Button(window,
                           text="Traiter",
                           command=process_csv)
process_button.pack()

# Canvas pour fermer toutes les fenêtres
close = tk.Tk()
close.title("Femer")
close.geometry("300x50+1200+50")

process_button = tk.Button(close,
                           text="Fermer les fenêtres",
                           command=window.quit)
process_button.pack()


# Lance la boucle principale Tkinter
window.mainloop()
