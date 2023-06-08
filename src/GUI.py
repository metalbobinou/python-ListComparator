import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from logic_processing import union
from logic_processing import inter
from logic_processing import occurence
from logic_processing import unique
from logic_processing import inv_inter
from logic_processing import smart_union
from csv_manipulate import load_csv
# from csv_manipulate import save_csv

gui_windows = [None, None, None, None]
gui_liste = [None, None, None]


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


class WindowList:
    geometry = "0"
    Title = "My window"
    # Canevas getting the whole window
    MainCanevas = None
    # Load/Save buttons in the window
    LoadButton = None
    SaveButton = None
    # Frame for putting scrollbar and list inside
    Frame = None
    # Right scrollbar
    Scrollbar = None
    # ListBox with the data
    ListBox = None

    # def WindowListGenerator(self):
    def __init__(self, geometry):
        self.MainCanevas = tk.Tk()

        self.SetGeometry(geometry)

        # Load CSV button
        self.LoadButton = tk.Button(self.MainCanevas,
                                    text="Charger",
                                    state=tk.DISABLED,
                                    command=lambda: LoadFile(self))
        self.LoadButton.pack()
        # Save CSV button
        self.SaveButton = tk.Button(self.MainCanevas,
                                    text="Sauvegarder",
                                    state=tk.DISABLED,
                                    command=lambda: SaveFile(self))
        self.SaveButton.pack()

        # Frame for containing the list
        self.Frame = ttk.Frame(self.MainCanevas)
        self.Frame.pack(fill=tk.BOTH,
                        expand=True)

        # Scrollbar for the list
        self.Scrollbar = ttk.Scrollbar(self.Frame,
                                       orient=tk.VERTICAL)

        # ListBox for containing the list
        self.ListBox = tk.Listbox(self.Frame,
                                  yscrollcommand=self.Scrollbar.set)
        self.ListBox.pack(side=tk.LEFT,
                          fill=tk.BOTH,
                          expand=True)

        # Configure the scrollbar for expanding with the list
        self.Scrollbar.config(command=self.ListBox.yview)
        self.Scrollbar.pack(side=tk.RIGHT,
                            fill=tk.Y)

    # def WindowListOutputGenerator(self):
    def SpecializedAsInputList(self):
        self.LoadButton.config(state=tk.NORMAL)
        self.SaveButton.config(state=tk.DISABLED)

    # def WindowListOutputGenerator(self):
    def SpecializedAsOutputList(self):
        self.LoadButton.config(state=tk.DISABLED)
        self.SaveButton.config(state=tk.NORMAL)

    def SetTitle(self, title):
        self.Title = title
        self.MainCanevas.title(title)

    def SetGeometry(self, geometry):
        self.geometry = geometry
        self.MainCanevas.geometry(geometry)

    def GetGeometry(self):
        return (self.geometry)

    def CallWithdraw(self):
        self.MainCanevas.withdraw()

    def CallDestroy(self):
        self.MainCanevas.destroy()

    def GetCanevas(self):
        return (self.MainCanevas)


# Callback for LoadButton
def LoadFile(TheWindowList):
    TheWindowList.CallWithdraw()
    TheWindowList.SimpleCanevas()
    TheWindowList.SetTitle("Charger un nouveau CSV")

    # Variables pour stocker les chemins des fichiers
    file_path = tk.StringVar()

    # Étiquettes pour afficher les chemins des fichiers
    label = tk.Label(TheWindowList, textvariable=file_path)
    label.pack()

    # Boutons pour importer les fichiers
    button = tk.Button(TheWindowList,
                       text="Importer CSV 1",
                       command=lambda: import_csv(file_path))
    button.pack()


# Callback for SaveButton
def SaveFile(TheWindowList):
    TheWindowList.CallWithdraw()
    TheWindowList.SimpleCanevas()
    TheWindowList.SetTitle("Sauvegarder le résultat")


def inter_window():
    global gui_windows, gui_liste

    if gui_windows[3] is not None:
        gui_windows[3].CallWithdraw()
        del gui_windows[3]
        gui_windows.append(None)

    # Crée un canevas pour afficher les résultats
    gui_windows[3] = WindowList("300x400+650+300")
    gui_windows[3].SetTitle("Intersection des BN_ID des deux CSV")
    gui_windows[3].SpecializedAsOutputList()
    insert_data(gui_windows[3].ListBox, (occurence(inter(gui_liste[0],
                                                         gui_liste[1]))))


def union_window():
    global gui_windows, gui_liste

    if gui_windows[3] is not None:
        # gui_windows[3].withdraw()
        gui_windows[3].CallWithdraw()
        del gui_windows[3]
        gui_windows.append(None)

    # Crée un canevas pour afficher les résultats
    gui_windows[3] = WindowList("300x400+650+300")
    gui_windows[3].SetTitle("Union des BN_ID des deux CSV")
    gui_windows[3].SpecializedAsOutputList()
    insert_data(gui_windows[3].ListBox, (occurence(union(gui_liste[0],
                                                         gui_liste[1]))))


