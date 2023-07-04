import os.path
import tkinter as tk
from tkinter import filedialog

from GuiClasses import WindowError
from csv_manipulate import load_csv

# gui_liste : Input List 1, Input List 2, Output List
import GlobalLists
# gui_liste = [None, None, None]


# Frame asking for informations about a CSV (path, sep, col)
class FrameCSVLoader:
    GlobalListNumber = None

    # Values we want to get from the user (tk.StringVar())
    Filename = None
    Separator = None
    Column = None

    ### GUI
    # The current frame
    Frame = None
    # Canvas where to put the current frame
    Canvas = None
    # Specifications of the current frame
    Geometry = None
    Padding = None
    BorderWidth = None
    Relief = None
    # Widgets of the frame
    FileDescription = None
    FileButton = None
    FileEntry = None
    SeparatorDescription = None
    SeparatorEntry = None
    ColumnDescription = None
    ColumnEntry = None
    # Widgets for reloading a CSV
    LaunchButton = None

    def __init__(self, canvas, ListNum=None):
        # Get the canvas where to put the frame
        self.Canvas = canvas
        self.GlobalListNumber = ListNum

        self.Frame = tk.Frame(self.Canvas)

        # Fill variables
        self.Filename = tk.StringVar()
        self.Separator = tk.StringVar()
        self.Column = tk.StringVar()

        # Describe the field and button
        self.FileDescription = tk.Label(self.Frame,
                                        text="CSV File Path:")
        self.FileDescription.pack()
        # Put the button for the file and fill the file field when chosen
        self.FileButton = tk.Button(self.Frame,
                                    text="Choose file",
                                    command=self.ChooseFile)
        self.FileButton.pack()
        # Create a file field
        self.FileEntry = tk.Entry(self.Frame, textvariable=self.Filename)
        self.FileEntry.insert(0, "C1.csv")
        self.FileEntry.pack()

        # Separator Description and Field
        self.SeparatorDescription = tk.Label(self.Frame,
                                             text="Separator:")
        self.SeparatorDescription.pack()
        self.SeparatorEntry = tk.Entry(self.Frame,
                                       textvariable=self.Separator)
        self.SeparatorEntry.insert(0, ";")
        self.SeparatorEntry.pack()

        # Column Description and Field
        self.ColumnDescription = tk.Label(self.Frame,
                                          text="Column:")
        self.ColumnDescription.pack()
        self.ColumnEntry = tk.Entry(self.Frame, textvariable=self.Column)
        self.ColumnEntry.insert(0, "6")
        self.ColumnEntry.pack()

        #self.Frame.pack(side="left", padx=50, pady=50)

    def GetFilename(self):
        return (self.Filename)

    def GetSeparator(self):
        return (self.Separator)

    def GetColumn(self):
        return (self.Column)

    def SetPadding(self, padding):
        self.Padding = padding
        self.Frame['padding'] = padding

    def SetBorder(self, borderwidth):
        self.BorderWidth = borderwidth
        self.Frame['borderwidth'] = borderwidth

    def SetRelief(self, relief):
        self.Relief = relief
        self.Frame['relief'] = relief

    def PackLeft(self):
        self.Frame.pack(side=tk.LEFT,
                        anchor=tk.NW,
                        padx=10,
                        pady=10)

    def PackRight(self):
        self.Frame.pack(side=tk.RIGHT,
                        anchor=tk.NE,
                        padx=10,
                        pady=10)

    # Called when reloading a CSV
    #  Add the launch button and pack everything
    def Reload_PutLaunchButton(self, TheWindowListToReload):
        self.Frame.pack(side=tk.TOP, anchor=tk.N)
        self.LaunchButton = tk.Button(self.Canvas,
                                      text="Launch",
                                      command=lambda: Reload_WindowList(self,
                                                                        self.GlobalListNumber,
                                                                        TheWindowListToReload))
        self.LaunchButton.pack(side=tk.TOP,
                               padx=10,
                               pady=10)

    # Quit the "mainloop" and return
    def CallQuit(self):
        self.Canvas.quit()

    # Kill the "mainloop" completely/Exit program
    def CallDestroy(self):
        self.Canvas.destroy()

    def ChooseFile(self):
        # Open a dialog box in order to select the CSV file
        file = filedialog.askopenfilename(title="Select a CSV file",
                                          filetypes=[("CSV Files", "*.csv"),
                                                     ("Text Files","*.txt"),
                                                     ("All Files","*.*")])

        # Check if a file has been selected
        if (file):
            # Store & Fill the file path in the entry box
            self.Filename.set(file)
            self.FileEntry.delete(0, tk.END) # remove previous content
            self.FileEntry.insert(0, file)

    def Validate(self):
        self.Filename.set(self.FileEntry.get())
        self.Separator.set(self.SeparatorEntry.get())
        self.Column.set(self.ColumnEntry.get())

        #print("Frame :")
        #print("  Path : --" + self.Filename.get() + "--")
        #print("  Sep  : --" + self.Separator.get() + "--")
        #print("  Col  : --" + self.Column.get() + "--")

        if ((os.path.isfile(self.Filename.get())) and
            (len(self.Separator.get()) == 1) and
            (int(self.Column.get()) > 0)) :

            return (self.Filename.get(), self.Separator.get(), self.Column.get())
        else :
            return (None)

    def GetCSVInfos(self):
        return (self.Validate())


def Reload_WindowList(Frame, NumList, TheWindowListToReload):
    # Get CSV informations
    CSVInfos = Frame.GetCSVInfos()

    #print("[ReloadWindowList] CSV :")
    #print(type(CSVInfos))
    #print(CSVInfos)
    #print(" ")

    if (not (CSVInfos is None)):
        # Correct the columns (technical) : [1 -> 9] to [0 -> 8]
        Col = int(CSVInfos[2]) - 1

        GlobalLists.gui_liste[NumList] = load_csv(CSVInfos[0], CSVInfos[1], Col)

        # If the CSV has been correctly loaded, exit
        if (not (GlobalLists.gui_liste[NumList] is None)):
            # Refresh the WindowList
            TheWindowListToReload.InsertListInListBox(GlobalLists.gui_liste[NumList])
            # Close the main window and return back to the program
            Frame.CallDestroy()
            #Frame.CallQuit()

    else :
        #ErrWindow = tk.Tk()
        #ErrWindow.title("Error")
        #ErrLabel = tk.Label(ErrWindow, text="Error : Fill correctly CSV")
        #ErrLabel.pack()
        #ErrButton = tk.Button(ErrWindow,
        #                      text="OK",
        #                      command=lambda: ErrWindow.destroy())
        #ErrButton.pack()
        ErrWindow = WindowError.WindowError()
        ErrWindow.SetLabel("Error : Fill correctly CSV paths, separator, and column")
