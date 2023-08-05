# Tkinter GUI
import tkinter as tk
from tkinter import messagebox

# Windows for input lists
from GuiClasses import WindowList

# Logic operations
from logic_processing import union
from logic_processing import inter
from logic_processing import unique
from logic_processing import inv_inter
from logic_processing import disjoint_union
from logic_processing import unique_without_occurrence

# Globals required for the GUI
from GuiClasses import Globals
# gui_liste :  [0]:Input List 1  [1]:Input List 2  [2]:Output List
# gui_liste = [None, None, None]

from GuiClasses import GlobalWindows
# gui_windows : Opening 2 files, Input List 1, Input List 2, Output List
# gui_windows = [None, None, None, None]

# Insert data in a dictionnary
def insert_data(data, dictio):
    for valeur, compte in dictio.items():
        texte = f"{valeur} : {compte} occurrence(s)"
        data.insert(0, texte)


# Class for proposing as much buttons as available operations on sets
class WindowActions:
    Geometry = "0"
    Title = "CSV List Comparator"
    # Canvas getting the whole window
    MainCanvas = None
    # Buttons for launching actions (set operations)
    Buttons = []
    # Separators
    Separators = []
    # Frame for putting scrollbar and list inside
    Frame = None
    # Right scrollbar
    Scrollbar = None
    # ListBox with the data
    ListBox = None

    # Output WindowList that can be destroy as wished
    OutWindow = None

    def __init__(self, geometry):
        self.MainCanvas = tk.Tk()

        self.SetGeometry(geometry)

        # Loading buttons
        # [Currently hardcoded]
        # TODO : loading as much buttons as there are operations in the operations file

        self.AddButton("Intersection des 2 csv", inter_window)
        self.AddButton("Union des 2 csv", union_window)
        self.AddButton("Union Disjointe des 2 csv", disjoint_union_window)

        self.AddButton("Valeurs propre au premier csv", unique_1_window)
        self.AddButton("Valeurs propre au deuxième csv", unique_2_window)
        self.AddButton("Valeurs propre au premier csv (occurrence)", unique_1_occu_window)
        self.AddButton("Valeurs propre au deuxième csv (occurrence)", unique_2_occu_window)

        self.AddButton("Inverse intersection des 2 csv", inv_inter_window)

        # Separate
        self.Separators.append(tk.ttk.Separator(self.MainCanvas,
                                                orient='horizontal'))
        self.Separators[-1].pack(fill='x')

        # Add Exit button
        self.Buttons.append(tk.Button(self.MainCanvas,
                                      text="Quit",
                                      command=lambda: on_closing(self)))
        self.Buttons[-1].pack()
        # Catch the exit signal on the window ('X' in right corner)
        self.MainCanvas.protocol("WM_DELETE_WINDOW",
                                 lambda: on_closing(self))

    def AddButton(self, Text, Command):
        self.Buttons.append(tk.Button(self.MainCanvas,
                                      text=Text,
                                      command=Command))
        self.Buttons[-1].pack()

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

    def CallMainloop(self):
        self.MainCanvas.mainloop()

    def CallWithdraw(self):
        self.MainCanvas.withdraw()

    def CallDestroy(self):
        self.MainCanvas.destroy()


def inter_window():
    global gui_windows, gui_liste

    CheckWindows3(GlobalWindows.gui_windows[3])

    Globals.gui_liste[2] = inter(Globals.gui_liste[0],
                                 Globals.gui_liste[1])

    # Crée un canevas pour afficher les résultats
    GlobalWindows.gui_windows[3] = WindowList.WindowList(2,
                                                         "300x400+650+375")
    GlobalWindows.gui_windows[3].SetTitle("Intersection des BN_ID des deux CSV")
    GlobalWindows.gui_windows[3].SpecializedAsOutputList()


def union_window():
    global gui_windows, gui_liste

    CheckWindows3(GlobalWindows.gui_windows[3])

    Globals.gui_liste[2] = union(Globals.gui_liste[0],
                                 Globals.gui_liste[1])

    # Crée un canevas pour afficher les résultats
    GlobalWindows.gui_windows[3] = WindowList.WindowList(2,
                                                         "300x400+650+375")
    GlobalWindows.gui_windows[3].SetTitle("Union des BN_ID des deux CSV")
    GlobalWindows.gui_windows[3].SpecializedAsOutputList()


