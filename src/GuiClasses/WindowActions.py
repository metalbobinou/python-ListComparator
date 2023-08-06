# Tkinter GUI
import tkinter as tk
from tkinter import ttk
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
    # Root Window
    Root = None
    # Canvas getting the Frame & Internal Canvas
    Canvas = None
    # Frame for putting scrollbars
    FrameMain = None
    FrameScrollbar = None
    # Frame for buttons and others
    Frame = None
    # Scrollbars
    Scrollbar_X = None
    Scrollbar_Y = None
    # Buttons for launching actions (set operations)
    Buttons = []
    # Separators
    Separators = []
    # ListBox with the data
    #ListBox = None

    # Output WindowList that can be destroy as wished
    OutWindow = None

    def __init__(self, geometry):
        self.Root = tk.Tk()

        self.SetTitle("Actions")
        self.SetGeometry(geometry)

        ## Frame Main [in root]
        self.FrameMain = ttk.Frame(self.Root)
        self.FrameMain.pack(fill=tk.BOTH,
                            expand=True)
        ## Frame for the scrollbar [in FrameMain]
        self.FrameScrollbar = ttk.Frame(self.FrameMain)
        self.FrameScrollbar.pack(side=tk.BOTTOM,
                                 fill=tk.X)
        ## Canvas [in FrameMain]
        self.Canvas = tk.Canvas(self.FrameMain)
        self.Canvas.pack(side=tk.LEFT,
                         fill=tk.BOTH,
                         expand=True)

        ## Scrollbar in the Canvas [in FrameScrollbar and FrameMain]
        #self.Scrollbar_X = ttk.Scrollbar(self.FrameScrollbar,
        #                                 orient=tk.HORIZONTAL,
        #                                 command=self.Canvas.xview)
        #self.Scrollbar_X.pack(side=tk.BOTTOM,
        #                      fill=tk.X)
        self.Scrollbar_Y = ttk.Scrollbar(self.FrameMain,
                                         orient=tk.VERTICAL,
                                         command=self.Canvas.yview)
        self.Scrollbar_Y.pack(side=tk.RIGHT,
                              fill=tk.Y)

        ## Configure the Canvas
        #self.Canvas.configure(xscrollcommand=self.Scrollbar_X.set)
        self.Canvas.configure(yscrollcommand=self.Scrollbar_Y.set)
        self.Canvas.bind("<Configure>",
                         lambda e : self.Canvas.config(scrollregion=self.Canvas.bbox(tk.ALL)))

        ## Frame internal (that will contain buttons) [in Canvas]
        self.Frame = ttk.Frame(self.Canvas)
        ## add a window to that frame in the canvas
        self.Canvas.create_window((0,0),
                                  window=self.Frame,
                                  anchor="nw")

        ######################################
        ### Put the separators and buttons ###
        ######################################
        self.__PutSeparatorsAndButtons()
        ######################################

        ## Separator
        self.AddSeparator()

        ## Exit button
        self.Buttons.append(tk.Button(self.Frame,
                                      text="Quit",
                                      command=lambda: on_closing(self)))
        self.Buttons[-1].pack()
        ## Catch the exit signal on the window ('X' in right corner)
        self.Root.protocol("WM_DELETE_WINDOW",
                           lambda: on_closing(self))


    ## Put the separators and buttons
    def __PutSeparatorsAndButtons(self):
        ## Loading buttons [in Frame]
        ## [Currently hardcoded]
        ## TODO : loading as much buttons as there are operations in the operations file

        self.AddButton("Intersection des 2 csv", inter_window)
        self.AddButton("Union des 2 csv", union_window)
        self.AddButton("Union Disjointe des 2 csv", disjoint_union_window)

        self.AddButton("Valeurs propre au premier csv", unique_1_window)
        self.AddButton("Valeurs propre au deuxième csv", unique_2_window)
        self.AddButton("Valeurs propre au premier csv (occurrence)", unique_1_occu_window)
        self.AddButton("Valeurs propre au deuxième csv (occurrence)", unique_2_occu_window)

        self.AddButton("Inverse intersection des 2 csv", inv_inter_window)


    ## Add a button in the frame
    def AddButton(self, Text, Command):
        self.Buttons.append(tk.Button(self.Frame,
                                      text=Text,
                                      command=Command))
        self.Buttons[-1].pack()

    ## Add a separator in the frame
    def AddSeparator(self):
        self.Separators.append(tk.ttk.Separator(self.Frame,
                                                orient=tk.HORIZONTAL))
        self.Separators[-1].pack(fill=tk.X)

    ## Regular Setters and Getters
    def SetTitle(self, title):
        self.Title = title
        self.Root.title(title)

    def SetGeometry(self, geometry):
        self.Geometry = geometry
        self.Root.geometry(geometry)

    def GetGeometry(self):
        return (self.Geometry)

    def GetTitle(self):
        return (self.Title)

    ## Window loop and destroyers
    def CallMainloop(self):
        self.Root.mainloop()

    def CallWithdraw(self):
        self.Root.withdraw()

    def CallDestroy(self):
        self.Root.destroy()


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
