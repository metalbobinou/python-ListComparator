# Windows for each part
from GuiClasses import WindowStart
from GuiClasses import WindowActions
from GuiClasses import WindowList
from GuiClasses import WindowExit

# Plugin loader
from plugins_loader import PluginsImporter

# CSV Loader
from csv_manipulate import load_csv

# Tools
from tools import occurrence

# Globals required for the GUI
from GuiClasses import Globals
# gui_liste : Input List 1, Input List 2, Output List
# gui_liste = [None, None, None]


def main():
    # Load the plugins
    Globals.MyPluginsImporter = PluginsImporter()
    nb_plugins_classes = Globals.MyPluginsImporter.LoadPlugins()

    # Initialize 2 empty CSV (global var)
    # (done by the initial files)

    # Load exit button in hardcoded way
    #ExitWindow = WindowExit.WindowExit()
    #ExitWindow.SetGeometry("300x50+1200+50")

    StartWindow = None
    # main loop of events :
    while (True):

        # if 2 empty CSV (global var) :
        if ((Globals.gui_liste[0] is None) or
            (Globals.gui_liste[1] is None)) :

            # Open WindowStart if not already opened
            if (StartWindow is None) :
                StartWindow = WindowStart.WindowStart("500x300+550+250")
                StartWindow.SetTitle("Import CSV")

            #   Load inside 2 FrameCSVLoader
            #   OnPress "Process"
            #     Validate content
            #     if correct :
            #       fill 2 CSV (global var)
            #       quit WindowStart
            #     if incorrect :
            #       pop for error

            #   WindowStart.mainloop
            StartWindow.CallMainloop()

        # else :
        else :
            # Open WindowActions   (300x250+650+50)
            ActionsWindow = WindowActions.WindowActions("450x450+650+50")
            ActionsWindow.SetTitle("CSV List Comparator")

            #   Open 2 WindowList with their CSV content (global var)
            List1Window = WindowList.WindowList(0,
                                                "300x400+200+150")
            List1Window.SetTitle("CSV 1 List")
            List1Window.SpecializedAsInputList()

            List2Window = WindowList.WindowList(1,
                                                "300x400+1100+150")
            List2Window.SetTitle("CSV 2 List")
            List2Window.SpecializedAsInputList()

            #   WindowActions.mainloop
            ActionsWindow.CallMainloop()

    return 0

main()
