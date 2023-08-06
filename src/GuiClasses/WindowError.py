# Tkinter GUI
import tkinter as tk


class WindowError:
    Geometry = None
    Title = None

    # Main window getting the label and button
    Root = None

    # The label first with the error message
    Label = None
    # The button and its text to click on
    Button = None
    ButtonText = None

    def __init__(self):
        self.Root = tk.Tk()
        self.SetTitle("Error")
        self.Label = tk.Label(self.Root, text="Error")
        self.Label.pack()
        self.ButtonText = "OK"
        self.Button = tk.Button(self.Root,
                                text="OK",
                                command=lambda: self.Root.destroy())
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
                                command=lambda: self.Root.destroy())
        self.Button.pack()

    # For upating the label, we must remove the button and put it again
    def SetLabel(self, new_text):
        self.Label.destroy()
        self.Label = tk.Label(self.Root, text=new_text)
        self.Label.pack()
        self.SetButton(self.ButtonText)
