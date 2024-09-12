import customtkinter

from tkinter import messagebox

from src.data.exportData import ExportWindow
from src.LOG.LOG_manager import LOGGER
from src.data.dirSpotCheck import SpotCheck
from src.data.shareables import ShareHereby
from src.GUI.frames.lowerFrame import LowerFrameForUsage
from src.GUI.frames.sideBarFrame import ObjectSideBar
from src.GUI.frames.topFrame import (MainInterfaceTopFrame, 
                                     TopFrameForUsage)

from .config.windowConfig import (WINDOWSIZE, 
                                 PROJECT_TITLE,
                                 PROJECTNAME, 
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
        
        # self.master.iconbitmap(r'src\GUI\images\allied.ico')
        
        self.master.geometry(f'{self.windowSize}+{self.windowPosition}')
        self.master.resizable(False, False)
        
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)
        
    def on_close(self):
        res = messagebox.askyesno("Exportar", "Antes de fechar, deseja exportar os dados alocados?")
        if res:
            ExportWindow(self.master)
        else:
            self.master.destroy()
        
    def executeGUI(self) -> None:
        self.InicialExecutions()
        #------------------------------
        self.OSB = ObjectSideBar(self)
        self.TF = TopFrameForUsage(self)
        self.LF = LowerFrameForUsage(self)
        
        mainInterfaceTF = MainInterfaceTopFrame(self.TF.get())
        mainInterfaceTF.GRID_ALL()
        #------------------------------


    def InicialExecutions(self):
        LOGGER(f'=============== {PROJECTNAME} ===============', 'INFO')
        LOGGER(f'{PROJECTNAME} Inicializado', 'INFO')
        SpotCheck.CreateFileIfNotExists()
        
