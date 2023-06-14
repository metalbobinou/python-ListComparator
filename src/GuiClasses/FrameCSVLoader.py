import os.path
import tkinter as tk
from tkinter import filedialog


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

    def __init__(self, canvas):
        # Get the canvas where to put the frame
        self.Canvas = canvas

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

    # Quit the "mainloop" and return
    def CallQuit(self):
        self.MainCanvas.quit()

    # Kill the "mainloop" completely/Exit program
    def CallDestroy(self):
        self.MainCanvas.destroy()

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
