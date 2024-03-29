# Tkinter GUI
import tkinter as tk
from tkinter import messagebox

# Windows & Frames for Errors and CSV Loading
from GuiClasses import FrameCSVLoader
from GuiClasses import WindowError

# Tools
from csv_manipulate import load_csv

# Globals required for the GUI
from GuiClasses import Globals
# gui_liste : Input List 1, Input List 2, Output List
# gui_liste = [None, None, None]


# Main first window asking to input 2 CSV
class WindowStart:
    Geometry = "0"
    Title = "List Window"
    # Main window getting everything
    Root = None
    # 1st Frame for CSV 1
    FrameCSV1 = None
    # 2nd Frame for CSV 2
    FrameCSV2 = None
    # Launch button
    FrameButton = None
    LaunchButton = None

    def __init__(self, geometry):
        self.Root = tk.Tk()
        self.SetGeometry(geometry)

        # If user close the window, kill everything
        self.Root.protocol("WM_DELETE_WINDOW",
                           lambda: on_closing(self))

        # Add the CSV 1 frame
        self.FrameCSV1 = FrameCSVLoader.FrameCSVLoader(self.Root)
        self.FrameCSV1.PackLeft()

        # Add the CSV 2 frame
        self.FrameCSV2 = FrameCSVLoader.FrameCSVLoader(self.Root)
        self.FrameCSV2.PackRight()

        # Add the launch button
        self.FrameButton = tk.Frame(self.Root)
        self.PutLaunchButton()
        self.FrameButton.pack(side=tk.BOTTOM,
                              fill=tk.BOTH)

    def PutLaunchButton(self):
        self.LaunchButton = tk.Button(self.FrameButton,
                                      text="Launch",
                                      command=lambda: Launch_WindowListActions(self))
        self.LaunchButton.pack(fill=tk.BOTH,
                               padx=10,
                               pady=10)

    def SetTitle(self, title):
        self.Title = title
        self.Root.title(title)

    def SetGeometry(self, geometry):
        self.Geometry = geometry
        self.Root.geometry(geometry)

    def GetTitle(self):
        return (self.Title)

    def GetGeometry(self):
        return (self.Geometry)

    def GetCSVInfos(self, num):
        if (num == 1):
            return (self.FrameCSV1.Validate())
        elif (num == 2):
            return (self.FrameCSV2.Validate())
        else:
            print("Bad CSV number (should be 1 or 2) : " + num)
            return (None)

    def CallMainloop(self):
        self.Root.mainloop()

    def CallWithdraw(self):
        self.Root.withdraw()

    # Quit the "mainloop" and return
    def CallQuit(self):
        self.Root.withdraw()
        self.Root.quit()

    # Kill the "mainloop" completely/Exit program
    def CallDestroy(self):
        self.Root.destroy()


def Launch_WindowListActions(TheStartWindow):
    # Get CSV 1 & 2 informations
    CSV1Infos = TheStartWindow.GetCSVInfos(1)
    CSV2Infos = TheStartWindow.GetCSVInfos(2)

    #print("[WindowStart] CSV 1 :")
    #print(type(CSV1Infos))
    #print(CSV1Infos)
    #print(" ")
    #print("[WindowStart] CSV 2 :")
    #print(type(CSV2Infos))
    #print(CSV2Infos)

    if ((not (CSV1Infos is None)) and (not (CSV2Infos is None))) :
        # Correct the columns (technical) : [1 -> 9] to [0 -> 8]
        Col1 = int(CSV1Infos[2]) - 1
        Col2 = int(CSV2Infos[2]) - 1

        Globals.gui_liste[0] = load_csv(CSV1Infos[0], CSV1Infos[1], Col1)
        Globals.gui_liste[1] = load_csv(CSV2Infos[0], CSV2Infos[1], Col2)

        # If the 2 CSV has been correctly loaded, exit
        #if (! (Globals.gui_liste[0] is None) or
        #    (Globals.gui_liste[1] is None)) :
        # Close the main window and return back to the program
        #TheStartWindow.CallDestroy()
        TheStartWindow.CallQuit()

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

def on_closing(TheStartWindow):
    if (messagebox.askokcancel("Quit", "Do you want to quit?")):
        #TheStartWindow.CallDestroy()
        exit(0)
