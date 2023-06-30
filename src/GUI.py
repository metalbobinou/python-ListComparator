from GuiClasses import WindowStart
from GuiClasses import WindowActions
from GuiClasses import WindowList
from GuiClasses import WindowExit

from csv_manipulate import load_csv

from tools import occurrence


# gui_liste : Input List 1, Input List 2, Output List
import GlobalLists
# gui_liste = [None, None, None]


def main():
    # Initialize 2 empty CSV (global var)
    # (done by the initial files)

    # Load exit button in hardcoded way
    #ExitWindow = tk.Tk()
    #ExitWindow.title("Close Application")
    ExitWindow = WindowExit.WindowExit()
    ExitWindow.SetGeometry("300x50+1200+50")
    #ExitButton = tk.Button(ExitWindow,
    #                       text="Close All Windows",
    #                       command=lambda: exit(0))
    #ExitButton.pack()

    StartWindow = None
    # main loop of events :
    while (True):

        # if 2 empty CSV (global var) :
        if ((GlobalLists.gui_liste[0] is None) or
            (GlobalLists.gui_liste[1] is None)) :

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
            # Open WindowActions
            ActionsWindow = WindowActions.WindowActions("300x250+650+50")
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
