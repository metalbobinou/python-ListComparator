import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


# Class for printing lists (input and output) and asking for load/save
class WindowList:
    Geometry = "0"
    Title = "List Window"
    # Canvas getting the whole window
    MainCanvas = None
    # Load/Save buttons in the window
    LoadButton = None
    SaveButton = None
    SortButton = None
    ListButton = None
    # Frame for putting scrollbar and list inside
    Frame = None
    # Right scrollbar
    Scrollbar = None
    # ListBox with the data
    ListBox = None

    # def WindowListGenerator(self):
    def __init__(self, geometry, liste, dictio):
        self.MainCanvas = tk.Tk()

        self.SetGeometry(geometry)

        # Load CSV button
        self.LoadButton = tk.Button(self.MainCanvas,
                                    text="Charger",
                                    state=tk.DISABLED,
                                    command=lambda: LoadFile(self))
        self.LoadButton.pack()
        # Save CSV button
        self.SaveButton = tk.Button(self.MainCanvas,
                                    text="Sauvegarder",
                                    state=tk.DISABLED,
                                    command=lambda: SaveFile(self))
        self.SaveButton.pack()
        # List CSV button
        ListButton = tk.Button(self.MainCanvas,
                               text="Lister",
                               state=tk.NORMAL,
                               command=lambda: insert_data_list(self.ListBox,
                                                                liste))
        ListButton.pack()
        # Occurence CSV button
        OccuButton = tk.Button(self.MainCanvas,
                               text="Occurence",
                               state=tk.NORMAL,
                               command=lambda: insert_data_occu(self.ListBox,
                                                                dictio))
        OccuButton.pack()

        # Frame for containing the list
        self.Frame = ttk.Frame(self.MainCanvas)
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
        self.MainCanvas.title(title)

    def SetGeometry(self, geometry):
        self.Geometry = geometry
        self.MainCanvas.geometry(geometry)

    def GetGeometry(self):
        return (self.Geometry)

    def GetTitle(self):
        return (self.Title)

    def CallWithdraw(self):
        self.MainCanvas.withdraw()

    def CallDestroy(self):
        self.MainCanvas.destroy()


# Callback for LoadButton
def LoadFile(TheWindowList):
    TheWindowList.CallWithdraw()
    TheWindowList.SimpleCanvas()
    TheWindowList.SetTitle("Charger un nouveau CSV")

    # Variables pour stocker les chemins des fichiers
    file_path = tk.StringVar()

    # Étiquettes pour afficher les chemins des fichiers
    label = tk.Label(TheWindowList, textvariable=file_path)
    label.pack()

    # Boutons pour importer les fichiers
    button = tk.Button(TheWindowList,
                       text="Importer CSV 1",
                       command=lambda: import_csv2(file_path))
    button.pack()


# Callback for SaveButton
def SaveFile(TheWindowList):
    TheWindowList.CallWithdraw()
    TheWindowList.SimpleCanvas()
    TheWindowList.SetTitle("Sauvegarder le résultat")


def insert_data_list(data, liste):
    data.delete(0, tk.END)
    for element in liste:
        data.insert(tk.END, element)


def insert_data_occu(data, dictio):
    data.delete(0, tk.END)
    for valeur, compte in dictio.items():
        texte = f"{valeur} : {compte} occurrence(s)"
        data.insert(tk.END, texte)


#  TMP
def import_csv2(file_path):
    # Ouvre une boîte de dialogue pour sélectionner un fichier CSV
    file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    # Vérifie si un fichier a été sélectionné
    if file:
        # Stocke le chemin du fichier
        file_path.set(file)
