import os
import customtkinter

from PIL import Image

from src.data.exportData import ExportWindow
from src.data.dirSpotCheck import SpotCheck
from src.GUI.frames.patternAbstractClass import AbstractGlobalObject
from src.GUI.topLevels.dynamicalWindow import DynamicalWindowApproach


class ObjectSideBar(AbstractGlobalObject):
    
    def __init__(self, object) -> None:
        super().__init__(object)
        
        
    def run(self):
        self.buildFrame()
        self.labelProjectName()
        self.buttonExport()
        self.buttonLOG()
        self.buttonAlocationConfiguration()
        self.buttonTutorial()
        self.projectOwnerWaterMark()
        
    
    def buildFrame(self):
        self.sidebarFrame = customtkinter.CTkFrame(master=self.master, width=200, corner_radius=20)
        self.sidebarFrame.grid(row=0, column=0, sticky='ns', rowspan=4, padx=(0,20))
        self.sidebarFrame.grid_propagate(False)
        
    
    def labelProjectName(self):
        labelProjectName = customtkinter.CTkLabel(master=self.sidebarFrame,
                                               text=self.object_main.projectName, font=('Roboto', 24, 'bold'))
        labelProjectName.grid(row=0, column=0, padx=20, pady=(40,60), sticky='n')


    def projectOwnerWaterMark(self):
        spacer = customtkinter.CTkLabel(master=self.sidebarFrame, text="")
        spacer.grid(row=9, column=0, sticky='ns', pady=(430,0))
        
        label = customtkinter.CTkLabel(master=self.sidebarFrame, text="powered by Lucas Lourenço", text_color='#424949', font=('Robolo', 10))
        label.grid(row=10, column=0, sticky='s', pady=(0, 10))
        
        
    def buttonExport(self):
        logButton = customtkinter.CTkButton(master=self.sidebarFrame, text='Exportar',
                                            command=ExportWindow,
                                            image=customtkinter.CTkImage(light_image=Image.open(r'src\GUI\images\export_icon.png').resize((50,50)), dark_image=Image.open(r'src\GUI\images\export_icon.png').resize((50,50))),
                                            font=('Robolo', 14, 'bold'), border_spacing=5, border_width=2)
        logButton.grid(row=1, column=0, pady=(0, 20))


    def buttonLOG(self):
        logButton = customtkinter.CTkButton(master=self.sidebarFrame, text='Acessar LOG',
                                            command=self.__command_LogOptions,
                                            image=customtkinter.CTkImage(light_image=Image.open(r'src\GUI\images\log_icon.png').resize((50,50)), dark_image=Image.open(r'src\GUI\images\log_icon.png').resize((50,50))),
                                            font=('Robolo', 14, 'bold'), border_spacing=5, border_width=2)
        logButton.grid(row=2, column=0, pady=(0, 20))

    
    def buttonAlocationConfiguration(self):
        logButton = customtkinter.CTkButton(master=self.sidebarFrame, 
                                            text='Alocadores', 
                                            command=self.__comamnd_alocation, 
                                            border_spacing=5, 
                                            border_width=2,
                                            font=('Robolo', 14, 'bold'), 
                                            image=customtkinter.CTkImage(light_image=Image.open(r'src\GUI\images\indicator_icon.png').resize((50,50)), dark_image=Image.open(r'src\GUI\images\indicator_icon.png').resize((50,50))),)
        logButton.grid(row=3, column=0, pady=(0, 20))
        
    def buttonTutorial(self):
        logButton = customtkinter.CTkButton(master=self.sidebarFrame, 
                                            command=print, 
                                            text='Tutorial',
                                            border_spacing=5, 
                                            border_width=2,
                                            font=('Robolo', 14, 'bold'), 
                                            image=customtkinter.CTkImage(light_image=Image.open(r'src\GUI\images\tutorial_icon.png').resize((50,50)), dark_image=Image.open(r'src\GUI\images\tutorial_icon.png').resize((50,50))),)
        logButton.grid(row=4, column=0, pady=(0, 20))
        
    
    def __comamnd_alocation(self):
        options = {
            "Designar Indicador":SpotCheck.dir_appointment,
            "Visualizar Apontamentos":SpotCheck.show_appointment,
        }
        
        app = DynamicalWindowApproach(master=self.sidebarFrame)
        app.giveOptions(options_dict=options)
        
        
    def __command_LogOptions(self):
        options = {
            'Log Geral':lambda:os.startfile(r'src\LOG\file\log.log'),
            'Log da Instância':print,            
        }
        
        app = DynamicalWindowApproach(master=self.sidebarFrame)
        app.giveOptions(options_dict=options)
        ...
        
        
        
    