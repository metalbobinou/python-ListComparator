import tkinter as tk

class StartWindow:
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
        self.LaunchButton = tk.Button(window,
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

    def CallWithdraw(self):
        self.MainCanvas.withdraw()
    
    def CallDestroy(self):
        self.MainCanvas.destroy()
    
    def GetCSVInfos(self, num):
        if (num == 1):
            return (self.FrameCSV1.Validate())
        else if (num == 2):
            return (self.FrameCSV2.Validate())
        else:
            print("Error in CSV Frame selection")
            return (None)

def Launch_WindowListAction(TheStartWindow):
    # Get CSV 1 & 2 informations
    CSV1Infos = TheStartWindow.GetCSVInfos(1)
    CSV2Infos = TheStartWindow.GetCSVInfos(2)

    ### TODO : !!! ADD VERIFICATIONS SOMEWHERE !!!
    
    # Close the main window
    TheStartWindow.destroy()
    # unsure about this one
    
    # Launch the WindowActions and the 2 WindowLists
    # unsure about this one
