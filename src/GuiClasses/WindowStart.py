import tkinter as tk

from GuiClasses import FrameCSVLoader
from logic_processing import occurence
from csv_manipulate import load_csv


# gui_liste : Input List 1, Input List 2, Output List
import GlobalLists
# gui_liste = [None, None, None]

# Main first window asking to input 2 CSV
class WindowStart:
    Geometry = "0"
    Title = "List Window"
    # Canvas getting the whole window
    MainCanvas = None
    # 1st Frame for CSV 1
    FrameCSV1 = None
    # 2nd Frame for CSV 2
    FrameCSV2 = None
    # Launch button
    LaunchButton = None

    def __init__(self, geometry):
        self.MainCanvas = tk.Tk()
        self.SetGeometry(geometry)

        # Add the CSV 1 frame
        self.FrameCSV1 = FrameCSVLoader.FrameCSVLoader(self.MainCanvas)

        # Add the CSV 2 frame
        self.FrameCSV2 = FrameCSVLoader.FrameCSVLoader(self.MainCanvas)

        # Add the launch button
        self.PutLaunchButton()


    def PutLaunchButton(self):
        self.LaunchButton = tk.Button(self.MainCanvas,
                                      text="Launch",
                                      command=lambda: Launch_WindowListActions(self))
        self.LaunchButton.pack()


    def SetTitle(self, title):
        self.Title = title
        self.MainCanvas.title(title)

    def SetGeometry(self, geometry):
        self.Geometry = geometry
        self.MainCanvas.geometry(geometry)

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
        self.MainCanvas.mainloop()

    def CallWithdraw(self):
        self.MainCanvas.withdraw()

    # Quit the "mainloop" and return
    def CallQuit(self):
        self.MainCanvas.quit()

    # Kill the "mainloop" completely/Exit program
    def CallDestroy(self):
        self.MainCanvas.destroy()


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

        GlobalLists.gui_liste[0] = load_csv(CSV1Infos[0], CSV1Infos[1], Col1)
        GlobalLists.gui_liste[1] = load_csv(CSV2Infos[0], CSV2Infos[1], Col2)

        # If the 2 CSV has been correctly loaded, exit
        #if (! (GlobalLists.gui_liste[0] is None) or
        #    (GlobalLists.gui_liste[1] is None)) :
        # Close the main window and return back to the program
        #TheStartWindow.CallDestroy()
        TheStartWindow.CallQuit()

    else :
        ErrWindow = tk.Tk()
        ErrWindow.title("Error")
        ErrLabel = tk.Label(ErrWindow, text="Error : Fill correctly CSV")
        ErrLabel.pack()
        ErrButton = tk.Button(ErrWindow,
                              text="OK",
                              command=lambda: ErrWindow.destroy())
        ErrButton.pack()
