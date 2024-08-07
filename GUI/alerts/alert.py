import customtkinter

from typing import Literal

from GUI.alerts.config import windowsconfig
from GUI.alerts.frames.areaframe import UsageFrame
from data.shareables import ShareHereby


class VisualAlert:
    
    def __init__(self, status:Literal['X',"OK"], 
                 message:str, 
                 windowTitle:str=None, 
                 color_appearance:Literal['light','dark']='light') -> None:
        
        # Objetos
        #------------------------------
        self.master = None
        self.color_appearance = color_appearance
        self.message = message
        self.status = status.upper()
        self.windowTitle = windowTitle if not windowTitle == None else status
        #------------------------------
        self.__config_GUI_inicializacao()
    
    
    def resizeWindow(self, resize:list[str:str]):
        # self.
        self.master.geometry(f'{resize}'+{windowsconfig.WINDOW_POSITION})
        
    def build(self):
        # self.__config_GUI_inicializacao()
        frame = UsageFrame(self)
        self.master.grab_set()
        
    
    def __config_GUI_inicializacao(self):
        self.master = customtkinter.CTkToplevel(self.master)
        self.master.title(self.windowTitle)
        

        self.total_weight = self.master.winfo_screenwidth()
        self.total_height = self.master.winfo_screenheight()  
        
        
        x = (self.total_weight - int(windowsconfig.WINDOW_SIZE.split('x')[0])) // 2
        y = ((self.total_height - int(windowsconfig.WINDOW_SIZE.split('x')[1])) - 100) // 2
        windowsconfig.WINDOW_POSITION = '+'.join([str(x),str(y)])
        
        customtkinter.set_appearance_mode(self.color_appearance)
        
        self.master.geometry(f'{windowsconfig.WINDOW_SIZE}+{windowsconfig.WINDOW_POSITION}')
        self.master.resizable(False, False)
        
        
    def destroy(self):
        print(3)
        self.master.destroy()
        print(4)