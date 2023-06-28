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
    # Values we want to get from the user (tk.StringVar())
    Filename = None
    Separator = None
    Column = None

    # Frame where to put the Canvas
    Frame = None
    # Canvas where to put the frame
    Canvas = None

    Num = None
    # Specifications of the frame
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

    def __init__(self, canvas, num=None):
        # Get the canvas where to put the frame
        self.Canvas = canvas
        self.Num = num

        self.Frame = tk.Frame(self.Canvas, width=250, height=300)

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

        self.Frame.pack(side="left")

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

    def PutLaunchButton(self):
        self.LaunchButton = tk.Button(self.Canvas,
                                      text="Launch",
                                      command=lambda: Launch_WindowList(self, self.Num))
        self.LaunchButton.pack(side=tk.BOTTOM)

    # Quit the "mainloop" and return
    def CallQuit(self):
        self.Canvas.quit()

    # Kill the "mainloop" completely/Exit program
    def CallDestroy(self):
        self.Canvas.destroy()

    def ChooseFile(self):
        # Open a dialog box in order to select the CSV file
        file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

        # Check if a file has been selected
        if (file):
            # Store & Fill the file path in the entry box
            self.Filename.set(file)
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

    def GetCSVInfos(self, num):
        return (self.Validate())


def Launch_WindowList(Window, num):
    # Get CSV 1 & 2 informations
    CSVInfos = Window.GetCSVInfos(num)

    #print("[WindowStart] CSV 1 :")
    #print(type(CSV1Infos))
    #print(CSV1Infos)
    #print(" ")
    #print("[WindowStart] CSV 2 :")
    #print(type(CSV2Infos))
    #print(CSV2Infos)

    if (not (CSVInfos is None)):
        # Correct the columns (technical) : [1 -> 9] to [0 -> 8]
        Col = int(CSVInfos[2]) - 1

        GlobalLists.gui_liste[num] = load_csv(CSVInfos[0], CSVInfos[1], Col)

        # If the 2 CSV has been correctly loaded, exit
        #if (! (GlobalLists.gui_liste[0] is None) or
        #    (GlobalLists.gui_liste[1] is None)) :
        # Close the main window and return back to the program
        #TheStartWindow.CallDestroy()
        Window.CallQuit()

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
