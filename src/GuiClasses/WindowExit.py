# Tkinter GUI
import tkinter as tk


class WindowExit:
    Geometry = None
    Title = None

    # Main window getting the label and button
    Root = None

    # The button and its text to click on
    Button = None
    ButtonText = None

    def __init__(self):
        self.Root = tk.Tk()
        self.SetTitle("Close Application")
        self.ButtonText = "Close All Windows"
        self.Button = tk.Button(self.Root,
                                text="Close All Windows",
                                command=lambda: exit(0))
        self.Button.pack()

    def SetGeometry(self, geometry):
        self.Geometry = geometry
        self.Root.geometry(geometry)

    def GetGeometry(self):
        return (self.Geometry)

    def SetTitle(self, title):
        self.Title = title
        self.Root.title(title)

    def GetTitle(self):
        return (self.Title)

    def SetButton(self, button_text):
        self.Button.destroy()
        self.ButtonText = button_text
        self.Button = tk.Button(self.Root,
                                text=button_text,
                                command=lambda: exit(0))
        self.Button.pack()
