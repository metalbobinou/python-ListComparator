import tkinter as tk
from GuiClasses import WindowList
from logic_processing import union
from logic_processing import inter
from logic_processing import unique
from logic_processing import inv_inter
from logic_processing import smart_union
from logic_processing import unique_without_occurrence

# gui_windows : Opening 2 files, Input List 1, Input List 2, Output List
from GuiClasses import GlobalWindows
# gui_windows = [None, None, None, None]

# gui_liste : Input List 1, Input List 2, Output List
import GlobalLists
# gui_liste = [None, None, None]


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
        self.Buttons.append(tk.Button(self.MainCanvas,
                                      text="Intersection des 2 csv",
                                      command=inter_window))
        self.Buttons[-1].pack()
        self.Buttons.append(tk.Button(self.MainCanvas,
                                      text="Union des 2 csv",
                                      command=union_window))
        self.Buttons[-1].pack()
        self.Buttons.append(tk.Button(self.MainCanvas,
                                      text="Valeurs propre au premier csv",
                                      command=unique_1_window))
        self.Buttons[-1].pack()
        self.Buttons.append(tk.Button(self.MainCanvas,
                                      text="Valeurs propre au deuxième csv",
                                      command=unique_2_window))
        self.Buttons[-1].pack()
        self.Buttons.append(tk.Button(self.MainCanvas,
                                      text="Valeurs propre au deuxième csv (occurrence)",
                                      command=unique_1_occu_window))
        self.Buttons[-1].pack()
        self.Buttons.append(tk.Button(self.MainCanvas,
                                      text="Valeurs propre au deuxième csv (occurrence)",
                                      command=unique_2_occu_window))
        self.Buttons[-1].pack()
        self.Buttons.append(tk.Button(self.MainCanvas,
                                      text="Inverse intersection des 2 csv",
                                      command=inv_inter_window))
        self.Buttons[-1].pack()
        self.Buttons.append(tk.Button(self.MainCanvas,
                                      text="Smart union des 2 csv",
                                      command=smart_union_window))
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

    if GlobalWindows.gui_windows[3] is not None:
        GlobalWindows.gui_windows[3].CallWithdraw()
        del GlobalWindows.gui_windows[3]
        GlobalWindows.gui_windows.append(None)

    GlobalLists.gui_liste[2] = inter(GlobalLists.gui_liste[0],
                                     GlobalLists.gui_liste[1])

    # Crée un canevas pour afficher les résultats
    GlobalWindows.gui_windows[3] = WindowList.WindowList(2,
                                                         "300x400+650+300")
    GlobalWindows.gui_windows[3].SetTitle("Intersection des BN_ID des deux CSV")
    GlobalWindows.gui_windows[3].SpecializedAsOutputList()


def union_window():
    global gui_windows, gui_liste

    if GlobalWindows.gui_windows[3] is not None:
        # gui_windows[3].withdraw()
        GlobalWindows.gui_windows[3].CallWithdraw()
        del GlobalWindows.gui_windows[3]
        GlobalWindows.gui_windows.append(None)

    GlobalLists.gui_liste[2] = union(GlobalLists.gui_liste[0],
                                     GlobalLists.gui_liste[1])

    # Crée un canevas pour afficher les résultats
    GlobalWindows.gui_windows[3] = WindowList.WindowList(2,
                                                         "300x400+650+300")
    GlobalWindows.gui_windows[3].SetTitle("Union des BN_ID des deux CSV")
    GlobalWindows.gui_windows[3].SpecializedAsOutputList()


def unique_1_window():
    global gui_windows, gui_liste

    if GlobalWindows.gui_windows[3] is not None:
        # gui_windows[3].withdraw()
        GlobalWindows.gui_windows[3].CallWithdraw()
        del GlobalWindows.gui_windows[3]
        GlobalWindows.gui_windows.append(None)

    GlobalLists.gui_liste[2] = unique_without_occurrence(GlobalLists.gui_liste[0],
                                      GlobalLists.gui_liste[1], 1)

    # Crée un canevas pour afficher les résultats
    GlobalWindows.gui_windows[3] = WindowList.WindowList(2,
                                                         "300x400+650+300")
    GlobalWindows.gui_windows[3].SetTitle("Valeur propre au premier CSV")
    GlobalWindows.gui_windows[3].SpecializedAsOutputList()


