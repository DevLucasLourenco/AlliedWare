import customtkinter
from src.GUI.topLevels.dynamicalWindow import DynamicalWindowApproach
from src.GUI.frames.patternAbstractClass import AbstractGlobalObject


class ObjectSideBar(AbstractGlobalObject):
    
    def __init__(self, object) -> None:
        super().__init__(object)
        
        
    def run(self):
        self.buildFrame()
        self.labelProjectName()
        self.buttonCheckLOG()
        self.buttonAlocationConfiguration()
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
        
        
    def buttonCheckLOG(self):
        logButton = customtkinter.CTkButton(master=self.sidebarFrame, text='Visualizar\nLOG', command=print, 
                                            font=('Robolo', 14, 'bold'), border_spacing=5, border_width=2)
        logButton.grid(row=1, column=0, pady=(0, 20))
        
    
    def buttonAlocationConfiguration(self):
        logButton = customtkinter.CTkButton(master=self.sidebarFrame, text='Apontamento de\nAlocadores', command=self.__comamnd_alocation, 
                                            font=('Robolo', 14, 'bold'), border_spacing=5, border_width=2)
        logButton.grid(row=2, column=0, pady=(0, 20))
        
        
    def __comamnd_alocation(self):
        options = {
            "Designar Diretório":print,
            "Visualizar Apontamentos":print,
        }
        
        app = DynamicalWindowApproach(master=self.sidebarFrame)
        app.giveOptions(options_dict=options)
        