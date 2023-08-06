import sys

# Tkinter GUI
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Windows for input lists
from GuiClasses import WindowList

# Plugin loader
from plugins_loader import PluginsImporter

# Logic operators
from basic_set_operators import ListSetOperators
from basic_occurrencies_operators import ListOccurrenciesOperators
from basic_various_operators import ListVariousOperators

# Globals required for the GUI
from GuiClasses import Globals
# gui_liste :  [0]:Input List 1  [1]:Input List 2  [2]:Output List
# gui_liste = [None, None, None]


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
    # Labels
    Labels = []
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

        self.AddSeparator()
        self.AddLabel("Occurrencies/Categories")

        for cls in ListOccurrenciesOperators():
            button_str = str(cls.GetButton(cls))
            name_str = str(cls.GetName(cls))
            self.AddButton(button_str[0:32], lambda x=name_str[0:32] : CallBackAction(x))

        self.AddSeparator()
        self.AddLabel("Sets (no occurrencies)")

        for cls in ListSetOperators():
            button_str = str(cls.GetButton(cls))
            name_str = str(cls.GetName(cls))
            self.AddButton(button_str[0:32], lambda x=name_str[0:32] : CallBackAction(x))

        self.AddSeparator()
        self.AddLabel("Various")

        for cls in ListVariousOperators():
            button_str = str(cls.GetButton(cls))
            name_str = str(cls.GetName(cls))
            self.AddButton(button_str[0:32], lambda x=name_str[0:32] : CallBackAction(x))

        self.AddSeparator()
        self.AddLabel("Plugins")

        for cls in Globals.MyPluginsImporter.GetClasses():
            button_str = str(cls.GetButton(cls))
            name_str = str(cls.GetName(cls))
            self.AddButton(button_str[0:32], lambda x=name_str[0:32] : CallBackAction(x))


    ## Add a button in the frame
    def AddButton(self, Text, Command):
        self.Buttons.append(tk.Button(self.Frame,
                                      text=Text,
                                      command=Command))
        self.Buttons[-1].pack(side=tk.TOP,
                              fill=tk.X)

    ## Add a label in the frame
    def AddLabel(self, Text):
        self.Labels.append(tk.ttk.Label(self.Frame,
                                        text=Text))
        self.Labels[-1].pack(expand=True,
                             pady=5)

    ## Add a separator in the frame
    def AddSeparator(self):
        self.Separators.append(tk.ttk.Separator(self.Frame,
                                                orient=tk.HORIZONTAL))
        self.Separators[-1].pack(side=tk.TOP,
                                 fill=tk.X,
                                 pady=5)

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


## Callback for when an action button is clicked
def CallBackAction(action):
    CloseOutWindow()

    # Put Occurrencies and Set in the list of operators
    operators = ListOccurrenciesOperators() + ListSetOperators() + ListVariousOperators()
    # Add plugins in the list of operators
    operators = operators + Globals.MyPluginsImporter.GetClasses()

    for cls in operators:
        verb = str(cls.GetName(cls))
        if (action == verb[0:32]):
            res = cls.Logic(cls, Globals.gui_liste[0], Globals.gui_liste[1])
            break

    Globals.gui_liste[2] = res

    # Open a new Window List specialized as OutputList / FrameCSVSaver
    Globals.gui_out_window = WindowList.WindowList(2,
                                                   "300x400+650+375")
    Globals.gui_out_window.SetTitle(action)
    Globals.gui_out_window.SpecializedAsOutputList()


# Procedure for closing the output window (before reopening it)
def CloseOutWindow():
    if (not (Globals.gui_out_window is None)):
        # Globals.gui_out_window.withdraw()
        Globals.gui_out_window.CallWithdraw()
        del Globals.gui_out_window
        Globals.gui_out_window = None

# Callback called when clicking on closing
def on_closing(TheWindow):
    if (messagebox.askokcancel("Quit", "Do you want to quit?")):
        #TheWindow.CallDestroy()
        sys.exit(0)

# Insert data in a dictionnary
def insert_data(data, dictio):
    for valeur, compte in dictio.items():
        texte = f"{valeur} : {compte} occurrence(s)"
        data.insert(0, texte)
