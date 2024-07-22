import customtkinter

from GUI.buttons.patternButtons import *
from GUI.frames.patternAbstractClass import AbstractGlobalObject
from GUI.config.shareables import ShareHereby



class TopFrameForUsage(AbstractGlobalObject):
    
    def __init__(self, object) -> None:
        super().__init__(object)
    
    
    def get(self):
        return self.frameForUsage
        
        
    def run(self):
        self.buildFrame()
        self.buildLabel()
        self.buildButtons()
        
    
    def buildFrame(self):
        self.frameForUsage = customtkinter.CTkFrame(master=self.master, corner_radius=20, width=570, height=450)
        self.frameForUsage.grid(row=0, column=1, sticky='nsew', padx=(0,0), pady=(20,0))
        self.frameForUsage.grid_propagate(False)
       
       
    def buildButtons(self):
        buttonDIF = PATTERN_BUTTON(buttonName="DOC. INF. FUNCIONÁRIOS", master=self.frameForUsage, gridRow=1, gridColumn=0, function=print, padTuple=((50, 0), (75, 0)))
        buttonCC = PATTERN_BUTTON(buttonName="CONTRACHEQUE", master=self.frameForUsage, gridRow=1, gridColumn=1, function=print, padTuple=((35, 0), (75, 0)))
        buttonCP = PATTERN_BUTTON(buttonName="CARTÃO DE PONTO", master=self.frameForUsage, gridRow=2, gridColumn=0, function=print, padTuple=((50, 0), (25, 0)))
        buttonHE = PATTERN_BUTTON(buttonName="SOLICITAÇÃO DE HE", master=self.frameForUsage, gridRow=2, gridColumn=1, function=print, padTuple=((35, 0), (25, 0)))
        buttonAll = PATTERN_BUTTON_WITH_COLUMNSPAN(buttonName="REALIZAR TODOS", master=self.frameForUsage, gridRow=3, gridColumn=0, gridColumnspan=2,
                                       function=print, padTuple=((50, 0), (50, 0)), sticky='ew')
        
        ShareHereby.buttonsFromTopFrame = [buttonDIF.get(), buttonCC.get(), buttonCP.get(), buttonHE.get(), buttonAll.get()]
        
    def buildLabel(self):
        self.label = customtkinter.CTkLabel(master=self.frameForUsage, text='Defina um Diretório de Orientação', font=("Robolo", 20, "bold"))
        self.label.grid(row=0, column=0, columnspan=2, padx=(50, 0), pady=(45, 0))
        
        ShareHereby.labelFromTopFrame = self.label