def unique_2_window():
    global gui_windows, gui_liste

    if GlobalWindows.gui_windows[3] is not None:
        # gui_windows[3].withdraw()
        GlobalWindows.gui_windows[3].CallWithdraw()
        del GlobalWindows.gui_windows[3]
        GlobalWindows.gui_windows.append(None)

    GlobalLists.gui_liste[2] = unique_without_occurrence(GlobalLists.gui_liste[0],
                                      GlobalLists.gui_liste[1], 2)

    # Crée un canevas pour afficher les résultats
    GlobalWindows.gui_windows[3] = WindowList.WindowList(2,
                                                         "300x400+650+300")
    GlobalWindows.gui_windows[3].SetTitle("Valeur propre au deuxième CSV")
    GlobalWindows.gui_windows[3].SpecializedAsOutputList()


def unique_1_occu_window():
    global gui_windows, gui_liste

    if GlobalWindows.gui_windows[3] is not None:
        # gui_windows[3].withdraw()
        GlobalWindows.gui_windows[3].CallWithdraw()
        del GlobalWindows.gui_windows[3]
        GlobalWindows.gui_windows.append(None)

    GlobalLists.gui_liste[2] = unique(GlobalLists.gui_liste[0],
                                      GlobalLists.gui_liste[1], 1)

    # Crée un canevas pour afficher les résultats
    GlobalWindows.gui_windows[3] = WindowList.WindowList(2,
                                                         "300x400+650+300")
    GlobalWindows.gui_windows[3].SetTitle("Valeur propre au premier CSV (occurrence)")
    GlobalWindows.gui_windows[3].SpecializedAsOutputList()


def unique_2_occu_window():
    global gui_windows, gui_liste

    if GlobalWindows.gui_windows[3] is not None:
        # gui_windows[3].withdraw()
        GlobalWindows.gui_windows[3].CallWithdraw()
        del GlobalWindows.gui_windows[3]
        GlobalWindows.gui_windows.append(None)

    GlobalLists.gui_liste[2] = unique(GlobalLists.gui_liste[0],
                                      GlobalLists.gui_liste[1], 2)

    # Crée un canevas pour afficher les résultats
    GlobalWindows.gui_windows[3] = WindowList.WindowList(2,
                                                         "300x400+650+300")
    GlobalWindows.gui_windows[3].SetTitle("Valeur propre au deuxième CSV (occurrence)")
    GlobalWindows.gui_windows[3].SpecializedAsOutputList()


def inv_inter_window():
    global gui_windows, gui_liste

    if GlobalWindows.gui_windows[3] is not None:
        # gui_windows[3].withdraw()
        GlobalWindows.gui_windows[3].CallWithdraw()
        del GlobalWindows.gui_windows[3]
        GlobalWindows.gui_windows.append(None)

    GlobalLists.gui_liste[2] = inv_inter(GlobalLists.gui_liste[0],
                                         GlobalLists.gui_liste[1])

    # Crée un canevas pour afficher les résultats
    GlobalWindows.gui_windows[3] = WindowList.WindowList(2,
                                                         "300x400+650+300")
    GlobalWindows.gui_windows[3].SetTitle("Inverse de l'intersection des BN_ID des deux CSV")
    GlobalWindows.gui_windows[3].SpecializedAsOutputList()


def smart_union_window():
    global gui_windows, gui_liste

    if GlobalWindows.gui_windows[3] is not None:
        # gui_windows[3].withdraw()
        GlobalWindows.gui_windows[3].CallWithdraw()
        del GlobalWindows.gui_windows[3]
        GlobalWindows.gui_windows.append(None)

    GlobalLists.gui_liste[2] = smart_union(GlobalLists.gui_liste[0],
                                           GlobalLists.gui_liste[1])

    # Crée un canevas pour afficher les résultats
    GlobalWindows.gui_windows[3] = WindowList.WindowList(2,
                                                         "300x400+650+300")
    GlobalWindows.gui_windows[3].SetTitle("Smart union des BN_ID des deux CSV")
    GlobalWindows.gui_windows[3].SpecializedAsOutputList()
