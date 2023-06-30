import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from enum import Enum

from tools import occurrence
from GuiClasses import FrameCSVLoader

# gui_windows : Opening 2 files, Input List 1, Input List 2, Output List
from GuiClasses import GlobalWindows
# gui_windows = [None, None, None, None]

# gui_liste : Input List 1, Input List 2, Output List
import GlobalLists
# gui_liste = [None, None, None]


# If the list is printed with only names (list), or with occurrencies (dict)
class WindowListState(Enum):
    NAMES = 1
    OCCURRENCIES = 2

# If the list is unsorted (0), or sorted alphabetically or by occurrencies
class WindowListSortState(Enum):
    UNKNOWN = 0
    SORTED_AtoZ = 1
    SORTED_ZtoA = 2
    SORTED_0to9 = 3
    SORTED_9to0 = 1

# Class for printing lists (input and output) and asking for load/save
class WindowList:
    GlobalListNumber = None

    ### States / Context
    # State (list in Name format only, or Name+Ocurrencies)
    State = None
    # SortState (list unsorted, sorted alphabetically, or by occurrencies)
    SortState = None

    ### GUI
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
    # Specifications of the window
    Geometry = "0"
    Title = "List Window"

    # def WindowListGenerator(self):
    def __init__(self, globallistnum, geometry):
        self.MainCanvas = tk.Tk()
        self.SetGeometry(geometry)
        self.GlobalListNumber = globallistnum
        self.State = WindowListState.NAMES
        self.SortState = WindowListSortState.UNKNOWN

        # Load CSV button
        self.LoadButton = tk.Button(self.MainCanvas,
                                    text="Load",
                                    state=tk.DISABLED,
                                    command=lambda: LoadFile(self.GlobalListNumber, self))
        self.LoadButton.pack()
        # Save CSV button
        self.SaveButton = tk.Button(self.MainCanvas,
                                    text="Save",
                                    state=tk.DISABLED,
                                    command=SaveFile)
        self.SaveButton.pack()

        # List CSV button
        self.ListButton = tk.Button(self.MainCanvas,
                                    text="Mode: Terms List",
                                    state=tk.NORMAL,
                                    command=lambda: self.InsertListInListBox(GlobalLists.gui_liste[self.GlobalListNumber]))
        self.ListButton.pack()

        # Occurence CSV button
        self.OccuButton = tk.Button(self.MainCanvas,
                                    text="Mode: Occurences",
                                    state=tk.NORMAL,
                                    command=lambda: self.InsertDictInListBox(occurrence(GlobalLists.gui_liste[self.GlobalListNumber])))
        self.OccuButton.pack()

        # Sort A->Z CSV button
        self.SortButton = tk.Button(self.MainCanvas,
                                    text="Sort (A -> Z)",
                                    state=tk.NORMAL,
                                    command=lambda: self.SortListInListBoxAlphabetically())
        self.SortButton.pack()

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

    # Specialize the Window List as an Input list (one of the 2 input CSV)
    #  List each term in its exact position (print only the terms)
    def SpecializedAsInputList(self):
        self.LoadButton.config(state=tk.NORMAL)
        self.SaveButton.config(state=tk.DISABLED)
        self.ListBox.delete(0, tk.END)

        self.InsertListInListBox(GlobalLists.gui_liste[self.GlobalListNumber])

    # Specialize the Window List as an Output list
    #  List the occurrencies of terms
    def SpecializedAsOutputList(self):
        self.LoadButton.config(state=tk.DISABLED)
        self.SaveButton.config(state=tk.NORMAL)
        self.ListBox.delete(0, tk.END)

        self.InsertDictInListBox(occurrence(GlobalLists.gui_liste[self.GlobalListNumber]))

    # Switch between the 2 states (NAMES <-> OCCURRENCIES)
    def StateSwitch(self):
        if (self.State == WindowListState.NAMES):
            self.State = WindowListState.OCCURRENCES
        else:
            self.State = WindowListState.NAMES

    # Switch the button from A->Z to Z->A (and vice versa)
    def UpdateSortAtoZButton(self):
        # If list is already in alphabetical, propose the reverse
        if (self.SortState == WindowListSortState.SORTED_AtoZ):
            self.SortButton.config(text="Sort (Z -> A)")
        else:
            self.SortButton.config(text="Sort (A -> Z)")

    # Insert a list of terms in the ListBox
    def InsertListInListBox(self, liste):
        self.ListBox.delete(0, tk.END)
        for element in liste:
            self.ListBox.insert(tk.END, element)
        self.State = WindowListState.NAMES

    # Insert a dictionnary (term:occ) in the ListBox
    def InsertDictInListBox(self, dico):
        self.ListBox.delete(0, tk.END)
        for valeur, compte in dico.items():
            texte = f"{valeur} : {compte} occurrence(s)"
            self.ListBox.insert(tk.END, texte)
        self.State = WindowListState.OCCURRENCIES

    # Sort (A <-> Z) the list of terms
    def SortListInListBoxAlphabetically(self):
        liste = GlobalLists.gui_liste[self.GlobalListNumber]
        if (self.State == WindowListState.NAMES):
            # List mode
            if (self.SortState != WindowListSortState.SORTED_AtoZ):
                # If the list is not sorted alphabetically...
                #  let's sort it!
                sorted_list = sorted(liste, reverse=False)
                self.SortState = WindowListSortState.SORTED_AtoZ
            else:
                # Else, let's revert the sort
                sorted_list = sorted(liste, reverse=True)
                self.SortState = WindowListSortState.SORTED_ZtoA
            self.InsertListInListBox(sorted_list)

        else:
            dico = occurrence(liste)
            # Occurrencies mode
            if (self.SortState != WindowListSortState.SORTED_AtoZ):
                # If the list is not sorted alphabetically...
                sorted_items = sorted(dico.items(), reverse=False)
                self.SortState = WindowListSortState.SORTED_AtoZ
            else:
                # Else, let's revert the sort
                sorted_items = sorted(dico.items(), reverse=True)
                self.SortState = WindowListSortState.SORTED_ZtoA
            self.InsertDictInListBox(dict(sorted_items))
        self.UpdateSortAtoZButton()

    ### Regular Methods of the class (setters, getters, quit, geometry, ...)

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

    # Hide the window
    def CallWithdraw(self):
        self.MainCanvas.withdraw()

    # Destroy the window
    def CallDestroy(self):
        self.MainCanvas.destroy()



