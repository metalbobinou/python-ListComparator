import tkinter as tk
from tkinter import filedialog
import os.path
from enum import Enum

from GuiClasses import WindowError
from csv_manipulate import load_csv
from tools import occurrence

# gui_liste : Input List 1, Input List 2, Output List
import GlobalLists
# gui_liste = [None, None, None]


# Choice of the output style : terms ? or terms;occ ?
class ChoiceModeType(Enum):
    TERMS = 1
    OCCURRENCIES = 2

# Frame asking for informations about a CSV (path, sep, col)
class FrameCSVSaver:
    GlobalListNumber = None

    # Values we want to get from the user (tk.StringVar())
    Separator = None
    ModeType = None
    Filename = None

    ### GUI
    # The current frame
    Frame = None
    # Canvas where to put the current frame
    OutterCanvas = None
    # Specifications of the current frame
    Geometry = None
    Padding = None
    BorderWidth = None
    Relief = None
    # Widgets of the frame
    SeparatorLabel = None
    SeparatorEntry = None
    ModeTypeLabel = None
    ModeTypeRadioButton1 = None
    ModeTypeRadioButton2 = None
    # Widgets for saving into a CSV
    SaveButton = None

    def __init__(self, canvas, ListNum=None):
        # Get the canvas where to put the frame
        self.OutterCanvas = canvas
        self.GlobalListNumber = ListNum

        self.Frame = tk.Frame(self.OutterCanvas)

        # Fill variables
        self.Separator = tk.StringVar()
        self.ModeType = tk.IntVar(self.Frame)
        self.Filename = tk.StringVar()

        # Separator Description and Field
        self.SeparatorLabel = tk.Label(self.Frame,
                                       text="Separator:")
        self.SeparatorLabel.pack()
        self.SeparatorEntry = tk.Entry(self.Frame,
                                       textvariable=self.Separator)
        self.SeparatorEntry.insert(0, ";")
        self.SeparatorEntry.pack()

        # Output choice list type : terms ? or terms;occ ?
        self.ModeTypeLabel = tk.Label(self.Frame,
                                      text="Type of output:")
        self.ModeTypeLabel.pack()
        # Radio button : List
        self.ModeTypeRadioButton1 = tk.Radiobutton(self.Frame,
                                                   text="Terms only",
                                                   variable=self.ModeType,
                                                   value=ChoiceModeType.TERMS.value)
        self.ModeTypeRadioButton1.pack()
        # Radio button : Occurrencies
        self.ModeTypeRadioButton2 = tk.Radiobutton(self.Frame,
                                                   text="Occurrencies",
                                                   variable=self.ModeType,
                                                   value=ChoiceModeType.OCCURRENCIES.value)
        self.ModeTypeRadioButton2.pack()

        # Default : Terms list
        #self.ModeType.set(ChoiceModeType.TERMS.value)
        self.ModeTypeRadioButton1.select()
        # Default : None
        #self.ModeType.set(None)

        #self.Frame.pack(side="left", padx=50, pady=50)


    def GetFilename(self):
        return (self.Filename)

    def GetSeparator(self):
        return (self.Separator)

    def GetModeType(self):
        return (self.ModeType)


    # Called when saving a CSV
    #  Add the launch button and pack everything
    def Save_PutSaveButton(self, TheWindowListToSave):
        self.Frame.pack(side=tk.TOP, anchor=tk.N)
        self.SaveButton = tk.Button(self.OutterCanvas,
                                    text="Save to",
                                    command=lambda: Save_WindowList(self,
                                                                    self.GlobalListNumber,
                                                                    TheWindowListToSave))
        self.SaveButton.pack(side=tk.TOP,
                             padx=10,
                             pady=10)


    # Quit the "mainloop" and return
    def CallQuit(self):
        self.OutterCanvas.quit()

    # Kill the "mainloop" completely/Exit program
    def CallDestroy(self):
        self.OutterCanvas.destroy()


    def Validate(self):
        self.Separator.set(self.SeparatorEntry.get())
        #self.ModeType.set(self.ModeTypeEntry.get())

        #print("Frame [Save] :")
        #print("  Sep  : --" + self.Separator.get() + "--")
        #print("  ModeType  : --" + str(self.ModeType.get()) + "--")

        if ((len(self.Separator.get()) == 1) and
            ((self.ModeType.get() == ChoiceModeType.TERMS.value)
             or (self.ModeType.get() == ChoiceModeType.OCCURRENCIES.value))) :

            return (self.Separator.get(), self.ModeType.get())
        else :
            return (None)

    def GetCSVInfos(self):
        return (self.Validate())


def Save_WindowList(Frame, NumList, TheWindowListToSave):
    # Get CSV informations
    CSVInfos = Frame.GetCSVInfos()

    #print("[SaveWindowList] CSV :")
    #print(type(CSVInfos))
    #print(CSVInfos)
    #print(" ")

    if (not (CSVInfos is None)):
        ModeType = int(CSVInfos[1])
        Sep = CSVInfos[0]
        data = GlobalLists.gui_liste[NumList]

        filename = filedialog.asksaveasfilename(filetypes=[("CSV Files", "*.csv")],
                                                defaultextension=".csv")
        fd = open(filename, 'w')
        if (ModeType == ChoiceModeType.TERMS.value):
            [fd.write("{0}\n".format(key)) for key in data]
        elif (ModeType == ChoiceModeType.OCCURRENCIES.value):
            occu = occurrence(data)
            [fd.write("{0}{1}{2}\n".format(key, Sep, value)) for key, value in occu.items()]
        fd.close()
        Frame.CallDestroy()
    else:
        ErrWindow = WindowError.WindowError()
        ErrWindow.SetLabel("Error : Fill correctly CSV separator and column")
