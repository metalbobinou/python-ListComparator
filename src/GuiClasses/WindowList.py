import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from enum import Enum

from tools import occurrence
from GuiClasses import FrameCSVLoader
from GuiClasses import FrameCSVSaver

# gui_windows : Opening 2 files, Input List 1, Input List 2, Output List
from GuiClasses import GlobalWindows
# gui_windows = [None, None, None, None]

# gui_liste : Input List 1, Input List 2, Output List
import GlobalLists
# gui_liste = [None, None, None]


# If the list is printed with only names (list), or with occurrencies (dict)
class WindowListState(Enum):
    TERMS = 1
    OCCURRENCIES = 2

# If the list is unsorted (0), or sorted alphabetically or by occurrencies
class WindowListSortState(Enum):
    UNKNOWN = 0
    SORTED_AtoZ = 1
    SORTED_ZtoA = 2
    SORTED_0to9 = 3
    SORTED_9to0 = 4

# Class for printing lists (input and output) and asking for load/save
class WindowList:
    GlobalListNumber = None

    ### States / Context
    # Context (Input list or Output list)
    Context = None
    # State (list in Name format only, or Name+Ocurrencies)
    State = None
    # SortState (list unsorted, sorted alphabetically, or by occurrencies)
    SortState = None

    ### GUI
    # Canvas getting the whole window
    MainCanvas = None
    # Specifications of the window
    Geometry = "0"
    Title = "List Window"

    # Load/Save buttons in the window
    FrameLoadSave = None
    LoadButton = None
    SaveButton = None
    # Format list buttons
    FrameFormatList = None
    FormatTermButton = None
    FormatOccButton = None
    # Sorts buttons
    FrameSorts = None
    SortAlphaButton = None
    SortNumButton = None
    # List of terms
    FrameListBox = None
    ScrollbarListBox = None
    ListBox = None

    # def WindowListGenerator(self):
    def __init__(self, globallistnum, geometry):
        self.MainCanvas = tk.Tk()
        self.SetGeometry(geometry)
        self.GlobalListNumber = globallistnum
        self.State = WindowListState.TERMS
        self.SortState = WindowListSortState.UNKNOWN

        ### Load / Save
        # Frame for Load and Save
        self.FrameLoadSave = ttk.Frame(self.MainCanvas)
        self.FrameLoadSave.pack(side=tk.TOP,
                                fill=tk.X,
                                expand=tk.YES,
                                anchor=tk.N)
        # Load CSV button
        self.LoadButton = tk.Button(self.FrameLoadSave,
                                    text="Load",
                                    state=tk.DISABLED,
                                    command=lambda: LoadFile(self.GlobalListNumber, self))
        self.LoadButton.pack(side=tk.LEFT,
                             fill=tk.X,
                             expand=tk.YES,
                             anchor=tk.NW)
        # Save CSV button
        self.SaveButton = tk.Button(self.FrameLoadSave,
                                    text="Save",
                                    state=tk.DISABLED,
                                    command=lambda: SaveFile(self.GlobalListNumber, self))
        self.SaveButton.pack(side=tk.RIGHT,
                             fill=tk.X,
                             expand=tk.YES,
                             anchor=tk.NE)

        ### Format Terms/Occurrencies
        # Frame for two modes
        self.FrameFormatList = ttk.Frame(self.MainCanvas)
        self.FrameFormatList.pack(side=tk.TOP,
                                  fill=tk.X,
                                  expand=tk.YES,
                                  anchor=tk.N)
        # Button format list as Terms list
        self.FormatTermButton = tk.Button(self.FrameFormatList,
                                          text="Mode:\nTerms List",
                                          state=tk.NORMAL,
                                          command=lambda: self.InsertListInListBox(GlobalLists.gui_liste[self.GlobalListNumber]))
        self.FormatTermButton.pack(side=tk.LEFT,
                             fill=tk.X,
                             expand=tk.YES,
                             anchor=tk.NW)
        # Button format list as Occurrencies list
        self.FormatOccButton = tk.Button(self.FrameFormatList,
                                         text="Mode:\nOccurrences",
                                         state=tk.NORMAL,
                                         command=lambda: self.InsertDictInListBox(occurrence(GlobalLists.gui_liste[self.GlobalListNumber])))
        self.FormatOccButton.pack(side=tk.RIGHT,
                             fill=tk.X,
                             expand=tk.YES,
                             anchor=tk.NE)

        ### Sorts buttons
        # Frame for sorting by alphabetical and numerical orders
        self.FrameSorts = ttk.Frame(self.MainCanvas)
        self.FrameSorts.pack(side=tk.TOP,
                             fill=tk.X,
                             expand=tk.YES,
                             anchor=tk.N)
        # Sort A->Z CSV button
        self.SortAlphaButton = tk.Button(self.FrameSorts,
                                         text="Sort [Alphabetical]",
                                         state=tk.NORMAL,
                                         command=lambda: self.SortListInListBoxAlphabetically())
        self.SortAlphaButton.pack(side=tk.RIGHT,
                                  fill=tk.X,
                                  expand=tk.YES,
                                  anchor=tk.NW)
        self.UpdateSortAtoZButton()
        # Sort 0->9 CSV button
        self.SortNumButton = tk.Button(self.FrameSorts,
                                       text="Sort [Numerical]",
                                       state=tk.DISABLED,
                                       command=lambda: self.SortListInListBoxNumerically())
        self.SortNumButton.pack(side=tk.RIGHT,
                                fill=tk.X,
                                expand=tk.YES,
                                anchor=tk.NE)
        self.UpdateSort0to9Button()

        ### ListBox containing the list of terms
        # Frame for containing the list
        self.FrameListBox = ttk.Frame(self.MainCanvas)
        self.FrameListBox.pack(fill=tk.BOTH,
                               expand=True)
        # Scrollbar for the list
        self.ScrollbarListBox = ttk.Scrollbar(self.FrameListBox,
                                              orient=tk.VERTICAL)
        # ListBox containing the list
        self.ListBox = tk.Listbox(self.FrameListBox,
                                  yscrollcommand=self.ScrollbarListBox.set)
        self.ListBox.pack(side=tk.LEFT,
                          fill=tk.BOTH,
                          expand=True)
        # Configure the scrollbar for expanding with the list
        self.ScrollbarListBox.config(command=self.ListBox.yview)
        self.ScrollbarListBox.pack(side=tk.RIGHT,
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


    # Switch between the 2 states (TERMS <-> OCCURRENCIES)
    def StateSwitch(self):
        if (self.State == WindowListState.TERMS):
            self.State = WindowListState.OCCURRENCES
        else:
            self.State = WindowListState.TERMS

    # Switch the button from A->Z to Z->A (and vice versa)
    def UpdateSortAtoZButton(self):
        # If list is already in alphabetical, propose the reverse
        if (self.SortState == WindowListSortState.SORTED_AtoZ):
            self.SortAlphaButton.config(text="Sort (Z -> A)")
        else:
            self.SortAlphaButton.config(text="Sort (A -> Z)")

    # Switch the button from 0->9 to 0->9 (and vice versa)
    def UpdateSort0to9Button(self):
        # If list is already in alphabetical, propose the reverse
        if (self.SortState == WindowListSortState.SORTED_0to9):
            self.SortNumButton.config(text="Sort (9 -> 0)")
        else:
            self.SortNumButton.config(text="Sort (0 -> 9)")

    # Sort (A <-> Z) the list of terms
    def SortListInListBoxAlphabetically(self):
        liste = GlobalLists.gui_liste[self.GlobalListNumber]
        if (self.State == WindowListState.TERMS):
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

    # Sort (0 <-> 9) the list of terms
    def SortListInListBoxNumerically(self):
        liste = GlobalLists.gui_liste[self.GlobalListNumber]
        if (self.State == WindowListState.OCCURRENCIES):
            dico = occurrence(liste)
            # Occurrencies mode
            if (self.SortState != WindowListSortState.SORTED_0to9):
                # If the list is not sorted numerically...
                sorted_items = sorted(dico.items(), key=lambda x:x[1], reverse=False)
                self.SortState = WindowListSortState.SORTED_0to9
            else:
                # Else, let's revert the sort
                sorted_items = sorted(dico.items(), key=lambda x:x[1], reverse=True)
                self.SortState = WindowListSortState.SORTED_9to0
            self.InsertDictInListBox(dict(sorted_items))
        else:
            # Terms mode
            test = None
        self.UpdateSort0to9Button()


    # Insert a list of terms in the ListBox
    def InsertListInListBox(self, liste):
        self.ListBox.delete(0, tk.END)
        for element in liste:
            self.ListBox.insert(tk.END, element)
        self.State = WindowListState.TERMS
        self.SortNumButton.config(state=tk.DISABLED)

    # Insert a dictionnary (term:occ) in the ListBox
    def InsertDictInListBox(self, dico):
        self.ListBox.delete(0, tk.END)
        for valeur, compte in dico.items():
            texte = f"{valeur} : {compte} occurrence(s)"
            self.ListBox.insert(tk.END, texte)
        self.State = WindowListState.OCCURRENCIES
        self.SortNumButton.config(state=tk.NORMAL)


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
    WindowLoad.geometry("300x220+600+375")

    # Fill with the frame dedicated for loading CSV
    FrameLoad = FrameCSVLoader.FrameCSVLoader(WindowLoad, NumList)
    # Add the launch button & pack the frame
    FrameLoad.Reload_PutLaunchButton(TheWindowList)

    WindowLoad.mainloop()

# Callback for SaveButton
def SaveFile(NumList, TheWindowList):
    WindowSave = tk.Tk()
    WindowSave.title("Save CSV")
    WindowSave.geometry("250x200+600+375")

    # Create a frame
    FrameSave = FrameCSVSaver.FrameCSVSaver(WindowSave, NumList)
    # Add the save button & pack the frame
    FrameSave.Save_PutSaveButton(WindowSave)

    WindowSave.mainloop()
