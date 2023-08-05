# Tkinter GUI
import tkinter as tk


class WindowError:
    Geometry = None
    Title = None

    # Main canvas getting the label and button
    MainCanvas = None

    # The label first with the error message
    Label = None
    # The button and its text to click on
    Button = None
    ButtonText = None

    def __init__(self):
        self.MainCanvas = tk.Tk()
        self.SetTitle("Error")
        self.Label = tk.Label(self.MainCanvas, text="Error")
        self.Label.pack()
        self.ButtonText = "OK"
        self.Button = tk.Button(self.MainCanvas,
                                text="OK",
                                command=lambda: self.MainCanvas.destroy())
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
                                command=lambda: self.MainCanvas.destroy())
        self.Button.pack()

    # For upating the label, we must remove the button and put it again
    def SetLabel(self, new_text):
        self.Label.destroy()
        self.Label = tk.Label(self.MainCanvas, text=new_text)
        self.Label.pack()
        self.SetButton(self.ButtonText)
