import tkinter as tk
from tkinter import filedialog


class FrameCSVLoader:
    # Values we want to get from the user
    Filename = tk.StringVar()
    Separator = tk.StringVar()
    Column = tk.StringVar()

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
    FileField = None
    SeparatorDescription = None
    SeparatorField = None
    ColumnDescription = None
    ColumnField = None

    def __init__(self, canvas):
        # Get the canvas where to put the frame
        self.Canvas = canvas

        # Describe the field and button
        self.FileDescription = tk.Label(self.Canvas,
                                        text="CSV File Path:")
        self.FileDescription.pack()
        # Put the button for the file and fill the file field when chosen
        self.FileButton = tk.Button(self.Canvas,
                                    text="Choose file",
                                    command=lambda: import_csv(self))
        self.FileButton.pack()
        # Create a file field
        self.FileField = tk.Entry(self.Canvas, textvariable=Filename)
        self.FileField.pack()

        # Separator Description and Field
        self.SeparatorDescription = tk.Label(self.Canvas,
                                             text="Separator:")
        self.SeparatorDescription.pack()
        self.SeparatorField = tk.Entry(self.Canvas,
                                       textvariable=self.Separator)
        self.SeparatorField.insert(0, ";")
        self.SeparatorField.pack()

        # Column Description and Field
        self.ColumnDescription = tk.Label(self.Canvas,
                                          text="Column:")
        self.ColumnDescription.pack()
        self.ColumnField = tk.Entry(self.Canvas, textvariable=Column)
        self.ColumnField.insert(0, "6")
        self.ColumnField.pack()

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

    def ChooseFile(self):
        # Ouvre une boîte de dialogue pour sélectionner un fichier CSV
        file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

        # Vérifie si un fichier a été sélectionné
        if (file):
            # Stocke le chemin du fichier
            # file_path.set(file)
            self.Filename.set(file)
            self.FileField.insert(0, file)

    # def Validate(self):
        # check the content of th cells ?... unsure about this one


def import_csv(TheFrame):
    TheFrame.ChooseFile()
