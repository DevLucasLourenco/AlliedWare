import customtkinter
from .config.windowConfig import (WINDOWSIZE, 
                                 PROJECTNAME)
from guiManagement.frames.frames import (LowerFrameForUsage, 
                                         ObjectSideBar, 
                                         TopFrameForUsage)


class GUIMain:

    def __init__(self) -> None:
        self.projectName = PROJECTNAME
        self.windowSize = WINDOWSIZE
        self.windowPosition = None
        
        self.__objects()
        self.__execution()
            
    
    def __objects(self):
        self.master = None
        self.total_height = None
        self.total_weight = None
            
    
    def __execution(self):
        self.__initialization_GUI_configuration()
        self.executeGUI()
    
    
    def __initialization_GUI_configuration(self):
        self.master = customtkinter.CTk()
        self.master.title(self.projectName)
        
        self.total_weight = self.master.winfo_screenwidth()
        self.total_height = self.master.winfo_screenheight()
        
        
        x = (self.total_weight - int(self.windowSize.split('x')[0])) // 2
        y = ((self.total_height - int(self.windowSize.split('x')[1])) - 100) // 2
        self.windowPosition = '+'.join([str(x),str(y)])
        
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        
        self.master.geometry(f'{self.windowSize}+{self.windowPosition}')
        self.master.resizable(False, False)
        
        
    def executeGUI(self):
        #------------------------------
        self.OSB = ObjectSideBar(self)
        self.TFFU = TopFrameForUsage(self)
        self.LFFU = LowerFrameForUsage(self)
        
        #------------------------------


