# Tkinter GUI
import tkinter as tk


class WindowExit:
    Geometry = None
    Title = None

    # Main canvas getting the label and button
    MainCanvas = None

    # The button and its text to click on
    Button = None
    ButtonText = None

    def __init__(self):
        self.MainCanvas = tk.Tk()
        self.SetTitle("Close Application")
        self.ButtonText = "Close All Windows"
        self.Button = tk.Button(self.MainCanvas,
                                text="Close All Windows",
                                command=lambda: exit(0))
        self.Button.pack()

    def SetGeometry(self, geometry):
        self.Geometry = geometry
        self.MainCanvas.geometry(geometry)

    def GetGeometry(self):
        return (self.Geometry)

    def SetTitle(self, title):
        self.Title = title
        self.MainCanvas.title(title)

    def GetTitle(self):
        return (self.Title)

    def SetButton(self, button_text):
        self.Button.destroy()
        self.ButtonText = button_text
        self.Button = tk.Button(self.MainCanvas,
                                text=button_text,
                                command=lambda: exit(0))
        self.Button.pack()