def unique_1_window():
    global gui_windows, gui_liste

    if gui_windows[3] is not None:
        # gui_windows[3].withdraw()
        gui_windows[3].CallWithdraw()
        del gui_windows[3]
        gui_windows.append(None)

    # Crée un canevas pour afficher les résultats
    gui_windows[3] = WindowList("300x400+650+300")
    gui_windows[3].SetTitle("Valeur propre au premier CSV")
    gui_windows[3].SpecializedAsOutputList()
    insert_data(gui_windows[3].ListBox, (occurence(unique(gui_liste[0],
                                                          gui_liste[1], 1))))
    

def unique_2_window():
    global gui_windows, gui_liste

    if gui_windows[3] is not None:
        # gui_windows[3].withdraw()
        gui_windows[3].CallWithdraw()
        del gui_windows[3]
        gui_windows.append(None)

    # Crée un canevas pour afficher les résultats
    gui_windows[3] = WindowList("300x400+650+300")
    gui_windows[3].SetTitle("Valeur propre au deuxième CSV")
    gui_windows[3].SpecializedAsOutputList()
    insert_data(gui_windows[3].ListBox, (occurence(unique(gui_liste[0],
                                                          gui_liste[1], 2))))


def inv_inter_window():
    global gui_windows, gui_liste

    if gui_windows[3] is not None:
        # gui_windows[3].withdraw()
        gui_windows[3].CallWithdraw()
        del gui_windows[3]
        gui_windows.append(None)

    # Crée un canevas pour afficher les résultats
    gui_windows[3] = WindowList("300x400+650+300")
    gui_windows[3].SetTitle("Inverse de l'intersection des BN_ID des deux CSV")
    gui_windows[3].SpecializedAsOutputList()
    insert_data(gui_windows[3].ListBox, (occurence(inv_inter(gui_liste[0],
                                                             gui_liste[1]))))


def smart_union_window():
    global gui_windows, gui_liste

    if gui_windows[3] is not None:
        # gui_windows[3].withdraw()
        gui_windows[3].CallWithdraw()
        del gui_windows[3]
        gui_windows.append(None)

    # Crée un canevas pour afficher les résultats
    gui_windows[3] = WindowList("300x400+650+300")
    gui_windows[3].SetTitle("Smart union des BN_ID des deux CSV")
    gui_windows[3].SpecializedAsOutputList()
    insert_data(gui_windows[3].ListBox, (occurence(smart_union(gui_liste[0],
                                                               gui_liste[1]))))


def process_csv():
    global gui_windows, gui_liste

    # Crée un nouveau canevas pour les différentes actions
    gui_windows[0].withdraw()
    gui_windows[0] = tk.Tk()
    gui_windows[0].title("Action possible")
    gui_windows[0].geometry("300x200+650+50")

    process_button = tk.Button(gui_windows[0],
                               text="Intersection des 2 csv",
                               command=inter_window)
    process_button.pack()

    process_button = tk.Button(gui_windows[0],
                               text="Union des 2 csv",
                               command=union_window)
    process_button.pack()

    process_button = tk.Button(gui_windows[0],
                               text="Valeurs propre au premier csv",
                               command=unique_1_window)
    process_button.pack()

    process_button = tk.Button(gui_windows[0],
                               text="Valeurs propre au deuxième csv",
                               command=unique_2_window)
    process_button.pack()

    process_button = tk.Button(gui_windows[0],
                               text="inverse de l'intersection des 2 csv",
                               command=inv_inter_window)
    process_button.pack()

    process_button = tk.Button(gui_windows[0],
                               text="Smart union des 2 csv",
                               command=smart_union_window)
    process_button.pack()

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
    if path_1 and path_2 and separator1 and separator2 and column1 and column2 is not None:
        # Crée un nouveau canevas pour chaque fichier CSV
        gui_windows[1] = WindowList("300x400+200+150")
        gui_windows[1].SetTitle("BN_ID du premier csv")
        gui_windows[1].SpecializedAsInputList()

        gui_windows[2] = WindowList("300x400+1100+150")
        gui_windows[2].SetTitle("BN_ID du deuxième csv")
        gui_windows[2].SpecializedAsInputList()

        # Lit les fichiers CSV et traite les données selon nos paramètres
        BN_ID_csv_1 = load_csv(path_1, separator1, column2)
        gui_liste[0] = BN_ID_csv_1
        insert_data(gui_windows[1].ListBox, occurence(gui_liste[0]))

        BN_ID_csv_2 = load_csv(path_2, separator1, column2)
        gui_liste[1] = BN_ID_csv_2
        insert_data(gui_windows[2].ListBox, occurence(gui_liste[1]))

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

gui_windows[0] = window

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

gui_windows[0] = window

# Bouton pour traiter les fichiers CSV
process_button = tk.Button(window,
                           text="Traiter",
                           command=process_csv)
process_button.pack()

# Canevas pour fermer toutes les fenêtres
close = tk.Tk()
close.title("Femer")
close.geometry("300x50+1200+50")

process_button = tk.Button(close,
                           text="Fermer les fenêtres",
                           command=window.quit)
process_button.pack()


# Lance la boucle principale Tkinter
window.mainloop()
