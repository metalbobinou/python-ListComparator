import tkinter as tk
from tkinter import filedialog
from GuiClasses import WindowStart
from GuiClasses import WindowList
from GuiClasses import WindowActions
from csv_manipulate import load_csv
from csv_manipulate import save_csv


# gui_liste : Input List 1, Input List 2, Output List
import GlobalLists
# gui_liste = [None, None, None]

def occurence(liste):
    # Initialiser un dictionnaire pour stocker les occurrences
    occu = {}

    # Parcourir les lignes du fichier CSV
    for row in liste:
        valeur = row
        if valeur in occu:
            occu[valeur] += 1
        else:
            occu[valeur] = 1

    return occu


def main():
    # Initialize 2 empty CSV (global var)
    #
    # Load exit button in hardcoded way
    #
    # main loop of events :
    #
    # if 2 empty CSV (global var) :
    #   Open WindowStart
    #    Load inside 2 FrameCSVLoader
    #   OnPress "Process"
    #     Validate content
    #     if correct :
    #       fill 2 CSV (global var)
    #       quit WindowStart
    #     if incorrect :
    #       pop for error
    #   WindowStart.mainloop
    # else :
    #   Open WindowActions
    #   Open 2 WindowList with their CSV content (global var)
    #   WindowActions.mainloop


    # Initialize 2 empty CSV (global var)
    # (done by the initial files)

    # Load exit button in hardcoded way
    ExitWindow = tk.Tk()
    ExitWindow.title("Close Application")
    ExitWindow.geometry("300x50+1200+50")

    ExitButton = tk.Button(ExitWindow,
                           text="Close All Windows",
                           command=lambda: exit(0))
    #                       command=window.quit)

    ExitButton.pack()

    StartWindow = None
    # main loop of events :
    while (True):

        # if 2 empty CSV (global var) :
        if ((GlobalLists.gui_liste[0] is None) or
            (GlobalLists.gui_liste[1] is None)) :

            # Open WindowStart if not already opened
            if (StartWindow is None) :
                StartWindow = WindowStart.WindowStart("500x350+500+300")
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
            ActionsWindow = WindowActions.WindowActions("300x200+650+50")

            #   Open 2 WindowList with their CSV content (global var)
            List1Window = WindowList.WindowList("300x400+200+150", GlobalLists.gui_liste[0], occurence(GlobalLists.gui_liste[0]))
            List1Window.SetTitle("CSV 1 List")
            List1Window.SpecializedAsInputList()

            List2Window = WindowList.WindowList("300x400+1100+150", GlobalLists.gui_liste[1], occurence(GlobalLists.gui_liste[1]))
            List2Window.SetTitle("CSV 2 List")
            List2Window.SpecializedAsInputList()

            #   WindowActions.mainloop
            ActionsWindow.CallMainloop()

    return 0

main()
