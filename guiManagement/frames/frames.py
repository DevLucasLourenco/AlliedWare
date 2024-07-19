import customtkinter


class AbstractGlobalObject():
    'Absolute Class for patterns'
    
    def __init__(self, object) -> None:
        # self.object_main:GUIMain = object
        self.object_main = object
        self.master = self.object_main.master
        self.run()

    def run(self):
        ...


class ObjectSideBar(AbstractGlobalObject):
    
    def __init__(self, object) -> None:
        super().__init__(object)
        
        
    def run(self):
        self.buildFrame()
        self.labelProjectName()
        
    
    def buildFrame(self):
        self.frame_config_pos_esquerda = customtkinter.CTkFrame(master=self.master, width=250, corner_radius=20)
        self.frame_config_pos_esquerda.grid(row=0, column=0, sticky='ns', rowspan=4, padx=(0,20))
        
    
    def labelProjectName(self):
        label_nome_projeto = customtkinter.CTkLabel(master=self.frame_config_pos_esquerda,
                                               text=self.object_main.projectName, font=('Roboto', 24, 'bold'))
        label_nome_projeto.grid(row=0, column=0, padx=20, pady=40, sticky='n')



class TopFrameForUsage(AbstractGlobalObject):
    
    def __init__(self, object) -> None:
        super().__init__(object)
    
    
    def get(self):
        return self.frameForUsage
        
        
    def run(self):
        self.buildFrame()
        
    
    def buildFrame(self):
        self.frameForUsage = customtkinter.CTkFrame(master=self.master, corner_radius=20, width=570, height=450)
        self.frameForUsage.grid(row=0, column=1, sticky='nsew', padx=(0,0), pady=(20,0))
        

class LowerFrameForUsage(AbstractGlobalObject):
    
    def __init__(self, object) -> None:
        super().__init__(object)
        
        
    def get(self):
        return self.frameForUsage
        
        
    def run(self):
        self.buildFrame()
        
    
    def buildFrame(self):
        self.frameForUsage = customtkinter.CTkFrame(master=self.master, corner_radius=20, width=570)
        self.frameForUsage.grid(row=1, column=1, sticky='nsew', padx=(0,0), pady=(20,0))
        
        
        
