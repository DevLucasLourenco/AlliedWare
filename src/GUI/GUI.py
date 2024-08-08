import customtkinter

from src.GUI.frames.lowerFrame import LowerFrameForUsage
from src.GUI.frames.sideBarFrame import ObjectSideBar
from src.GUI.frames.topFrame import TopFrameForUsage
from src.data.shareables import ShareHereby

from .config.windowConfig import (WINDOWSIZE, 
                                 PROJECT_TITLE, 
                                 APPEARANCE_MODE,
                                 COLOR_THEME)


class GUIMain:

    def __init__(self) -> None:
        self.projectName = PROJECT_TITLE
        self.windowSize = WINDOWSIZE
        self.windowPosition = None
        
        self.__objects()
        self.__execution()
            
    
    def __objects(self) -> None:
        self.master = None
        self.total_height = None
        self.total_weight = None
        
            
    
    def __execution(self) -> None:
        self.__initialization_GUI_configuration()
        self.executeGUI()
    
    
    def __initialization_GUI_configuration(self) -> None:
        self.master = customtkinter.CTk()
        ShareHereby.MAIN_INSTANCE_OF_GUI = self.master
        
        self.master.title(self.projectName)
        
        self.total_weight = self.master.winfo_screenwidth()
        self.total_height = self.master.winfo_screenheight()
        
        
        x = (self.total_weight - int(self.windowSize.split('x')[0])) // 2
        y = ((self.total_height - int(self.windowSize.split('x')[1])) - 100) // 2
        self.windowPosition = '+'.join([str(x),str(y)])
        
        customtkinter.set_appearance_mode(APPEARANCE_MODE)
        customtkinter.set_default_color_theme(COLOR_THEME)
        # customtkinter.set_default_color_theme('GUI/config/red-pattern.json')
        
        self.master.geometry(f'{self.windowSize}+{self.windowPosition}')
        self.master.resizable(False, False)
        
        
        
    def executeGUI(self) -> None:
        #------------------------------
        self.OSB = ObjectSideBar(self)
        self.TF = TopFrameForUsage(self)
        self.LF = LowerFrameForUsage(self)
        #------------------------------