# Callback for LoadButton
def LoadFile(NumList, TheWindowList):
    WindowLoad = tk.Tk()
    WindowLoad.title("Load CSV")
    WindowLoad.geometry("300x400+650+375")

    # Fill with the frame dedicated for loading CSV
    FrameLoad = FrameCSVLoader.FrameCSVLoader(WindowLoad, NumList)
    # Add the launch button & pack the frame
    FrameLoad.Reload_PutLaunchButton(TheWindowList)


# Callback for SaveButton
def SaveFile():
    WindowSave = tk.Tk()
    WindowSave.title("Save CSV")
    WindowSave.geometry("300x400+650+375")

    separator = tk.StringVar()
    choice = tk.StringVar()
    choice.set("List")

    SepLabel = tk.Label(WindowSave,
                        text="Separator:")
    SepLabel.pack()
    SepEntry = tk.Entry(WindowSave,
                        textvariable=separator)
    SepEntry.insert(0, ";")
    SepEntry.pack()

    ChoiceLabel = tk.Label(WindowSave,
                           text="Type of output :")
    ChoiceLabel.pack()

    RadioButton1 = tk.Radiobutton(WindowSave,
                                  text="List",
                                  variable=choice,
                                  value="List")
    RadioButton1.pack()
    RadioButton2 = tk.Radiobutton(WindowSave,
                                  text="Occurrencies",
                                  variable=choice,
                                  value="Occurrencies")
    RadioButton2.pack()

    LaunchButton = tk.Button(WindowSave,
                             text="Save",
                             command=lambda: save(SepEntry.get(),
                                                  GlobalLists.gui_liste[2],
                                                  choice.get(),
                                                  WindowSave))
    LaunchButton.pack()


def save(sep, data, choice, WindowSave):
    filename = filedialog.asksaveasfilename(filetypes=[("CSV Files", "*.csv")],
                                            defaultextension=".csv")
    fd = open(filename, 'w')
    if choice == "List":
        [fd.write("{0}\n".format(key)) for key in data]
    elif choice == "Occurrencies":
        occu = occurrence(data)
        [fd.write("{0}{1}{2}\n".format(key, sep, value)) for key, value in occu.items()]
    fd.close()

    WindowSave.destroy()