def unique_1_window():
    global gui_windows, gui_liste

    CheckWindows3(GlobalWindows.gui_windows[3])

    Globals.gui_liste[2] = unique_without_occurrence(Globals.gui_liste[0],
                                                     Globals.gui_liste[1], 1)

    # Crée un canevas pour afficher les résultats
    GlobalWindows.gui_windows[3] = WindowList.WindowList(2,
                                                         "300x400+650+375")
    GlobalWindows.gui_windows[3].SetTitle("Valeur propre au premier CSV")
    GlobalWindows.gui_windows[3].SpecializedAsOutputList()


def unique_2_window():
    global gui_windows, gui_liste

    CheckWindows3(GlobalWindows.gui_windows[3])

    Globals.gui_liste[2] = unique_without_occurrence(Globals.gui_liste[0],
                                                     Globals.gui_liste[1], 2)

    # Crée un canevas pour afficher les résultats
    GlobalWindows.gui_windows[3] = WindowList.WindowList(2,
                                                         "300x400+650+375")
    GlobalWindows.gui_windows[3].SetTitle("Valeur propre au deuxième CSV")
    GlobalWindows.gui_windows[3].SpecializedAsOutputList()


def unique_1_occu_window():
    global gui_windows, gui_liste

    CheckWindows3(GlobalWindows.gui_windows[3])

    Globals.gui_liste[2] = unique(Globals.gui_liste[0],
                                  Globals.gui_liste[1], 1)

    # Crée un canevas pour afficher les résultats
    GlobalWindows.gui_windows[3] = WindowList.WindowList(2,
                                                         "300x400+650+375")
    GlobalWindows.gui_windows[3].SetTitle("Valeur propre au premier CSV (occurrence)")
    GlobalWindows.gui_windows[3].SpecializedAsOutputList()


def unique_2_occu_window():
    global gui_windows, gui_liste

    CheckWindows3(GlobalWindows.gui_windows[3])

    Globals.gui_liste[2] = unique(Globals.gui_liste[0],
                                  Globals.gui_liste[1], 2)

    # Crée un canevas pour afficher les résultats
    GlobalWindows.gui_windows[3] = WindowList.WindowList(2,
                                                         "300x400+650+375")
    GlobalWindows.gui_windows[3].SetTitle("Valeur propre au deuxième CSV (occurrence)")
    GlobalWindows.gui_windows[3].SpecializedAsOutputList()


def inv_inter_window():
    global gui_windows, gui_liste

    CheckWindows3(GlobalWindows.gui_windows[3])

    Globals.gui_liste[2] = inv_inter(Globals.gui_liste[0],
                                     Globals.gui_liste[1])

    # Crée un canevas pour afficher les résultats
    GlobalWindows.gui_windows[3] = WindowList.WindowList(2,
                                                         "300x400+650+375")
    GlobalWindows.gui_windows[3].SetTitle("Inverse de l'intersection des BN_ID des deux CSV")
    GlobalWindows.gui_windows[3].SpecializedAsOutputList()


def disjoint_union_window():
    global gui_windows, gui_liste

    CheckWindows3(GlobalWindows.gui_windows[3])

    Globals.gui_liste[2] = disjoint_union(Globals.gui_liste[0],
                                          Globals.gui_liste[1])

    # Crée un canevas pour afficher les résultats
    GlobalWindows.gui_windows[3] = WindowList.WindowList(2,
                                                         "300x400+650+375")
    GlobalWindows.gui_windows[3].SetTitle("Union Disjointe des BN_ID des deux CSV")
    GlobalWindows.gui_windows[3].SpecializedAsOutputList()


def CheckWindows3(Window):
    global gui_windows

    if Window is not None:
        # gui_windows[3].withdraw()
        Window.CallWithdraw()
        del Window
        GlobalWindows.gui_windows.append(None)

def on_closing(TheWindow):
    if (messagebox.askokcancel("Quit", "Do you want to quit?")):
        #TheWindow.CallDestroy()
        exit(0)
